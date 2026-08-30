from fastapi import FastAPI,HTTPException,Request
from pydantic import BaseModel

app = FastAPI()

# FILE UPLOAD & STATIC FILES

from fastapi import UploadFile,File
from fastapi.staticfiles import StaticFiles
import os 
import shutil

# Step-1 : Ensure Upload folder exist

UPLOAD_DIR = "uploads"

if not os.path.exists(UPLOAD_DIR):
    os.makedirs(UPLOAD_DIR)

# Step-2 : Setting up Static file setup
# In this we are making public path for the static file

app.mount("/files",StaticFiles(directory=UPLOAD_DIR),name="files")

# This will create a URL like ----> http://127.0.0.1:8080/files/<Filename>

# Step -3 :Upload file API
@app.post("/upload")
def upload_file(file:UploadFile=File(...), request: Request = None):
    filename = file.filename
    file_path = os.path.join(UPLOAD_DIR,filename)

    if not filename : 
        raise HTTPException(400,"FILE NOT SELECTED")

    with open(file_path,"wb") as buffer:
        shutil.copyfileobj(file.file,buffer)

    base_url = str(request.base_url)
    return{
        "message" : "File Uploaded Successfully",
        "filename" : filename,
        "file_url" : f"{base_url}files/{filename}"
    }

# Step-4 : Get File URL API

@app.get("/files/{filename}")
def get_file(filename:str, request: Request):
    file_path = os.path.join(UPLOAD_DIR,filename)
    if not os.path.exists(file_path):
        raise HTTPException(404,"FILE NOT FOUND")
    return{
        "file_url" : f"{str(request.base_url)}files/{filename}"
    }

@app.get("/")
def check():
    return{
        "message" : "File UPLOADING API RUNNING"
    }