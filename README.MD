# TODO API - Practice Project

REST API to manage tasks (TODO list) built with FastAPI, MySQL, and tested with Pytest.
## 🚀 Tecnologies

- **FastAPI** - Web Framework
- **MySQL** - DataBase
- **PyMySQL** - MySql Connector
- **Pytest** - Automated Testing
- **Uvicorn** - ASGI Server

## 📋 Requirements

- Python 3.8+
- MySQL 8.0+

## ⚙️ Installation

1. Clone the repository:
```bash
git clone https://github.com/tu-usuario/todo-api.git
cd todo-api
```

2. Create virtual Environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Create the Database:
```sql
CREATE DATABASE all_tasks_testing_practice;
USE all_tasks_testing_practice;

CREATE TABLE tasks(
    id_tasks INT PRIMARY KEY AUTO_INCREMENT,
    title VARCHAR(100) NOT NULL,
    description VARCHAR(500) NOT NULL,
    create_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    due_date DATETIME,
    is_completed TINYINT(1) DEFAULT 0
);
```

5. Configure database credentials in `app/database.py`

## 🏃 Run The API
```bash
uvicorn app.main:app --reload
```

Abre: `http://127.0.0.1:8000/docs`

## 🧪 Run Tests
```bash
# All tests
pytest tests/ -v

# Database tests only
pytest tests/test_database.py -v

# API tests only
pytest tests/test_api.py -v
```

## 📚 Endpoints

| Method | Endpoint | Description       |
|--------|----------|-------------------|
| POST   | `/tasks` | Create task       |   
| GET    | `/tasks` | Get all tasks     |
| GET    | `/tasks/{id}` | Get task by ID    |
| PUT    | `/tasks/{id}` | Update task       |
| DELETE | `/tasks/{id}` | Delete task       |
| PATCH  | `/tasks/{id}/complete` | Mark as completed |

## 📖 Learnings

This project was created to practice:
- Automated testing with pytest
- REST API development with FastAPI
- MySQL Integration
- HTTP endpoint testing

🧠 What you already master (and it’s important to know it)

✔ FastAPI REST endpoints  
✔ Testing with pytest + TestClient  
✔ API ↔ DB contract  
✔ Proper 404 handling  
✔ Business logic outside the endpoint  
✔ QA + Backend mindset (very valuable)  
