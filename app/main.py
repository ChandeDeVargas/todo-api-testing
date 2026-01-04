from fastapi import FastAPI, HTTPException
from app.database import (
    create_tasks,
    get_all_tasks,
    get_task_by_id,
    update_task,
    delete_task,
    mark_as_completed
)
from app.schemas.schema import TaskCreate, TaskUpdate

app = FastAPI()

# Create a new Task
@app.post("/tasks", status_code=201)
def create_tasks_endpoint(task: TaskCreate):
    create_tasks(task.title, task.description, task.due_date)
    return {"Message": "Task Created Successfully",
            "status": "success"}

@app.get("/tasks")
def get_tasks_endpoint():
    task = get_all_tasks()
    return {
        "tasks": task,
        "total": len(task)
    }

@app.get("/tasks/{task_id}")
def get_task_by_id_endpoint(task_id: int):
    task = get_task_by_id(task_id)

    if task is None:
        raise HTTPException(status_code=404, detail="Task not found")

    return task


@app.put("/tasks/{task_id}")
def update_tasks_endpoint(task_id: int, task: TaskUpdate):
    update = update_task(task_id, task.title, task.description, task.due_date)

    if not update:
        raise HTTPException(status_code=404, detail="Task not found")

    return {"Message": "Task Updated Successfully"}

@app.delete("/tasks/{task_id}")
def delete_task_endpoint(task_id: int):
    delete_task(task_id)
    return {"Message": "Task Deleted Successfully",}

@app.patch("/tasks/{task_id}/complete")
def mark_as_completed_endpoint(task_id: int):
    mark_as_completed(task_id)
    return {"Message": "Task marked as completed successfully"}