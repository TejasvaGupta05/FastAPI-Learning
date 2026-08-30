from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional

## CRUD OPERATIONS {CREATE , READ , UPDATE , DELETE}

app = FastAPI()

todo = []

class TODO(BaseModel):
    id:int
    title:str
    completed :bool

# CREATE API OPERATION

@app.post("/todos")

def create_todo(TD:TODO):
    todo.append(TD)
    return {
        "message" : "TODO added",
        "data" : TD
    }

# READ API OPERATION

@app.get("/todos") 

def read_all(completed: Optional[bool] = None):   # OPTIONAL allows you to use the same address domain.com/todos for CONDITIONAL and NON CONDITIONAL thus \todos will print all and \todos?completed=false will print with condition applied
    if completed is None:
        return todo
    return [td for td in todo if td.completed == completed]

@app.get("/todos/{id}")

def read_todo(id:int):
    for td in todo:
        if td.id == id:
            return td
    return {
        "ERROR" : "NOT FOUND"
    }

# UPDATE API OPERATIONS

@app.put("/todos/{todo_id}")
def update_todo(todo_id:int, updated_todo:TODO):
    for index,td in enumerate(todo):
        if td.id==todo_id:
            todo[index] = updated_todo
            return {"message" : "UPDATED", "todo ID" : todo_id, "Data" : updated_todo}
    return {"message" : "NO TODO ID FOUND"}

# There is also an operation known as PATCH 
# PUT replaces the whole object
# PATCH updates partial data of the object

#DELETE API OPERATIONS

@app.delete("/todos/{todo_id}")
def delete_todo(todo_id:int):
    for index,td in enumerate(todo):
        if td.id==todo_id:
            todo.pop(index)
            return {"message" : "DELETED"}
    return {"message" : "not found"}