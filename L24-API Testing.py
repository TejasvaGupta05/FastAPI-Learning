from fastapi import FastAPI,HTTPException
from pydantic import BaseModel

app = FastAPI()


## API TESTING 
# w test_main.py
# install pytest , httpx2


# Make 2 API for testing
@app.get("/")
def home():
    return {"message":"HELLO BNW"}

@app.get("/add")
def add(a:int,b:int):
    return {"RESULT" : a+b}

# Make a file test_main.py and PASTE the following code && THEN run "pytest" on a different terminal

# from fastapi.testclient import TestClient
# from main import app  #<-------------------------Importing main.py app

# client = TestClient(app)

# def test_home():
#     response = client.get("/")
#     # Status code check
#     assert response.status_code == 200  ## <----------This checks that for the API domain.com/ (home route) status code is 200 or not 
#     # Response data check
#     assert response.json() == {"message" : "HELLO BNW"}  #<---------- Similarly this checks the output

# #Test Add API
# def test_add():
#     response = client.get("/add?a=5&b=3")

#     assert response.status_code == 200
#     assert response.json() == {"RESULT" : 8}