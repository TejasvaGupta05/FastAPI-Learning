from fastapi import FastAPI,HTTPException,Depends
from pydantic import BaseModel

app = FastAPI()

## CRUD OPERATION ON DATABASES 

## CREATE 

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker,declarative_base, Session
from sqlalchemy import Column,Integer,String,Boolean

DATABASE_URL = "sqlite:///./test.db"

engine = create_engine(
    DATABASE_URL,
    connect_args={
        "check_same_thread" : False
    }
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