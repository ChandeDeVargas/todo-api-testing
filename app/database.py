import pymysql
from .exceptions import DataBaseConnectionError

def get_connection():
    """
    Establish connection to MySQL database

    Returns:
            pymsql.Connection: Active database connection
    """
    try:
        conn = pymysql.connect(
            host='localhost',
            port= 3306,
            user= 'root',
            passwd= 'admin',
            db= 'all_tasks_testing_practice'
        )
        return conn
    except pymysql.MySQLError as e:
        raise DataBaseConnectionError(f"Error connecting to the database: {str(e)}")
def close_connection(connection):
    """
    Close the database connection
    """
    if connection:
        connection.close()

# - - - - - - - - CRUD OPERATIONS  - - - - - - - - - #

def create_tasks(title, description, due_date=None):
    """
    Create a new task in the database

    Args:
            title (str): Task title
            description (str): Task description
            due_date (str, optional): Task due date. Defaults to None.
    """
    conn = get_connection()
    cursor = conn.cursor()

    query = "INSERT INTO tasks (title, description, due_date) VALUES(%s, %s, %s)"
    cursor.execute(query, (title, description, due_date))

    conn.commit()
    cursor.close()
    close_connection(conn)

# Function Get All Tasks

def get_all_tasks():
    """
    Get all tasks from the database

    Returns:
            Tuple: All tasks records
    """
    conn = get_connection()
    cursor = conn.cursor()

    query = "SELECT * FROM tasks"
    cursor.execute(query)

    results = cursor.fetchall()
    cursor.close()
    close_connection(conn)

    return results

# Function get task by id.

def get_task_by_id(task_id):
    """
    Get a single task by ID

    Args:
            task_id (int): Task ID

    Returns:
            Tuple or None: Task data if found, None otherwise.
    """
    conn = get_connection()
    cursor = conn.cursor()

    query = "SELECT * FROM tasks WHERE id_tasks = %s"
    cursor.execute(query, (task_id,))
    result = cursor.fetchone()

    cursor.close()
    close_connection(conn)

    return result

# Function update task.

def update_task(task_id, title, description, due_date):
    """
    Update an existing task.

    Args:
            task_id (int): Task ID
            title (str): New title
            description (str): New description
            due_date (str, optional): New due date. Defaults to None.

    Returns:
            bool: True if the task was updated, False otherwise.
    """
    conn = get_connection()
    cursor = conn.cursor()

    # Check if the task exists.
    cursor.execute(
        "SELECT id_tasks FROM tasks WHERE id_tasks = %s ",
        (task_id,)
    )
    task = cursor.fetchone()

    if not task:
        cursor.close()
        close_connection(conn)
        return False

    query = "UPDATE tasks SET title = %s, description = %s, due_date = %s WHERE id_tasks = %s"
    cursor.execute(query, (title, description, due_date, task_id))

    conn.commit()
    cursor.close()
    return True

# Function delete task by id.

def delete_task(task_id):
    """
    Delete a task by ID.

    Args:
            task_id (int): Task ID

    Returns:
            bool: True if the task was deleted, False otherwise.
    """
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT id_tasks FROM tasks WHERE id_tasks = %s", (task_id,))
    task = cursor.fetchone()

    if not task:
        cursor.close()
        close_connection(conn)
        return False

    query = "DELETE FROM tasks WHERE id_tasks = %s"
    cursor.execute(query, (task_id,))

    conn.commit()
    cursor.close()
    close_connection(conn)

    return True

# Function mark as completed.

def mark_as_completed(task_id):
    """
    Mark a task as completed.

    Args:
            task_id (int): Task ID

    Returns:
            bool: True if the task was marked as completed, False otherwise.
    """
    conn = get_connection()
    cursor = conn.cursor()

    query = "UPDATE tasks SET is_completed = 1 WHERE id_tasks = %s"
    cursor.execute(query, (task_id,))

    conn.commit()
    cursor.close()
    close_connection(conn)