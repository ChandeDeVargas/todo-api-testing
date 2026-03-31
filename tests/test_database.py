from app.database import (
    create_tasks,
    get_all_tasks,
    get_task_by_id,
    delete_task,
    mark_as_completed,
    update_task
)


def test_create_task():
    # Arrange
    title = "Test Task"
    description = "Testing Create Function"

    # Act
    task_id = create_tasks(title, description)
    tasks = get_all_tasks()

    # Assert
    assert len(tasks) > 0
    assert task_id is not None


def test_get_all_task():
    # Arrange
    title = "Test Task"
    description = "Testing Get All Task"
    create_tasks(title, description)
    
    # Act
    tasks = get_all_tasks()
    
    # Assert
    assert tasks is not None
    assert type(tasks) is list


def test_get_task_by_id():
    # Arrange: Create a task to be able to search for it
    title = "Test task for searching"
    description = "Test description"
    task_id = create_tasks(title, description)

    # Act: Retrieve the specific task by its ID
    task = get_task_by_id(task_id)

    # Assert: Verify that the exact task was retrieved
    assert task is not None
    assert task["id_tasks"] == task_id
    assert task["title"] == title
    assert task["description"] == description


def test_update_task():
    # Arrange: Create a new task
    task_id = create_tasks("Original title", "Original description")

    # Act: Update the task details
    new_title = "Updated title"
    new_description = "Updated description"
    update_task(task_id, new_title, new_description, None)

    # Assert: Verify the task details have been updated
    updated_task = get_task_by_id(task_id)
    assert updated_task["title"] == new_title
    assert updated_task["description"] == new_description


def test_delete_task():
    # Arrange: Create a task designed to be deleted
    task_id = create_tasks("Task to delete", "This task will be deleted")

    # Act: Delete the task
    delete_task(task_id)

    # Assert: Verify the task can no longer be found
    deleted_task = get_task_by_id(task_id)
    assert deleted_task is None


def test_mark_as_completed():
    # Arrange: Create a task designed to be completed
    task_id = create_tasks("Finished task", "This task will be marked as completed")

    # Act: Complete the task
    mark_as_completed(task_id)
    
    # Assert: Verify the 'is_completed' flag is enabled
    completed_task = get_task_by_id(task_id)
    assert completed_task is not None
    assert completed_task["is_completed"] == 1