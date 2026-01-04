from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_create_task_endpoint():
    # 1. ARRANGE: Prepare data for sending.
    task_data = {
        "title": "Task From test",
        "description": "Testing data of POST",
        "due_date": "2026-12-31"
    }

    # 2. ACT: Make the requests POST.
    response = client.post("/tasks", json=task_data)

    # 3. ASSERT: Verified
    assert response.status_code == 201
    assert response.json()["Message"] == "Task Created Successfully"

def test_get_all_tasks_endpoint():
    task_data = {
        "title": "Task GET",
        "description": "Testing endpoint GET",
        "due_date": "2026-12-31"
    }

    client.post("/tasks", json=task_data)

    response = client.get("/tasks")

    assert response.status_code == 200
    body = response.json()

    assert "tasks" in response.json()
    assert len(body["tasks"]) > 0


def test_get_task_by_id_endpoint():
    # 1. ARRANGE: Create a task first.
    task_data = {
        "title": "Task by ID",
        "description": "testing endpoint GET by id",
        "due_date": "2026-12-31"
    }
    client.post("/tasks", json=task_data)  # Create Task

    # Get all tasks to know ID the last.
    tasks = client.get("/tasks").json()["tasks"]
    task_id = tasks[-1][0]  # The ID is in position [0]

    # 2. ACT: Search for this task by ID
    response = client.get(f"/tasks/{task_id}")

    # 3. ASSERT: Verified the request.
    assert response.status_code == 200
    task = response.json()

    assert task[0] == task_id
    assert task[1] == task_data["title"]


def test_update_task_endpoint():
    # 1. ARRANGE: Create a task first.
    task_data = {
        "title": "Original",
        "description": "Desc original",
        "due_date": "2026-01-01"
    }
    client.post("/tasks", json=task_data)

    # Get ID from task create.
    tasks = client.get("/tasks").json()["tasks"]
    task_id = tasks[-1][0]

    # 2. ACT: Update task.
    updated_data = {
        "title": "Task Update",
        "description": "Desc update",
        "due_date": "2026-12-31"
    }

    # Check if the ID exists
    check = client.get(f"/tasks/{task_id}")
    print(check.json())
    assert check.status_code == 200

    response = client.put(f"/tasks/{task_id}", json=updated_data)

    # 3. ASSERT: Verified.
    assert response.status_code == 200
    assert response.json()["Message"] == "Task Updated Successfully"

def test_delete_task_endpoint():
    task_data = {
        "title": "Task delete",
        "description": "Task at delete",
    }

    client.post("/tasks", json=task_data)


    tasks = client.get("/tasks").json()["tasks"]
    task_id = tasks[-1][0]

    response = client.delete(f"/tasks/{task_id}")

    assert response.status_code == 200
    assert response.json()["Message"] == "Task Deleted Successfully"

    assert client.get(f"/tasks/{task_id}").status_code == 404

def test_mark_as_completed_endpoint():
    task_data = {
        "title": "Task Completed",
        "description": "Task will be completed",
    }

    client.post("/tasks", json=task_data)

    tasks = client.get("/tasks").json()["tasks"]
    task_id = tasks[-1][0]

    response = client.patch(f"/tasks/{task_id}/complete")

    assert response.status_code == 200
    assert response.json()["Message"] == "Task marked as completed successfully"

    task = client.get(f"/tasks/{task_id}").json()
    assert task[5] == 1


