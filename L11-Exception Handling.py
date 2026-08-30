from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# EXCEPTION HANDLING 
# The handling done on status code exceptions 

# Exception handling allows programs to manage errors gracefully

from fastapi import HTTPException

# Raising Predefault Exception

@app.get("/users/{user_id}")
def get_user(user_id:int):
    if user_id != 1:
        raise HTTPException(
            status_code=404,
            detail = "User NOt Found"
        )
    return {
        "id":1,
        "name":"NIBUIED"
    }

# CREATING CUSTOM EXCEPTION

class UserNOTfoundException(Exception):
    def __init__(self, name:str):
        self.name=name 

@app.get("/user/{user_name}")
def get_userbyname(user_name:str):
    if user_name != "tejas":
        raise UserNOTfoundException(user_name)
    return {
        "name" : "tejas",
        "age" : 20
    }


# Raising Global level Exception
from fastapi import Request
from fastapi.responses import JSONResponse

@app.exception_handler(UserNOTfoundException)
def user_not_found_handler(req:Request, exc:UserNOTfoundException):
    return JSONResponse(
        status_code=404,
        content={
            "status":"ERROR",
            "message" : f"User {exc.name} Not found"
        }
    )