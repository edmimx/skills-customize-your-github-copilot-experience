from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="Task API")

items = [
    {"id": 1, "name": "Write code", "done": False},
    {"id": 2, "name": "Study for quiz", "done": True},
]


class Item(BaseModel):
    name: str
    done: bool = False


@app.get("/")
def read_root():
    return {"message": "Welcome to the Task API"}


# TODO: Add a GET /items endpoint
# TODO: Add a POST /items endpoint
# TODO: Add a GET /items/{item_id} endpoint
# TODO: Add validation and not-found handling
