import psycopg2
from psycopg2.extras import RealDictCursor
from config import DB_NAME, DB_USERNAME, DB_PASSWORD, DB_HOST, DB_PORT, DATABASE_URL

def get_db_connection():

    if DATABASE_URL:
        return psycopg2.connect(
            DATABASE_URL, 
            cursor_factory=RealDictCursor
        )

    return psycopg2.connect(
        dbname=DB_NAME, 
        user=DB_USERNAME, 
        password=DB_PASSWORD,
        host=DB_HOST, 
        port=DB_PORT,
        cursor_factory=RealDictCursor # This makes rows behave like Python dictionaries
    )

# FastAPI Dependency
def get_db():
    conn = get_db_connection()
    try:
        yield conn
    finally:
        conn.close()

def init_db():
    """Creates the necessary tables if they don't exist."""
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS chat_messages (
            id SERIAL PRIMARY KEY,
            sender VARCHAR(50) NOT NULL,
            content TEXT NOT NULL,
            timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        );
    """)
    conn.commit()
    cur.close()
    conn.close()

if __name__ == "__main__":
    init_db()