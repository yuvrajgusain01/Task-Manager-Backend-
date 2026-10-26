from pydantic import BaseModel

class Task(BaseModel):
    taskId: int
    taskName: str
    taskDescription: str

