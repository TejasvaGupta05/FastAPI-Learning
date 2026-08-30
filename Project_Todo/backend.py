from fastapi import FastAPI,HTTPException
from pydantic import BaseModel

from fastapi.middleware.cors import CORSMiddleware # Since a request from an unknown URL/PORT is Automatically BLOCKED by the CORS(Cross Origins Resource Sharing). Thus we allow some URL Explicitly

app = FastAPI()

#Explicit Allowance
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://127.0.0.1:5500"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

todos = []

class TODOS(BaseModel) :
    id : int = None
    title : str = None
    isdone : bool = False

@app.get("/")
def connectionremark():
    return {"message":"CONNECTED"}

@app.get("/count")
def todoscount():
    return {"count" : len(todos)}

@app.post("/post")
def create_todo(title:str):
    todo = TODOS()
    todo.id = len(todos)+1
    todo.title=title
    todos.append(todo)
    return {
        "message" : "Successfully Added"
    }

@app.get("/todos")
def get_all():
    return todos

@app.get("/todos/{todo_id}")
def get_todo(todo_id:int):
    if todo_id>len(todos) or todo_id<1:
        raise HTTPException(404,"NOT FOUND")
    return {
        "message" : "TODO Found",
        "Todo" : todos[todo_id-1]
    }

@app.put("/mark/{todo_id}")
def mark_done(todo_id:int):
    if todo_id>len(todos) or todo_id<1:
        raise HTTPException(404,"NOT FOUND")
    todos[todo_id-1].isdone = True
    return {
        "message" : "Marked as Done",
        "Todo" : todos[todo_id-1]
    }

@app.delete("/delete/{todo_id}")
def delete_todo(todo_id:int):
    if todo_id>len(todos) or todo_id<1:
        raise HTTPException(404,"NOT FOUND")
    temp = todos.pop(todo_id-1)
    return {
        "message" : "Removed from List",
        "Todo" : temp
    }

