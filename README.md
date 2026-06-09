# webapp_ai_chatbot
***extremely raw and WIP***

---

## Installation and Setup
### Clone the Repository
```bash
git clone https://github.com/thxlxn/webapp_ai_chatbot.git
```
### Database Configuration
This project supports two ways to connect to PostgreSQL, depending on your preference. <br/>
**NOTE:** The `.env` file must be created in `backend/`. <br/>
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
docker-compose --env-file ./backend/.env up -d
```
**Option B: Cloud Database**<br/>
If you prefer to use a hosted database, you can bypass the Docker container entirely. Simply provide a standard PostgreSQL connection URI in the `.env` file. If this variable is present, the application will automatically use it instead of the local credentials:<br/>
```env
DATABASE_URL=postgresql://username:password@your-cloud-host.com:5432/dbname
```
### Groq API Key
The API key can be obtained for free by registering at [groq.com](https://console.groq.com/home) and clicking **API Keys** in the top right. After that, copy your key and paste it into the `.env` file:
```env
GROQ_API_KEY=gsk_7JSgm8349SBDbmdn8azjgHSf8gz8HG1mb31vnH
```

---

## Running the App
Simply execute the following command:
```bash
npm run dev
```
If you prefer having your backend and frontend in separate terminal windows so their logs don't mix, run the following:
```bash
.\start.bat
```

---

## Note on AI usage
As a backend-focused developer, I utilized AI tools to help write the frontend layer of this application. While I have reviewed and tested the code to ensure it works properly, frontend devs are more than welcome to submit PRs to improve the UI/UX.

---

## License
This project is licensed under the GNU General Public License v3.0 license. See [LICENSE](./LICENSE) for details.
