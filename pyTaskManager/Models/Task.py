from pydantic import BaseModel


class Task(BaseModel):
    Id: int = None
    Title: str
    Description: str
    Completed: bool = False


