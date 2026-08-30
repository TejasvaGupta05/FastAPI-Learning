from fastapi import FastAPI,HTTPException
from pydantic import BaseModel

app = FastAPI()

# MIDDLEWARE
# A secure layer between client application and backend Servers handling tasks like authentication, routing, data transformation, and security.

#                     ┌─────────────────────────────────────┐
#                     │               SERVER                │
#                     │                                     │
#                     │  ┌──────────────┐   ┌────────────┐  │
#                     │  │              │   │            │  │
# CLIENT              │  │  MIDDLEWARE  │   │  HANDLER   │  │
#   │                 │  │              │   │  FUNCTION  │  │
#   │ REQUEST ────────┼─►│              │──►│            │  │
#   │                 │  │              │   │            │  │
#   │ RESPONSE ◄──────┼──│              │◄──│            │  │
#   │                 │  └──────────────┘   └────────────┘  │
#   │                 │                                     │
#   └─────────────────┴─────────────────────────────────────┘


# A basic example

from fastapi import Request

# @app.middleware("http")
# async def my_middleware(request:Request,call_next):
#     print(" REQUEST SENT TO SERVER")

#     response = await call_next(request)  # Request has been sent to backend

#     print("DATA RECEIEVED from server")
#     return response

# ANOTHER EXAMPLE 

import time 

@app.middleware("http")
async def log_middleware(request:Request, call_next):
    start_time=time.time()
    response=await call_next(request)
    process_time=time.time()-start_time
    print(f"Path:{request.url.path} | Time:{process_time}")

    return response

@app.get("/users")
def get_users():
    return{
        "name":"Tejasva Gupta",
        "age":20
    }