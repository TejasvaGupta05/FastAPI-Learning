from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# STATUS CODE (HTTP) & RESPONSES

# Some famous status codes are :
# 200 OK 
# 201 API Created 
# 202 API Accepted
# 400 Bad Request 
# 401 Unauthorized 
# 403 Forbidden 
# 404 Not Found 
# 500 Server Error 

from fastapi import status  # Firstly import ststus from fastapi 

# Now youu can use your custom ststus codes like below
@app.post("/create_users", status_code=status.HTTP_201_CREATED)


def create_users():
    return {
        "message" : "USER CREATED",
        "data" : {
            "name" : "Tejasva Gupta",
            "age" : 20
        }
    }

@app.get("/users")
def get_users():
    return {
        "status":"Success",
        "message":"User fetched",
        "data" : {
            "name" : "Tejasva Gupta",
            "age" : 20
        }
    }

from fastapi import HTTPException

@app.get("/users/{user_id}")
def get_users(user_id:int):
    if user_id != 1:
        raise HTTPException(
            status_code=404,
            detail="User Not Found"
        )

    return {
        "id":1,
        "name":"Mohit"
    }