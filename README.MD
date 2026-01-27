# TODO API - Task Management System

![Tests](https://github.com/tu-usuario/todo-api-testing/actions/workflows/tests.yml/badge.svg)
![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=for-the-badge&logo=fastapi&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![MySQL](https://img.shields.io/badge/MySQL-4479A1?style=for-the-badge&logo=mysql&logoColor=white)
![Pytest](https://img.shields.io/badge/Pytest-0A9EDC?style=for-the-badge&logo=pytest&logoColor=white)

A professional REST API for task management built with FastAPI, MySQL, and comprehensive test coverage.

---

## 🎯 Features

- ✅ **CRUD Operations** - Create, Read, Update, Delete tasks
- ✅ **Task Completion** - Mark tasks as completed
- ✅ **Professional Error Handling** - HTTP status codes (200, 201, 404, 500)
- ✅ **API Documentation** - Interactive Swagger UI
- ✅ **Comprehensive Testing** - Unit and integration tests with Pytest
- ✅ **Database Integration** - MySQL with PyMySQL

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

# Linux/Mac

source venv/bin/activate

````

3. Install dependencies:

```bash
pip install -r requirements.txt
````

4. Create the Database:

````sql
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

**Set up database:**
```sql
   CREATE DATABASE all_tasks_testing_practice;
   USE all_tasks_testing_practice;

   -- Run the schema from database/schema.sql
````

````

5. **Configure database connection:**

   Update `app/database.py` with your MySQL credentials:
```python
   conn = pymysql.connect(
       host='localhost',
       port=3306,
       user='your_user',      # Change this
       passwd='your_password', # Change this
       db='all_tasks_testing_practice'
   )
```

## ▶️ Running the API

### **Development Server:**
```bash
uvicorn app.main:app --reload
```

Open: `http://127.0.0.1:8000/docs`

The API will be available at:
- **API:** http://127.0.0.1:8000
- **Interactive Docs:** http://127.0.0.1:8000/docs
- **OpenAPI Spec:** http://127.0.0.1:8000/openapi.json


## 🧪 Run Tests

```bash
# All tests
pytest tests/ -v

# Database tests only
pytest tests/test_database.py -v

# API tests only
pytest tests/test_api.py -v
```

## 📚 API Endpoints

### **Tasks**

| Method | Endpoint | Description | Status Codes |
|--------|----------|-------------|--------------|
| POST | `/tasks` | Create a new task | 201, 500 |
| GET | `/tasks` | Get all tasks | 200, 500 |
| GET | `/tasks/{id}` | Get task by ID | 200, 404, 500 |
| PUT | `/tasks/{id}` | Update a task | 200, 404, 500 |
| DELETE | `/tasks/{id}` | Delete a task | 200, 404, 500 |
| PATCH | `/tasks/{id}/complete` | Mark as completed | 200, 500 |

## 📝 API Usage Examples

### **Create a Task**

**Request:**
```bash
POST /tasks
Content-Type: application/json

{
  "title": "Buy groceries",
  "description": "Milk, eggs, bread",
  "due_date": "2024-12-31T23:59:59"
}
```

**Response (201 Created):**
```json
{
  "message": "Task created successfully",
  "status": "success"
}
```

---

### **Get All Tasks**

**Request:**
```bash
GET /tasks
```

**Response (200 OK):**
```json
{
  "tasks": [
    [1, "Buy groceries", "Milk, eggs, bread", "2024-01-15 10:00:00", "2024-12-31 23:59:59", 0],
    [2, "Finish report", "Q4 sales report", "2024-01-16 09:00:00", null, 1]
  ],
  "total": 2
}
```

---

### **Get Task by ID**

**Request:**
```bash
GET /tasks/1
```

**Response (200 OK):**
```json
[1, "Buy groceries", "Milk, eggs, bread", "2024-01-15 10:00:00", "2024-12-31 23:59:59", 0]
```

**Response (404 Not Found):**
```json
{
  "detail": "Task with ID 999 not found"
}
```

---

### **Update a Task**

**Request:**
```bash
PUT /tasks/1
Content-Type: application/json

{
  "title": "Buy groceries (UPDATED)",
  "description": "Milk, eggs, bread, butter",
  "due_date": "2024-12-25T23:59:59"
}
```

**Response (200 OK):**
```json
{
  "message": "Task updated successfully",
  "task_id": 1
}
```

---

### **Mark Task as Completed**

**Request:**
```bash
PATCH /tasks/1/complete
```

**Response (200 OK):**
```json
{
  "message": "Task marked as completed",
  "task_id": 1
}
```

---

### **Delete a Task**

**Request:**
```bash
DELETE /tasks/1
```

**Response (200 OK):**
```json
{
  "message": "Task deleted successfully",
  "task_id": 1
}
```

---

## ⚠️ Error Responses

### **404 - Task Not Found**
```json
{
  "detail": "Task with ID 999 not found"
}
```

### **500 - Database Connection Error**
```json
{
  "error": "Database Error",
  "message": "Error connecting to the database: ...",
  "status_code": 500
}
```

---

## 🧪 Running Tests

### **Run all tests:**
```bash
pytest tests/ -v
```

### **Run specific test file:**
```bash
pytest tests/test_database.py -v
pytest tests/test_api.py -v
```

### **Run with coverage:**
```bash
pytest tests/ --cov=app --cov-report=html
```

### **Test Structure:**
```
tests/
├── conftest.py           # Test configuration
├── test_database.py      # Database function tests
└── test_api.py           # API endpoint tests
```

---

## 📊 Test Coverage

| Module | Tests | Coverage |
|--------|-------|----------|
| `database.py` | 6 tests | CRUD operations |
| `main.py` | 6 tests | All endpoints |
| **Total** | **12 tests** | Core functionality |

---

## 🏗️ Project Structure
```
todo-api-testing/
├── app/
│   ├── __init__.py
│   ├── main.py              # FastAPI application
│   ├── database.py          # Database operations
│   ├── exceptions.py        # Custom exceptions
│   └── schemas/
│       └── schema.py        # Pydantic models
├── tests/
│   ├── __init__.py
│   ├── conftest.py          # Pytest configuration
│   ├── test_database.py     # Database tests
│   └── test_api.py          # API tests
├── requirements.txt
├── .gitignore
└── README.md
```

---

## 🛠️ Technologies Used

- **FastAPI** - Modern web framework for building APIs
- **MySQL** - Relational database
- **PyMySQL** - MySQL connector for Python
- **Pytest** - Testing framework
- **Pydantic** - Data validation
- **Uvicorn** - ASGI server

---

## 🔒 Security Considerations

⚠️ **This is a development/testing project. For production:**

1. **Never commit database credentials** - Use environment variables
2. **Use connection pooling** - For better performance
3. **Add authentication** - Implement JWT or OAuth2
4. **Input validation** - Already using Pydantic, but add more
5. **SQL injection protection** - Using parameterized queries ✅
6. **HTTPS only** - In production

---

## 🚧 Future Improvements

- [ ] Add user authentication (JWT)
- [ ] Implement pagination for `/tasks`
- [ ] Add task filtering and sorting
- [ ] Task priority levels
- [ ] Task categories/tags
- [ ] Due date reminders
- [ ] Soft delete (instead of hard delete)
- [ ] API rate limiting
- [ ] Docker containerization
- [ ] CI/CD pipeline with GitHub Actions

---

## 📖 API Documentation

Interactive API documentation is available at:
- **Swagger UI:** http://127.0.0.1:8000/docs
- **ReDoc:** http://127.0.0.1:8000/redoc

---

## 🤝 Contributing

This is a personal learning project, but suggestions are welcome!

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Open a Pull Request

---

## 👤 Chande De Vargas

GitHub: https://github.com/ChandeDeVargas
LinkedIn: https://www.linkedin.com/in/chande-de-vargas-b8a51838a/


---

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

---

**⭐ If this project helped you learn, give it a star!**
````
