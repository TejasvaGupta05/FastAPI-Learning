
### AUTHENTICATION BASICS 

# JWT : JSON Web Token
# +--------+                  +---------+
# | Client |                  | Server  |
# +--------+                  +---------+
#     |                           |
#     |  POST /login              |
#     |  username + password      |
#     |-------------------------->|
#     |                           |
#     |       JWT Token           |
#     |<--------------------------|
#     |                           |
#     |  GET /profile             |
#     |  Authorization: Bearer JWT|
#     |-------------------------->|
#     |                           |
#     |       Verify JWT          |
#     |                           |
#     |       Response            |
#     |<--------------------------|


# JWT is assigned to a Client by a Server on first Login so that Client doesn't have to send Pass again and again for every request on the server
# All the next requests to the server after login is made through JWT token

# It consists of 3 Base64URL-encoded parts, separated by dots : HEADER.PAYLOAD.SIGNATURE

from fastapi import FastAPI,HTTPException,Depends,Header
from pydantic import BaseModel

# Importing JWT dependencies
from jose import jwt  # JOSE : JS Object Signature and Encryption
from datetime import datetime, timedelta, timezone

app = FastAPI()

SECRET_KEY = "mysecret"  #----> private key for encryption
ALGORITHM = "HS256"   #-----> Algorithm for encryption

def create_token(data: dict):
    to_encode = data.copy()     #--------> Data to be encoded
    expiration_time = datetime.now(timezone.utc) + timedelta(minutes=30)  #---->time after which token will expire
    to_encode.update({
        "exp":expiration_time
    })
    token = jwt.encode(to_encode,SECRET_KEY,algorithm=ALGORITHM)
    return token

# Login API(Token Generate)
@app.post("/login")
def login(username:str,password:str):
    if username != "admin" or password != "1234" :
        raise HTTPException(404,detail="Invalid U or Pass")
    token = create_token({
        "sub" : username,
        "pass": password
    })
    return {
        "access_token":token
    }


#Token Verification
def verify_token(token:str = Header(None)):
    try:
        payload = jwt.decode(token,SECRET_KEY,algorithms=[ALGORITHM])
        return payload
    except:
        raise HTTPException(401,"Wrong/Expired Token")

# Protected route
@app.get("/secure")
def secure_data(user = Depends(verify_token)):
    return{
        "message":"SECURE DATA ACCESSED",
        "user":user
    }