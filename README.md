# 🚀 Cloud-Based Task Management System

A production-ready **RESTful Task Management API** built using FastAPI, MySQL, JWT authentication, and Docker.

This project demonstrates backend system design, secure authentication, CRUD operations, and containerized deployment — designed to showcase Software Development Engineer (SDE) level skills.

---

## 📌 Features

* 🔐 JWT Authentication
* 👥 User Registration & Login
* 🛡 Role-Based Access (User / Admin ready)
* 📋 Full CRUD Operations for Tasks
* 🔎 Pagination, Filtering & Search (extendable)
* 🐳 Dockerized MySQL Database
* 🧱 Clean Layered Architecture
* 📖 Auto API Documentation (Swagger UI)

---

## 🏗 Tech Stack

* Python 3.11
* FastAPI
* SQLAlchemy ORM
* MySQL 8 (Docker)
* JWT (python-jose)
* Passlib (bcrypt)
* Docker & Docker Compose

---

## 📂 Project Structure

```
Cloud-Based-Task-Management-System/
│
├── app/
│   ├── main.py
│   ├── database.py
│   ├── models.py
│   ├── schemas.py
│   ├── auth.py
│   ├── dependencies.py
│   ├── routers/
│   │     ├── auth.py
│   │     └── tasks.py
│
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
├── .env
└── README.md
```

---

## ⚙️ Setup Instructions

---

### 🔹 Option 1: Run with Docker (Recommended)

### 1️⃣ Clone Repository

```bash
git clone https://github.com/lithinspark/Cloud-Based-Task-Management-System.git
cd Cloud-Based-Task-Management-System
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

Swagger Documentation:

```
http://localhost:8000/docs
```

---

## 🔐 Authentication Flow

---

### 📝 Register User

**POST** `/auth/register`

```json
{
  "username": "john",
  "email": "john@example.com",
  "password": "password123"
}
```

---

### 🔑 Login

**POST** `/auth/login`

Returns:

```json
{
  "access_token": "JWT_TOKEN"
}
```

Use token in headers:

```
Authorization: Bearer <JWT_TOKEN>
```

---

## 📋 Task CRUD Endpoints

| Method | Endpoint    | Description    |
| ------ | ----------- | -------------- |
| POST   | /tasks      | Create task    |
| GET    | /tasks      | Get user tasks |
| PUT    | /tasks/{id} | Update task    |
| DELETE | /tasks/{id} | Delete task    |

---

## 🗄 Database Schema

### Users Table

* id (UUID)
* username (Unique)
* email (Unique)
* password_hash
* role
* created_at

---

### Tasks Table

* id (UUID)
* title
* description
* owner_id (Foreign Key → users)
* created_at

---

## 🔄 REST API Principles Used

* Resource-based URLs
* Stateless authentication (JWT)
* Proper HTTP methods
* JSON responses
* HTTP status codes
* Modular router structure

---

## 🐳 Docker Services

### MySQL Container

* Image: mysql:8
* Port: 3306
* Persistent storage enabled

### API Container

* Runs FastAPI
* Exposed on port 8000

---

## 🧪 Testing

Test using:

* Swagger UI (`/docs`)
* Postman
* curl

Example:

```bash
curl -X GET http://localhost:8000/tasks \
  -H "Authorization: Bearer YOUR_TOKEN"
```

---

## 🚀 Future Enhancements

* Refresh Tokens
* Role-Based Admin APIs
* Pagination & Filtering
* Redis Caching
* Rate Limiting
* CI/CD Pipeline
* AWS Deployment
* Alembic Migrations

---

## 🎯 Learning Objectives

This project demonstrates:

* Backend architecture design
* Secure authentication implementation
* REST API best practices
* Database relationships
* Containerized deployment
* Production-ready API structure

---

## 👨‍💻 Author

Lithin Spark
Backend Developer | FastAPI | MySQL | Docker

---

If you want, I can now:

* 🔥 Make it more professional (Open-source style)
* 🔥 Add architecture diagram section
* 🔥 Add shields & GitHub badges
* 🔥 Write ATS-optimized project description
* 🔥 Create deployment section for AWS

Tell me your next step 🚀
