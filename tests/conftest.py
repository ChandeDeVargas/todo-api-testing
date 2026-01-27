import pytest
import os
from app.database import get_connection, close_connection

@pytest.fixture(scope="session", autouse=True)
def setup_test_environment():
    """Set up testing environment"""
    os.environ['TESTING'] = 'true'
    
    # Clean database before tests
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("TRUNCATE TABLE tasks")
    conn.commit()
    cursor.close()
    close_connection(conn)
    
    yield