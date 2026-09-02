from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_home():
    response = client.get("/")
    # Status code check
    assert response.status_code == 200  ## <----------This checks that for the API domain.com/ (home route) status code is 200 or not 
    # Response data check
    assert response.json() == {"message" : "HELLO BNW"}  #<---------- Similarly this checks the output

#Test Add API
def test_add():
    response = client.get("/add?a=5&b=3")

    assert response.status_code == 200
    assert response.json() == {"RESULT" : 8}