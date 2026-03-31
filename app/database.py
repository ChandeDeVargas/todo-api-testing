import pymysql
from .exceptions import DatabaseConnectionError
import os
from contextlib import contextmanager
from typing import Generator
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

def get_connection():
    """
    Establish connection to MySQL database using environment variables.
    
    Returns:
        pymysql.Connection: Active database connection
    """
    try:
        # Determine if we are in testing environment
        is_testing_environment = os.getenv('TESTING', 'false').lower() == 'true'

        # Database configuration from environment variables
        # No more hardcoded credentials
        conn = pymysql.connect(
            host=os.getenv('DB_HOST', '127.0.0.1'),
            port=int(os.getenv('DB_PORT', 3306)),
            user=os.getenv('DB_USER', 'root'),
            password=os.getenv('DB_PASSWORD', 'testpassword'),
            db=os.getenv('DB_NAME', 'all_tasks_testing_practice'),
            charset='utf8mb4',
            cursorclass=pymysql.cursors.DictCursor  # Returns dictionaries instead of tuples
        )
        return conn
    except pymysql.MySQLError as e:
        raise DatabaseConnectionError(f"Error connecting to the database: {str(e)}")

@contextmanager
def get_db_connection() -> Generator[pymysql.Connection, None, None]:
    """
    Context manager to handle database connections.
    Ensures connections are always closed properly, even if errors occur.
    
    Yields:
        pymysql.Connection: Database connection
    """
    connection = None
    try:
        connection = get_connection()
        yield connection
    except Exception as e:
        if connection:
            connection.rollback()
        raise e
    finally:
        if connection:
            connection.close()

def close_connection(connection):
    """
    Close the database connection.
    
    NOTE: This function is obsolete. Use get_db_connection() context manager instead.
    """
    if connection:
        connection.close()

# - - - - - - - - CRUD OPERATIONS  - - - - - - - - - #

def create_tasks(title, description, due_date=None):
    """
    Create a new task in the database.
    
    Args:
        title (str): Task title
        description (str): Task description
        due_date (str, optional): Due date. Defaults to None.
        
    Returns:
        int: Created task ID
    """
    with get_db_connection() as conn:
        cursor = conn.cursor()
        query = "INSERT INTO tasks (title, description, due_date) VALUES(%s, %s, %s)"
        cursor.execute(query, (title, description, due_date))
        conn.commit()
        task_id = cursor.lastrowid
        cursor.close()
        return task_id

def get_all_tasks():
    """
    Get all tasks from the database.
    
    Returns:
        list[dict]: List of all tasks
    """
    with get_db_connection() as conn:
        cursor = conn.cursor()
        query = "SELECT * FROM tasks ORDER BY create_at DESC"
        cursor.execute(query)
        results = cursor.fetchall()
        cursor.close()
        return results

def get_task_by_id(task_id):
    """
    Get a task by its ID.
    
    Args:
        task_id (int): Task ID

    Returns:
        dict or None: Task data if found, None otherwise.
    """
    with get_db_connection() as conn:
        cursor = conn.cursor()
        query = "SELECT * FROM tasks WHERE id_tasks = %s"
        cursor.execute(query, (task_id,))
        result = cursor.fetchone()
        cursor.close()
        return result

def update_task(task_id, title, description, due_date):
    """
    Update an existing task.
    
    Args:
        task_id (int): Task ID
        title (str): New title
        description (str): New description
        due_date (str, optional): New due date. Defaults to None.

    Returns:
        bool: True if the task was updated, False if it doesn't exist.
    """
    with get_db_connection() as conn:
        cursor = conn.cursor()
        
        # Verify if the task exists
        cursor.execute("SELECT id_tasks FROM tasks WHERE id_tasks = %s", (task_id,))
        if not cursor.fetchone():
            cursor.close()
            return False
        
        # Update the task
        query = "UPDATE tasks SET title = %s, description = %s, due_date = %s WHERE id_tasks = %s"
        cursor.execute(query, (title, description, due_date, task_id))
        conn.commit()
        cursor.close()
        return True

def delete_task(task_id):
    """
    Delete a task by its ID.
    
    Args:
        task_id (int): Task ID

    Returns:
        bool: True if the task was deleted, False if it doesn't exist.
    """
    with get_db_connection() as conn:
        cursor = conn.cursor()
        
        # Verify if the task exists
        cursor.execute("SELECT id_tasks FROM tasks WHERE id_tasks = %s", (task_id,))
        if not cursor.fetchone():
            cursor.close()
            return False
        
        # Delete the task
        query = "DELETE FROM tasks WHERE id_tasks = %s"
        cursor.execute(query, (task_id,))
        conn.commit()
        cursor.close()
        return True

def mark_as_completed(task_id):
    """
    Mark a task as completed.
    
    Args:
        task_id (int): Task ID

    Returns:
        bool: True if the task was marked as completed, False if it doesn't exist.
    """
    with get_db_connection() as conn:
        cursor = conn.cursor()
        
        # Verify if the task exists before updating
        cursor.execute("SELECT id_tasks FROM tasks WHERE id_tasks = %s", (task_id,))
        if not cursor.fetchone():
            cursor.close()
            return False
        
        # Mark as completed
        query = "UPDATE tasks SET is_completed = 1 WHERE id_tasks = %s"
        cursor.execute(query, (task_id,))
        conn.commit()
        cursor.close()
        return True