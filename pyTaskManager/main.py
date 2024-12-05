
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

app = FastAPI()

class Task(BaseModel):
    id: int
    title: str
    description: str
    completed: bool

tasks = []

@app.post("/Task", response_model=Task)
def create_task(task: Task):
    task.id = len(tasks) + 1
    tasks.append(task)
    return task

@app.get("/Task", response_model=List[Task])
def get_all_tasks():
    return tasks

@app.get("/Task/{id}", response_model=Task)
def get_task_by_id(id: int):
    for task in tasks:
        if task.id == id:
            return task
    raise HTTPException(status_code=404, detail="Task not found")

@app.put("/Task/{id}", response_model=Task)
def update_task(id: int, updated_task: Task):
    for task in tasks:
        if task.id == id:
            task.title = updated_task.title
            task.description = updated_task.description
            task.completed = updated_task.completed
            return task
    raise HTTPException(status_code=404, detail="Task not found")

@app.delete("/Task/{id}")
def delete_task(id: int):
    for task in tasks:
        if task.id == id:
            tasks.remove(task)
            return {"detail": "Task deleted"}
    raise HTTPException(status_code=404, detail="Task not found")