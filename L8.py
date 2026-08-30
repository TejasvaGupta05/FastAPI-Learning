from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# PATH PARAMS + QUERY PARAMS + BODY 
# e.g. PUT on /users/101?notify=false

users = []

class USER(BaseModel):
    name : str
    age  : int

@app.post("/user")
def create_user(data:USER):
    users.append(data)
    return {
        "message" : "USER CREATED",
        "data" : data 
    }

@app.put("/user/{user_id}")
def update_user(user_id:int, data:USER, notify : bool = False ):
    if user_id<len(users):
        users[user_id]=data
        return {"message":"Updated", "Data":data}
    return {"error": "USER NOT FOUND"}
