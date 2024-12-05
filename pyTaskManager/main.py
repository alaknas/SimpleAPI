from fastapi import FastAPI, HTTPException
from typing import List
from Models.Task import Task

app = FastAPI()

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

@app.get("/Task/summary")
def get_summary():
    task_count = len(tasks)
    completed_count = len([task for task in tasks if task.completed])
    summary = (task_count, completed_count, task_count - completed_count)
    return {"summary": summary}

@app.get("/Task/pending")
def get_pending_tasks():
    pending_tasks = [task for task in tasks if not task.completed]
    return pending_tasks