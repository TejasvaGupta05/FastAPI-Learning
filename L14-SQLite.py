
###  DATABASE INTEGRATION {SQLite}

# NOW INSTEAD OF STORING DATA INTO LIST WE WILL STORE IT IN DATABASE

# What is SQLite ?? 
# SQLite is a highly efficient, serverless, and self-contained SQL database engine that stands out for its simplicity and ease of integration. 
# SQLite is a lightweight, serverless, self-contained, and highly reliable SQL database engine. It is widely used due to its simplicity, ease of setup and zero-configuration nature.

# Frontend
#    ↓ HTTP Request   
# Backend / API Server
#    ↓ SQL / ORM      
# SQLite Database      

from fastapi import FastAPI,HTTPException
from pydantic import BaseModel

app = FastAPI()

import sqlite3 

conn = sqlite3.connect("test.db",check_same_thread=False) 
                    #    ^^^           ^^^
                    #  directory      check if using the same thread(a small unit of execution inside a program. Each thread can perform work independently, while sharing the same program's memory.)

cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS todos(
        id INTEGER PRIMARY KEY,
        title TEXT,${mkde}
        completed BOOL
    )
""")

conn.commit()


#TO CHECK IF ABOVE OPERATIONS WORKED WELL 
@app.get("/")
def printall():
    return {
        "message":"CONNECTED SUCCESSFULLY"
    }