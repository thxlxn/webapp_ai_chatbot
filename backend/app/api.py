import os
from fastapi import FastAPI, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from openai import OpenAI
from dotenv import load_dotenv
from contextlib import asynccontextmanager

from database import get_db, init_db
from schemas import MessageCreate
from config import GROQ_API_KEY

load_dotenv()

# Initialize the database table on startup
@asynccontextmanager
async def lifespan(app: FastAPI):
    print("Server starting up... Initializing the database...")
    init_db()
    
    yield
    
    print("Server shutting down.")

# Pass the lifespan context manager
app = FastAPI(lifespan=lifespan)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

client = OpenAI(
    api_key=GROQ_API_KEY,
    base_url="https://api.groq.com/openai/v1"
)

@app.post("/api/chat")
async def chat_endpoint(payload: MessageCreate, conn = Depends(get_db)):
    user_content = payload.content
    cur = conn.cursor()

    try:
        # 1. Save user message
        cur.execute(
            "INSERT INTO chat_messages (sender, content) VALUES (%s, %s)",
            ("user", user_content)
        )
        conn.commit()

        # 2. Fetch recent context for the LLM
        cur.execute("""
            SELECT sender, content FROM chat_messages 
            ORDER BY timestamp DESC LIMIT 10
        """)
        recent_messages = cur.fetchall()
        recent_messages.reverse() # Oldest to newest

        messages = [{"role": "system", "content": "You are a helpful portfolio chatbot assistant."}]
        
        for msg in recent_messages[:-1]: # exclude the one we just inserted
            role = "user" if msg["sender"] == "user" else "assistant"
            messages.append({"role": role, "content": msg["content"]})
            
        messages.append({"role": "user", "content": user_content})

        # 3. Call LLM API
        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile", 
            messages=messages
        )
        bot_response = response.choices[0].message.content

        # 4. Save bot response
        cur.execute(
            "INSERT INTO chat_messages (sender, content) VALUES (%s, %s)",
            ("bot", bot_response)
        )
        conn.commit()

        return {"sender": "bot", "content": bot_response}

    except Exception as e:
        conn.rollback() # Crucial: rollback the transaction on error
        print(f"CRASH REASON: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        cur.close()

@app.get("/api/history")
async def get_history(conn = Depends(get_db)):
    cur = conn.cursor()
    cur.execute("SELECT sender, content FROM chat_messages ORDER BY timestamp ASC")
    messages = cur.fetchall()
    cur.close()
    return messages