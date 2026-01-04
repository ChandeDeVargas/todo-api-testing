from pydantic import BaseModel
from typing import Optional
from datetime import date

class TaskCreate(BaseModel):
    title: str
    description: str
    due_date: Optional[date] = None

class TaskUpdate(BaseModel):
    title: str
    description: str
    due_date: Optional[date] = None