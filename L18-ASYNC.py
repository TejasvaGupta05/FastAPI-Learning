
# ASYNCRONOUS PROGRAMMING : Handling Multiple REQUESTS at the same time
# Asynchronous programming is a non-blocking execution model where tasks can run independently and potentially concurrently, without waiting for other tasks to finish before starting.

import time
import asyncio

# SYNCHRONOUS : 
# def task():
#     time.sleep(3)
#     return "Done"

# ASYNCHRONOUS :
# async def task2():
#     await asyncio.sleep(3)
#     return "DONE"

# This is how a ASYNC func look
# Now use it in fastapi 

from fastapi import FastAPI,HTTPException
from pydantic import BaseModel

app = FastAPI()

@app.get("/")
async def home():
    await asyncio.sleep(3)
    return {
        "message" : "Async API"
    }

# +----------------+------------------------------+-------------------------------+
# | Aspect         | Sync API                     | Async API                     |
# +----------------+------------------------------+-------------------------------+
# | Execution      | Waits for response before    | Continues other work while    |
# |                | continuing                   | waiting                       |
# +----------------+------------------------------+-------------------------------+
# | Simplicity     | Easier to understand/debug   | More complex                  |
# +----------------+------------------------------+-------------------------------+
# | Performance    | Good for sequential tasks    | Better for concurrent I/O     |
# +----------------+------------------------------+-------------------------------+
# | Resource usage | Threads may wait for I/O     | Uses resources more           |
# |                |                              | efficiently                   |
# +----------------+------------------------------+-------------------------------+
# | Best for       | Scripts, CRUD, simple apps   | High-traffic, real-time apps  |
# +----------------+------------------------------+-------------------------------+
# | Error handling | Straightforward              | Requires async error handling|
# +----------------+------------------------------+-------------------------------+
