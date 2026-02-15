from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from .. import models, schemas
from ..dependencies import get_current_user, get_db

router = APIRouter(prefix="/tasks", tags=["Tasks"])

@router.post("/")
def create_task(task: schemas.TaskCreate,
                db: Session = Depends(get_db),
                user=Depends(get_current_user)):
    new_task = models.Task(
        title=task.title,
        description=task.description,
        owner_id=user.id
    )
    db.add(new_task)
    db.commit()
    return new_task

@router.get("/")
def get_tasks(db: Session = Depends(get_db),
              user=Depends(get_current_user)):
    return db.query(models.Task).filter(models.Task.owner_id == user.id).all()

@router.put("/{task_id}")
def update_task(task_id: str,
                task: schemas.TaskUpdate,
                db: Session = Depends(get_db),
                user=Depends(get_current_user)):
    db_task = db.query(models.Task).filter(models.Task.id == task_id,
                                           models.Task.owner_id == user.id).first()
    if not db_task:
        raise HTTPException(404)

    if task.title:
        db_task.title = task.title
    if task.description:
        db_task.description = task.description

    db.commit()
    return db_task

@router.delete("/{task_id}")
def delete_task(task_id: str,
                db: Session = Depends(get_db),
                user=Depends(get_current_user)):
    db_task = db.query(models.Task).filter(models.Task.id == task_id,
                                           models.Task.owner_id == user.id).first()
    if not db_task:
        raise HTTPException(404)

    db.delete(db_task)
    db.commit()
    return {"message": "Deleted"}
