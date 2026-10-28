
from fastapi import FastAPI, Depends, HTTPException
from models import Task
from dbConfig import session, engine
import databaseModel
from sqlalchemy.orm import Session

app = FastAPI()

databaseModel.Base.metadata.create_all(bind=engine)


def get_db():
    db = session()
    try:
        yield db
    finally:
        db.close()


@app.get("/tasks")
def getAllTasks(db: Session = Depends(get_db)):
    return db.query(databaseModel.Task).all()


@app.get("/tasks/{taskId}")
def getTaskById(
    taskId: int,
    db: Session = Depends(get_db)
):
    task = db.query(databaseModel.Task).filter(
        databaseModel.Task.taskId == taskId
    ).first()

    if task is None:
        raise HTTPException(
            status_code=404,
            detail="Task not found"
        )

    return task


@app.post("/task")
def addTask(
    task: Task,
    db: Session = Depends(get_db)
):
    existing_task = db.query(databaseModel.Task).filter(
        (databaseModel.Task.taskId == task.taskId) |
        (databaseModel.Task.taskName == task.taskName)
    ).first()

    if existing_task:
        raise HTTPException(
            status_code=409,
            detail="Task ID or task name already exists"
        )

    db_task = databaseModel.Task(**task.model_dump())

    db.add(db_task)
    db.commit()
    db.refresh(db_task)

    return db_task


@app.put("/task/{taskId}")
def updateTask(
    taskId: int,
    task: Task,
    db: Session = Depends(get_db)
):
    db_task = db.query(databaseModel.Task).filter(
        databaseModel.Task.taskId == taskId
    ).first()

    if db_task is None:
        raise HTTPException(
            status_code=404,
            detail="Task not found"
        )

    db_task.taskName = task.taskName
    db_task.taskDescription = task.taskDescription

    db.commit()
    db.refresh(db_task)

    return db_task


@app.delete("/task/{taskId}")
def deleteTask(
    taskId: int,
    db: Session = Depends(get_db)
):
    db_task = db.query(databaseModel.Task).filter(
        databaseModel.Task.taskId == taskId
    ).first()

    if db_task is None:
        raise HTTPException(
            status_code=404,
            detail="Task not found"
        )

    db.delete(db_task)
    db.commit()

    return "Task deleted successfully"