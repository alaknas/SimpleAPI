from pydantic import BaseModel


class Task(BaseModel):
    Id: int
    Title: str
    Description: str
    Completed: bool


