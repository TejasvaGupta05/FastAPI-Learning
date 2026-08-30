from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# RESPONSE MODELS
# Learn how to implement what data to show to users and what data to hide from the users
# How to hide Sensitive data etc.

class User(BaseModel):
    name : str
    age : int
    password : str

class UserResponse(BaseModel):
    name: str
    age: int

@app.get("/users", response_model=UserResponse) # Only respond through the User Model Data structures, Other field will be removed while responding
def Get_all_users():
    return {
        "name" : "Tejasva Gupta",
        "age" : 20,
        "password" : "123456" # This field will be removed
    }
