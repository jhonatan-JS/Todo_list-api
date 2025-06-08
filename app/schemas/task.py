from pydantic import BaseModel
from datetime import datetime

class TaskBase(BaseModel):
    description: str

class TaskCreate(TaskBase):
    pass

class TaskOut(TaskBase):
    id: int
    created_at: datetime
    user_id: int
    completed: bool

    class Config:
        from_attributes = True