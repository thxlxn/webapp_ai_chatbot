# webapp_ai_chatbot
***extremely raw and WIP***

## Installation and Setup
### Clone the Repository
```bash
git clone https://github.com/thxlxn/webapp_ai_chatbot.git
```
### Database Configuration
This project supports two ways to connect to PostgreSQL, depending on your preference. <br/>
<br/>
**Option A: Local Docker (Recommended for Development)**<br/>
Define the individual variables in the `.env` file:
```env
DB_NAME=chatbot_db
DB_USERNAME=postgres
DB_PASSWORD=postgres
DB_HOST=localhost
DB_PORT=5432
```
Spin up the included `docker-compose.yml` file:
```bash
docker-compose --env-file ./chatbot/backend/.env up -d
```
**Option B: Cloud Database**<br/>
If you prefer to use a hosted database, you can bypass the Docker container entirely. Simply provide a standard PostgreSQL connection URI in the `.env` file. If this variable is present, the application will automatically use it instead of the local credentials:<br/>
```env
DATABASE_URL=postgresql://username:password@your-cloud-host.com:5432/dbname
```
### Groq API Key
TODO
## Running the App
Simply execute the following command:
```bash
npm run dev
```
If you prefer having your backend and frontend in separate terminal windows so their logs don't mix, run the following:
```bash
.\start.bat
```
