### SQLAlchemy

# SQLAlchemy ek ORM (Object Relational Mapping) hai jo Python ko database ke saath connect karta hai.
# Iski madad se hum raw SQL queries likhne ke bajay Python classes aur objects se database handle kar sakte hain.

# Database engine banane ke liye create_engine function import kar rahe hain.
from sqlalchemy import create_engine
# sessionmaker database session banata hai aur declarative_base ORM models ka base class deta hai.
from sqlalchemy.orm import sessionmaker,declarative_base
# Ye classes table ke columns ke data types define karne ke kaam aati hain.
from sqlalchemy import Column,Integer,String,Boolean

# SQLite database file ka location aur naam yahan define kiya gaya hai.
DATABASE_URL = "sqlite:///./test.db"

engine = create_engine(
    DATABASE_URL,
    connect_args={"check_same_thread":False}  # IN L14 we passed this arguement while making the variable conn
)

# Is factory se jab bhi zaroorat ho, database ka naya session banega.
sessionlocal = sessionmaker(bind=engine)

# Saare ORM models isi base class se inherit karenge.
Base = declarative_base()

class Todo(Base):
    __tablename__ = "todos"

    id = Column(Integer,primary_key=True,index=True)
    title=Column(String)
    completed=Column(Boolean)

# Model ke basis par database mein table create kar diya jayega agar pehle se nahi hai.
Base.metadata.create_all(bind=engine)

from fastapi import FastAPI,HTTPException,Depends
from pydantic import BaseModel

# Database session ki type hint ke liye Session import kar rahe hain.
from sqlalchemy.orm import Session

app = FastAPI()

# Ye dependency har request ke liye database session provide karegi.
def get_db():
    # Database ke saath connection/session open kar rahe hain.
    db = sessionlocal()
    try:
        # 'yield' ke through session endpoint function ko diya ja raha hai.
        yield db
    finally:
        # Request complete hone ke baad session close karke resources release kar rahe hain.
        db.close()

@app.get("/")
def home(db: Session=Depends(get_db)):
    return{
        "message": "db created"
    }  