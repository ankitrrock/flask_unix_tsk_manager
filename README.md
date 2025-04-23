# 🧠 Flask Unix-Inspired Task Manager API

A lightweight RESTful API that mimics Unix-style process management with simple task operations like `ls` (list tasks) and `fork` (create a task). Built using Flask, SQLite, and Docker.

---

## 🚀 Features

- Create new tasks (like `fork`)
- List all tasks (like `ls`)
- Get a task by ID
- Delete a task by ID
- Built with Flask + SQLAlchemy + SQLite
- Containerized with Docker

---

## 📦 Setup Instructions

### 🐍 1. Clone and Set Up Virtual Environment

```bash
git clone https://github.com/ankitrrock/flask_unix_task_manager.git
cd flask_unix_task_manager
python -m venv env
source env/bin/activate  # or env\Scripts\activate on Windows
pip install -r requirements.txt


🐳 2. Run with Docker 
docker build -t flask-task-api .
docker run -p 5000:5000 flask-task-api



🔄 Create a Task
curl --location 'http://localhost:5000/tasks' \
--header 'Content-Type: application/json' \
--data '{"name": "Backup logs",
"access_token":"0000"
}'

📥 GET /tasks
curl --location --request GET 'http://localhost:5000/tasks' \
--header 'Content-Type: application/json' \
--data '{
"access_token":"0000"
}'

🔍 POST /tasks/<id>
curl --location --request GET 'http://localhost:5000/tasks/7' \
--header 'Content-Type: application/json' \
--data '{
"access_token":"0000"
}'

🗑️ DELETE /tasks/<id>
curl --location --request DELETE 'http://localhost:5000/tasks/8' \
--header 'Content-Type: application/json' \
--data '{
"access_token":"0000"
}'