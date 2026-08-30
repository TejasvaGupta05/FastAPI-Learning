### COPYING SAME FROM L16

from fastapi import FastAPI,HTTPException,Depends
from pydantic import BaseModel
from sqlalchemy import create_engine,Column,Integer,String,Boolean
from sqlalchemy.orm import sessionmaker,declarative_base,Session
app = FastAPI()

DATABASE_URL = "sqlite:///./test.db"

engine = create_engine(
    DATABASE_URL,
    connect_args={"check_same_thread" : False}
)

sessionlocal = sessionmaker(bind=engine)

Base = declarative_base()

class Todo(Base):
    __tablename__ = "todos"

    id = Column(Integer,primary_key=True,index=True)
    title = Column(String)
    completed = Column(Boolean)

Base.metadata.create_all(bind=engine)

def get_db():
    db = sessionlocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/post")
def create_todo(title:str, db:Session= Depends(get_db)):
    todo = Todo(title=title, completed=False)
    db.add(todo)
    db.commit()
    db.refresh(todo)  ## TO FETCH UPDATED DATA 
    return {
        "message" : "DATA ADDED",
        "data" : todo
    }

## READ OPERATIONS 

@app.get("/todos")
def get_todos(db: Session=Depends(get_db)):
    data = db.query(Todo).all()

    return {
        "Size" : len(data),
        "DATA" : data
    }

@app.get("/todo/{todo_id}")
def get_todo(todo_id:int, db : Session=Depends(get_db)):
    data = db.query(Todo).filter(Todo.id==todo_id).first()

    if not data:
        raise HTTPException(status_code=404,detail="Todo NOT FOUND")

    return data


## UPDATE OPERATIONS

@app.put("/todos/{todo_id}")
def update_todo(todo_id:int,title:str, db :Session=Depends(get_db)):
    data = db.query(Todo).filter(Todo.id==todo_id).first()

    if not data:
        raise HTTPException(status_code=404,detail="NOT FOUND")

    data.title = title

    db.commit()
    return{
        "message" : "TITLE UPDATED",
        "data" : data
    }

@app.delete("/todos/{todo_id}")
def delete_todo(todo_id:int,db:Session=Depends(get_db)):
    data = db.query(Todo).get({"id":todo_id})

    if not data:
        raise HTTPException(status_code=404,detail="NOT DOFUN")

    db.delete(data)
    db.commit()

    return {
        "message":"DELETED",
        "data":data
    }