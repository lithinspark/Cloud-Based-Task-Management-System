from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from .. import models, schemas
from ..dependencies import get_db, get_current_user
from typing import Optional

router = APIRouter(prefix="/tasks", tags=["Tasks"])

@router.post("/")
def create_task(task: schemas.TaskCreate,
                db: Session = Depends(get_db),
                user=Depends(get_current_user)):
    db_task = models.Task(**task.dict(), owner_id=user.id)
    db.add(db_task)
    db.commit()
    db.refresh(db_task)
    return db_task

@router.get("/")
def get_tasks(page: int = 1,
              limit: int = 10,
              status: Optional[str] = None,
              search: Optional[str] = None,
              db: Session = Depends(get_db),
              user=Depends(get_current_user)):

    query = db.query(models.Task)

    if user.role != "admin":
        query = query.filter(models.Task.owner_id == user.id)

    if status:
        query = query.filter(models.Task.status == status)

    if search:
        query = query.filter(models.Task.title.ilike(f"%{search}%"))

    tasks = query.offset((page - 1) * limit).limit(limit).all()
    return tasks
