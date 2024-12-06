from fastapi import FastAPI, HTTPException
from typing import List
from Models.Task import Task
from Models.TaskSummary import TaskSummary


app = FastAPI()

tasks = []

@app.post("/Task", response_model=Task)
def create_task(task: Task):
    task.Id = len(tasks) + 1
    tasks.append(task)
    return task

@app.get("/Task", response_model=List[Task])
def get_all_tasks():
    return tasks

@app.get("/Task/summary")
def get_summary():
    task_count = len(tasks)
    completed_count = len([task for task in tasks if task.Completed])
    summary = TaskSummary(
        TotalTasks=task_count,
        CompletedTasks=completed_count,
        PendingTasks=task_count - completed_count
    )    
    return summary

@app.get("/Task/pending")
def get_pending_tasks():
    pending_tasks = [task for task in tasks if not task.Completed]
    return pending_tasks

@app.get("/Task/{id}", response_model=Task)
def get_task_by_id(id: int):
    for task in tasks:
        if task.Id == id:
            return task
    raise HTTPException(status_code=404, detail="Task not found")

@app.put("/Task/{id}", response_model=Task)
def update_task(id: int, updated_task: Task):
    for task in tasks:
        if task.Id == id:
            task.Title = updated_task.Title
            task.Description = updated_task.Description
            task.Completed = updated_task.Completed
            return task
    raise HTTPException(status_code=404, detail="Task not found")

@app.delete("/Task/{id}")
def delete_task(id: int):
    for task in tasks:
        if task.Id == id:
            tasks.remove(task)
            return {"detail": "Task deleted"}
    raise HTTPException(status_code=404, detail="Task not found")