from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import Optional
from ..database import get_db
from ..schemas.task import TaskCreate, TaskOut
from ..crud.task import get_tasks, create_task
from ..utils.security import get_current_user
from typing import List

router = APIRouter(prefix="/tasks", tags=["Tasks"])

@router.get("/", response_model=List[TaskOut])
def read_tasks(
    search: Optional[str] = None,
    db: Session = Depends(get_db),
    current_user: int = Depends(get_current_user)
):
    return get_tasks(db, user_id=current_user.id, search=search)

@router.post("/", response_model=TaskOut, status_code=201)
def create_task(
    task: TaskCreate,
    db: Session = Depends(get_db),
    current_user: int = Depends(get_current_user)
):
    return create_task(db, task=task, user_id=current_user.id)