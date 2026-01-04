import pymysql


def get_connection():
    conn = pymysql.connect(
        host='localhost',
    port= 3306,
    user= 'root',
    passwd= 'admin',
    db= 'all_tasks_testing_practice'
    )
    return conn
def close_connection(connection):
    connection.close()

# - - - - - - - - FUNCTIONS  - - - - - - - - - #

def create_tasks(title, description, due_date=None):
    conn = get_connection()
    cursor = conn.cursor()

    query = "INSERT INTO tasks (title, description, due_date) VALUES(%s, %s, %s)"
    cursor.execute(query, (title, description, due_date))

    conn.commit()
    cursor.close()  # ← Close the cursor.
    close_connection(conn)  # ← Close the conection.

# Function Get All Tasks

def get_all_tasks():
    conn = get_connection()
    cursor = conn.cursor()

    query = "SELECT * FROM tasks"
    cursor.execute(query)

    results = cursor.fetchall() # Get all results.
    cursor.close()
    close_connection(conn)

    return results # <- Important, return the data.

# Function get task by id.

def get_task_by_id(task_id):
    conn = get_connection()
    cursor = conn.cursor()

    query = "SELECT * FROM tasks WHERE id_tasks = %s"
    cursor.execute(query, (task_id,))  # ← The comma, must be a tuple.
    result = cursor.fetchone()  # ← fetchone() no fetchall(), with fetchone get only 1.

    cursor.close()
    close_connection(conn)

    return result

# Function update task.

def update_task(task_id, title, description, due_date):
    conn = get_connection()
    cursor = conn.cursor()

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
    conn = get_connection()
    cursor = conn.cursor()

    query = "DELETE FROM tasks WHERE id_tasks = %s"
    cursor.execute(query, (task_id,))

    conn.commit()
    cursor.close()
    close_connection(conn)

# Function mark as completed.

def mark_as_completed(task_id):
    conn = get_connection()
    cursor = conn.cursor()

    query = "UPDATE tasks SET is_completed = 1 WHERE id_tasks = %s"
    cursor.execute(query, (task_id,))

    conn.commit()
    cursor.close()
    close_connection(conn)