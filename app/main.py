from fastapi import FastAPI, HTTPException, status
from .database import (
    create_tasks,
    get_all_tasks,
    get_task_by_id,
    update_task,
    delete_task,
    mark_as_completed
)
from .schemas.schema import TaskCreate, TaskUpdate
from .exceptions import DataBaseConnectionError

app = FastAPI(
    title="Todo API",
    description="Simple task management API with proper error handling",
    version="2.0.0"
)

# Global exception handler for database connection errors
@app.exception_handler(DataBaseConnectionError)
async def database_exception_handler(request, exc):
    return {
        "error": "Database Error",
        "message": str(exc),
        "status_code": 500
    }

@app.post("/tasks", status_code=status.HTTP_201_CREATED)
def create_tasks_endpoint(task: TaskCreate):
    """
    Create a new task.

    Returns:
            201: Task created successfully.
            500: Database connection error.
    """
    try:
        create_tasks(task.title, task.description, task.due_date)
        return {
            "message": "Task created successfully",
            "status": "success"
            }
    except DataBaseConnectionError:
        raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail="Database connection Failed"
                )

@app.get("/tasks")
def get_tasks_endpoint():
    """
    Get all tasks.

    Returns:
            200: List of tasks
            500: Database Error
    """
    try:
        task = get_all_tasks()
        return {
            "tasks": task,
            "total": len(task)
            }
    except DataBaseConnectionError:
        raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail="Database connection Failed"
                )

@app.get("/tasks/{task_id}", status_code=status.HTTP_200_OK)
def get_task_by_id_endpoint(task_id: int):
    """
    Get a task by ID.
    
    Returns:
        200: Task found
        404: Task not found
        500: Database error
    """
    try:
        task = get_task_by_id(task_id)
        
        if task is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Task with ID {task_id} not found"
            )
        
        # Convertir tupla a diccionario para mejor formato
        return {
            "id": task[0],
            "title": task[1],
            "description": task[2],
            "created_at": str(task[3]),
            "due_date": str(task[4]) if task[4] else None,
            "is_completed": task[5]
        }
        
    except DatabaseConnectionError:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Database connection failed"
        )

@app.put("/tasks/{task_id}", status_code=status.HTTP_200_OK)
def update_tasks_endpoint(task_id: int, task: TaskUpdate):
    """
    Update a task.

    Returns:
            200: Task updated successfully
            404: Task not found
            500: Database Error
    """
    try:
        update = update_task(task_id, task.title, task.description, task.due_date)

        if not update:
            raise HTTPException(
                    status_code=status.HTTP_404_NOT_FOUND,
                    detail=f"Task with ID {task_id} not found"
                    )

        return {
            "message": "Task updated successfully",
            "task_id": task_id
            }
    except DataBaseConnectionError:
        raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail="Database connection Failed"
                )

@app.delete("/tasks/{task_id}", status_code=status.HTTP_200_OK)
def delete_task_endpoint(task_id: int):
    """
    Delete a task by ID.

    Returns:
            200: Task deleted successfully
            404: Task not found
            500: Database Error
    """
    try:
        deleted = delete_task(task_id)
        
        if not deleted:
                raise HTTPException(
                        status_code=status.HTTP_404_NOT_FOUND,
                        detail=f"Task with ID {task_id} not found"
                        )

        return {
            "message": "Task deleted successfully",
            "task_id": task_id
        }
    except DataBaseConnectionError:
        raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail="Database connection Failed"
                )

@app.patch("/tasks/{task_id}/complete", status_code=status.HTTP_200_OK)
def mark_as_completed_endpoint(task_id: int):
    """
    Mark a task as completed by ID.

    Returns:
            200: Task marked as completed successfully

            500: Database Error
    """
    try:
        mark_as_completed(task_id)
        return {
            "message": "Task marked as completed",
            "task_id": task_id
        }
    except DataBaseConnectionError:
        raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail="Database connection Failed"
                )