from fastapi import FastAPI
from models import Task

app=FastAPI()

tasks=[]

@app.get("/tasks")
def getAllTasks():
    return tasks


@app.get("/tasks/{taskId}")
def getTaskById(taskId:int):
    for task in tasks:
        if task.taskId == taskId:
            return task

    return "Task not found"


@app.post("/task")
def addTask(task:Task):
    for i in range (len(tasks)):
        if tasks[i].taskId ==task.taskId or tasks[i].taskName ==task.taskName:
            return "Task already added"
    tasks.append(task)
    return task


@app.put("/task")
def updateTask(Id:int,task:Task):
    for i in range (len(tasks)):
        if tasks[i].taskId== Id:
            tasks[i]=task

            return "Task updated successfully"

    return "Task not found"


@app.delete("/task")
def deleteTask(taskId:int):
    for i in range(len(tasks)):
        if(tasks[i].taskId ==taskId):
            del tasks[i]

            return "Task deleted successfully"

    return "Task not found"


