
### OAuth2 + JWT

# OAuth2 : it is something like we use "LOGIN WITH GOOGLE" instead of username and pass
# OAuth 2.0 is a way to let an app access another service on your behalf without giving the app your password.

from fastapi import FastAPI,HTTPException,Depends
from jose import jwt 
from fastapi.security import OAuth2PasswordBearer,OAuth2PasswordRequestForm
from datetime import datetime,timedelta,timezone
from passlib.context import CryptContext

app = FastAPI()

#JWT Config
SECRET_KEY = "mykey"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

# Password HAASHING
pwd_context = CryptContext(schemes=["bcrypt"],deprecated ="auto")

#OauthSetup
oauth2_schema = OAuth2PasswordBearer(tokenUrl="login")

#Dummy DB
fake_user_db = {
    "admin":{
        "username":"admin",
        "hashed_password":pwd_context.hash("1234")
    }
}

#Hash Password
def hash_password(password:str):
    return pwd_context.hash(password)

#Verify Password
def verify_password(plain_pass:str,h_pass:str):
    return pwd_context.verify(plain_pass,h_pass)

def create_token(data:dict):
    to_encode = data.copy()
    expire = datetime.now(timezone.utc) + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({
        "exp":expire
    })
    token = jwt.encode(to_encode,SECRET_KEY,algorithm=ALGORITHM)

    return token

# Login (OAuth2)
@app.post("/login")
def login(form_data:OAuth2PasswordRequestForm = Depends()):
    user = fake_user_db.get(form_data.username)
    if not user or not verify_password(form_data.password,user["hashed_password"]):
        raise HTTPException(
            status_code=400,
            detail="Invalid Username and Password"
        )
    access_token = create_token({"sub":user["username"]})

    return {
        "access_token":access_token,
        "token_type":"bearer"
    }

#Token Verification
def verify_token(token:str=Depends(oauth2_schema)):
    try:
        payload= jwt.decode(token,SECRET_KEY,algorithms=[ALGORITHM])
        username : str = payload.get("sub")
        if username is None:
            raise HTTPException(401,"Invalid Token")
        return username
    except jwt.JWTError:
        raise HTTPException(401,"Invalid Token")


#Protected Route
@app.get("/protected")
def protected_route(username:str = Depends(verify_token)):
    return {
        "message" : "Hello you have access to this protected route",
        "user" : username
    }