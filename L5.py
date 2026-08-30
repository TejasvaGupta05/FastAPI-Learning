from fastapi import FastAPI
app=FastAPI()

# REQUEST BODY : Part of an HTTP request that carries data from client -> server 
# It is used in methods like POST, PUT, PATCH, or DELETE.

# Example : a person while logging in a website sends EMAIL, PASSWORD as REQUEST BODY JSON to BACKEND

# POST REQUEST : To send data from CLIENT --> SERVER

@app.post("/create-user")

# 
# def create_user(name:str, email:str):
#     return {
#         "NAME" : name,
#         "EMAIL" : email
#     }
# 

# Now to provide data in form of DICTIONARY KEY VAL pair so that their is no change in URL as well u can send data accordingly

# def create_user(data:dict):
#     return {
#         "message" : "DATA UPLOADED",
#         "DATA" : data
#     }

# NOW DICT has an issue that it accepts every type of data fields 
# for example it will also accept 
# {"Page-NO":21} and we require details like EMAIL,NAME,PASS

# Thus to VALIDATE the DATA STRUCTURE we use PYDANTIC

from pydantic import BaseModel

class USER(BaseModel):
    name:str
    age:int

@app.post("/create_user")

def create_usr(user : USER):
    return {
        "Message" : "User Created",
        "User" : user
    }
