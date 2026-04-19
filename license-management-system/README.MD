# License Management System

A backend system built using FastAPI to manage users, licenses, and expiry workflows.

## 🚀 Features
- User Registration & Authentication
- Secure password hashing (bcrypt)
- RESTful API design
- License creation & expiry tracking
- Swagger API documentation

## 🛠 Tech Stack
- Python (FastAPI)
- SQLAlchemy (ORM)
- SQLite (local DB)
- Uvicorn
- Passlib (bcrypt)

## 📌 API Endpoints
- POST /register → Register user
- POST /login → Login user
- POST /license → Create license

## ▶️ Run Locally
```bash
pip install -r requirements.txt
python -m uvicorn app.main:app --reload
