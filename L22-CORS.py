from fastapi import FastAPI,HTTPException
from pydantic import BaseModel

app = FastAPI()

# CORS + Connect React with Fast API

# What is CORS ??
# CORS(Cross-Origin Resource Sharing) is a security root offered by the browser 
# if ur backend and frontend are working on different ports CORS will block the coming frontend request from any unknown Port until backend specifically allows it.

from fastapi.middleware.cors import CORSMiddleware

# Allowing Frontend URL 
origins = [
    "http://127.0.0.1:5500",
    "http://localhost:5173"  # Or http://localhost:5173 or any other URL
]                            #  Generally it is written in an env file

app.add_middleware(
    CORSMiddleware,
    allow_origins = origins,
    allow_credentials = True,
    allow_headers = ["*"],
    allow_methods = ["*"] # GET POST PUT DELETE Etc
)

@app.get("/")
def check_conn():
    return {
        "message" : "BACKEND CONNECTED TO FRONTEND"
    }