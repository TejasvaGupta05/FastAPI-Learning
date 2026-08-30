from fastapi import FastAPI
app = FastAPI()

# Path Parameters = variables embedded directly in a URL path that identify specific resources in a RESTful API.

@app.get("/users/{user_id}")  # HERE user_id will be fetched from the URL => www.domain.com/users/123 => 123 will be fetched as a user id


def get_user(user_id:int): # Type validation is optional 
    return {"user_id": user_id}  # NOW the user_id will be according to the URL