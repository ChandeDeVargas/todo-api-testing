from pydantic import BaseModel
from datetime import datetime
from typing import Optional


class TaskCreate(BaseModel):
    title: str
    description: str
    due_date: Optional[datetime] = None


class TaskUpdate(BaseModel):
    title: str
    description: str
    due_date: Optional[datetime] = None