"""
Custom exception for TODO API.
"""

class DataBaseConnectionError(Exception):
    """
    Exception raised when there is an error connecting to the database.
    """
    pass

class TaskNotFoundError(Exception):
    """
    Exception raised when a task is not found.
    """
    pass

class InvalidTaskDataError(Exception):
    """
    Exception raised when the task data is invalid.
    """
    pass