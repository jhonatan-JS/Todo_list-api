from sqlalchemy.orm import Session
from ..models.task import Task
from ..schemas.task import TaskCreate

def get_tasks(db: Session, user_id: int, search: str = None):
    query = db.query(Task).filter(Task.user_id == user_id)
    if search:
        query = query.filter(Task.description.ilike(f"%{search}%"))
    return query.order_by(Task.created_at.desc()).all()

def create_task(db: Session, task: TaskCreate, user_id: int):
    db_task = Task(**task.dict(), user_id=user_id)
    db.add(db_task)
    db.commit()
    db.refresh(db_task)
    return db_task