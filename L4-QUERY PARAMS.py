from fastapi import FastAPI

app=FastAPI()

# QUERY PARAMETERS = key-value pairs appended to a URL that modify or filter the response from a server.
# Example :
#    www.domain.com/users?name=mohit
#    www.domain.com/products?price=1000

@app.get("/users")

def get_users(name : str=None):
    return {"Name":name}   # Automatically fetch mohit from => www.domain.com/users?name=mohit => NULL otherwise



# FOR MULTIPLE QUERY PARAMS

@app.get("/items")

# URL will look like this for the following => domain.com/items?name=abc&price=300
def get_items(name:str=None , price:int=10):
    return {
        "Name" : name,
        "Price" : price
    }