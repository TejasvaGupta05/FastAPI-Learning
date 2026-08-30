"""
CREATE BASIC ROUTE
GET REQUEST
RUN SERVER(UVICORN)
SWAGGER UI INTRO
"""

from fastapi import FastAPI

app = FastAPI()

# PATH IN THE DATABASE DOCUMENT IS A ROUTE
# CREATING HOME ROUTE
@app.get("/")

def home():
    return {"HELLO" : "MESSAGE"}

#MULTIPLE ROUTES
@app.get("/about")

def about():
    return {"About" : "BTECH CSE STUDDENT"}

@app.get("/college")

def college():
    return {"College" : ["Madhav INstituw gemnwm","IET DAVV","SHTJRPO"]}