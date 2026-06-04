@echo off
echo Starting Portfolio Chatbot...

:: Start the FastAPI backend in a new window
start "FastAPI Backend" cmd /k "cd backend/app && uvicorn api:app --reload"

:: Start the React frontend in a new window
start "React Frontend" cmd /k "npm run dev --prefix frontend"