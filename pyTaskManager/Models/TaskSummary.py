from pydantic import BaseModel


class TaskSummary(BaseModel):
    TotalTasks: int
    CompletedTasks: int
    PendingTasks: int


