from sqlalchemy.orm import declarative_base
from sqlalchemy import Column,Integer,String,Float
Base= declarative_base()
class Task(Base):
    __tablename__ = "task"
    taskId= Column(Integer,primary_key=True,index=True)
    taskName= Column(String)
    taskDescription= Column(String)
