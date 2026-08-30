from fastapi import FastAPI
from pydantic import BaseModel

# PYDANTIC MODELS
# Pydantic VALIDATES and COERCES input data so the final object matches the declared types.
#   >> Data Validation and Nested Schema

# CREATING SCHEMA
app = FastAPI()

class User(BaseModel):
    name:str
    age:int
    email:str



# FOR NESTED DATA

class Address(BaseModel):
    street : str
    city : str
    pincode : int

class User2(BaseModel):
    name : str
    age : int 
    address : Address

@app.post("/create-user")

def create_user(user:User2):
    return {
        "message" : "USer Created",
        "data" : user
    }
