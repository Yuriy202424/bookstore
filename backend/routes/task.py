from sqlalchemy import select, and_
from main import app
from db import Session, Task
from schemas import (TaskData,
                       ReadTask
)

                                                            
@app.get("/default") 
def get_tasks(data: ReadTask): 
    with Session.begin() as session:
        tasks = session.scalars(select(Task).where(Task.author == data.email))
        tasks = [TaskData.model_validate(task) for task in tasks]
        return tasks


@app.post('/create')
def create_task(data: TaskData):
    with Session.begin() as session:
        task = Task(**data.model_dump())
        session.add(task)
        return task 
    

@app.get("/task/{task_id}")
def get_task(task_id, data: ReadTask):
    with Session.begin() as session:
        task = session.scalar(select(Task).where(and_(Task.id == task_id, Task.author == data.email)))
        if task:
                task = TaskData.model_validate(task)
                return task
        else:
             return "Error"