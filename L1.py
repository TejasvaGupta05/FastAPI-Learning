from fastapi import FastAPI

app = FastAPI()  # MADE A OBJECT of the CLASS

@app.get("/")  # MAKING GET API WHOSE PATH IS SET TO "\"{home dir}

def home(): # Making a Home function
    return {"message" : "HELLO FROM A B C"}