from fastapi.testclient import TestClient
from app.main import app
from app.database import (
    create_tasks,
    get_all_tasks,
    get_task_by_id,
    delete_task,
    mark_as_completed,
    update_task
)

client = TestClient(app)


def test_create_task_endpoint():
    """Test creating a new task"""
    response = client.post(
        "/tasks",
        json={
            "title": "Test task",
            "description": "Test description",
            "due_date": "2024-12-31T23:59:59"
        }
    )
    print(f"Staus: {response.status_code}")
    print(f"Response: {response.json()}")
    
    assert response.status_code == 201
    assert response.json()["message"] == "Task created successfully"


def test_get_all_tasks_endpoint():
    """Test getting all tasks"""
    response = client.get("/tasks")
    
    assert response.status_code == 200
    assert "tasks" in response.json()
    assert "total" in response.json()


def test_get_task_by_id_endpoint():
    """Test getting a single task by ID"""
    # Arrange
    title = "Test task for get by id"
    description = "Test description"
    
    create_tasks(title, description)
    
    all_tasks = get_all_tasks()
    task_id = all_tasks[-1][0]
    
    # Act
    response = client.get(f"/tasks/{task_id}")
    
    # Assert
    assert response.status_code == 200
    
    task = response.json()
    assert task["id"] == task_id
    assert task["title"] == title
    assert task["description"] == description


def test_update_task_endpoint():
    """Test updating a task"""
    # Arrange
    create_tasks("Old title", "Old description")
    
    all_tasks = get_all_tasks()
    task_id = all_tasks[-1][0]
    
    # Act
    response = client.put(
        f"/tasks/{task_id}",
        json={
            "title": "Updated title",
            "description": "Updated description",
            "due_date": "2024-12-31T23:59:59"
        }
    )
    
    # Assert
    assert response.status_code == 200
    assert response.json()["message"] == "Task updated successfully"
    
    # Verify changes
    task = get_task_by_id(task_id)
    assert task[1] == "Updated title"
    assert task[2] == "Updated description"


def test_delete_task_endpoint():
    """Test deleting a task"""
    # Arrange
    create_tasks("Task to delete", "Delete me")
    
    all_tasks = get_all_tasks()
    task_id = all_tasks[-1][0]
    
    # Act
    response = client.delete(f"/tasks/{task_id}")
    
    # Assert
    assert response.status_code == 200
    assert response.json()["message"] == "Task deleted successfully"
    
    # Verify deletion
    assert get_task_by_id(task_id) is None


def test_mark_as_completed_endpoint():
    """Test marking a task as completed"""
    # Arrange
    title = "Task to complete"
    description = "Complete this task"
    
    create_tasks(title, description)
    
    all_tasks = get_all_tasks()
    task_id = all_tasks[-1][0]
    
    # Act
    response = client.patch(f"/tasks/{task_id}/complete")
    
    # Assert
    assert response.status_code == 200
    assert response.json()["message"] == "Task marked as completed"
    
    # Verify in database
    task = get_task_by_id(task_id)
    assert task[5] == 1