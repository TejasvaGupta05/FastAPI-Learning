from fastapi import FastAPI,HTTPException
from pydantic import BaseModel

app = FastAPI()

# ENVIRONMENT VARIABLES(.env)

# The Origins URL from L22 or The Secret Keys from L19 should not be written in the main code
# Since it can be pushed into github or can be exposed easily thus we use .env variables

# Make a file .env in the same dir

import os
from dotenv import load_dotenv

load_dotenv() # ---> Loading .env file

SECRET_KEY = os.getenv("SECRET_KEY")
DB_URL = os.getenv("DB_URL")
origins = os.getenv("ORIGINS")


print(SECRET_KEY)
print(DB_URL)
print(origins)

# FOR BIGGER PROJECTS we use a Seperate file CONFIG.PY for all this config from env to python
# By making a Class 
