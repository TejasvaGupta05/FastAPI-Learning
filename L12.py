from fastapi import FastAPI,HTTPException
from pydantic import BaseModel

app = FastAPI()

# DEPENDENCY INJECTION
# The same logic we try to reuse at different location(one logic is reused)
# Dependency injection in FastAPI allows you to declare and reuse components like database connections, authentication, or validation logic, which FastAPI automatically provides to your routes, enhancing modularity, testability, and maintainability.

from fastapi import Depends

# lets define a commmon logic we will reuse

def common_logic():
    return{
        "message":"Common Logic Executed"
    }

@app.get("/home")
def get_api(data = Depends(common_logic)):
    return data  #------> returns the "message" : "Common Logic Executed"

# NOW WHAT IS THE REAL USE OF IT 

from fastapi import Header,HTTPException

def verify_token(token: str = Header(None)):
    if token != "mysecrettoken":
        raise HTTPException(
            status_code=401,
            detail="Unauthorized"
        )
    return {
        "user":"Authorized User"
    }

@app.get("/secure-data")
def secure_data(user = Depends(verify_token)):
    return {
        "message":"Secure data accessed",
        "user":user
    }
