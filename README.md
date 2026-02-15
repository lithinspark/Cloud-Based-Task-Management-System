# Cloud-Based-Task-Management-System


---

# 📘 Smart Task Management API

A production-ready **Task Management REST API** built using FastAPI, MySQL, Docker, JWT authentication, and Role-Based Access Control (RBAC).

This project demonstrates backend architecture, authentication, authorization, pagination, filtering, and containerized deployment.

---

# 🚀 Features

* ✅ User Registration & Login
* ✅ JWT Authentication
* ✅ Role-Based Access Control (User/Admin)
* ✅ Task CRUD Operations
* ✅ Pagination
* ✅ Search by Title
* ✅ Filter by Status
* ✅ MySQL Database
* ✅ Dockerized Environment
* ✅ Production-Ready Structure

---

# 🏗️ Tech Stack

* Python 3.11
* FastAPI
* SQLAlchemy ORM
* MySQL 8
* Docker & Docker Compose
* JWT (python-jose)
* Bcrypt Password Hashing

---

# 📂 Project Structure

```
smart-task-api/
│
├── app/
│   ├── main.py
│   ├── database.py
│   ├── models.py
│   ├── schemas.py
│   ├── auth.py
│   ├── dependencies.py
│   ├── routers/
│
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
├── .env
└── README.md
```

---

# 🛠️ Installation & Setup

---

## 🔹 Option 1: Run Using Docker (Recommended)

### 1️⃣ Clone Repository

```bash
git clone <your-repo-url>
cd smart-task-api
```

---

### 2️⃣ Create `.env` File

```
MYSQL_ROOT_PASSWORD=rootpassword
MYSQL_DATABASE=smart_tasks
MYSQL_USER=appuser
MYSQL_PASSWORD=apppassword

DATABASE_URL=mysql+pymysql://appuser:apppassword@db:3306/smart_tasks
SECRET_KEY=supersecretkey
```

---

### 3️⃣ Run Docker Compose

```bash
docker compose up --build
```

---

### 4️⃣ Access API

Swagger UI:

```
http://localhost:8000/docs
```

---

## 🔹 Option 2: Run Locally Without Docker

### 1️⃣ Create Virtual Environment

```bash
python -m venv venv
venv\Scripts\activate   # Windows
```

---

### 2️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 3️⃣ Set Database URL

If MySQL running locally:

```
mysql+pymysql://appuser:apppassword@localhost:3306/smart_tasks
```

---

### 4️⃣ Start Server

```bash
uvicorn app.main:app --reload
```

---

# 🔐 Authentication

## Register

```
POST /auth/register
```

Body:

```json
{
  "username": "john",
  "email": "john@example.com",
  "password": "password123"
}
```

---

## Login

```
POST /auth/login
```

Returns:

```json
{
  "access_token": "JWT_TOKEN"
}
```

Use token in header:

```
Authorization: Bearer <token>
```

---

# 📋 Task Endpoints

| Method | Endpoint    | Description                      |
| ------ | ----------- | -------------------------------- |
| POST   | /tasks      | Create task                      |
| GET    | /tasks      | Get tasks (pagination supported) |
| GET    | /tasks/{id} | Get single task                  |
| PUT    | /tasks/{id} | Update task                      |
| DELETE | /tasks/{id} | Delete task                      |

---

# 🔎 Query Parameters

```
/tasks?page=1&limit=10&status=pending&search=meeting&sort=desc
```

Supports:

* Pagination
* Filtering by status
* Search by title
* Sorting by created_at

---

# 👥 Role-Based Access Control

### User

* Create task
* View own tasks
* Update own tasks
* Delete own tasks

### Admin

* View all tasks
* Delete any task
* View all users
* Delete users

---

# 🗄️ Database Schema

## Users Table

| Field         | Type      |
| ------------- | --------- |
| id            | UUID      |
| username      | VARCHAR   |
| email         | VARCHAR   |
| password_hash | TEXT      |
| role          | ENUM      |
| created_at    | TIMESTAMP |

---

## Tasks Table

| Field       | Type      |
| ----------- | --------- |
| id          | UUID      |
| title       | VARCHAR   |
| description | TEXT      |
| status      | ENUM      |
| owner_id    | UUID      |
| created_at  | TIMESTAMP |

---

# 🐳 Docker Configuration

### MySQL Service

* Image: mysql:8
* Port: 3306
* Persistent Volume enabled

### API Service

* Built from Dockerfile
* Runs on port 8000

---

# 🧪 Testing

You can test endpoints using:

* Swagger UI (`/docs`)
* Postman
* curl

---

# ⚠ Common Issues

### Port Already in Use

Change port mapping in docker-compose.yml

### Access Denied Error

Check:

* Username
* Password
* Database name

### Cannot Connect to DB

Ensure:

* Container is running
* Correct DATABASE_URL
* Correct host (db or localhost)

---

# 🚀 Future Improvements

* Add Refresh Tokens
* Add Redis Caching
* Add Rate Limiting
* Add Alembic Migrations
* Deploy to AWS EC2
* Add CI/CD Pipeline

---

# 📌 Learning Outcomes

This project demonstrates:

* Backend system design
* JWT authentication
* Role-based authorization
* Database relationships
* Query optimization
* Dockerized deployment
* Production-level API design

---

# 📄 License

This project is for educational and demonstration purposes.

---

# 👨‍💻 Author
  Lithin Spark
Backend Developer | FastAPI | MySQL | Docker

