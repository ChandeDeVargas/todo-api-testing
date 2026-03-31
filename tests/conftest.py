import pytest
import os
from app.database import get_connection, close_connection

@pytest.fixture(scope="session", autouse=True)
def setup_test_environment():
    """Set up testing environment"""
    os.environ['TESTING'] = 'true'
    
    # Ensure table exists and clean database before tests
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS tasks (
            id_tasks INT PRIMARY KEY AUTO_INCREMENT,
            title VARCHAR(100) NOT NULL,
            description VARCHAR(500) NOT NULL,
            create_at DATETIME DEFAULT CURRENT_TIMESTAMP,
            due_date DATETIME NULL,
            is_completed TINYINT(1) DEFAULT 0
        )
    """)
    cursor.execute("TRUNCATE TABLE tasks")
    conn.commit()
    cursor.close()
    close_connection(conn)
    
    yield