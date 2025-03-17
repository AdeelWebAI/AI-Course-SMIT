from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from config.database import SessionLocal
from models.todo_model import TodoModel, Users  # ✅ Corrected import
from pydantic import BaseModel
from typing import List
from pymongo import MongoClient 
from dotenv import load_dotenv
import os

load_dotenv()

app = FastAPI()
client = MongoClient(os.getenv("DB_URI"))

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

class TodoCreate(BaseModel):
    title: str
    description: str = None
    status: bool = False

class UserCreate(BaseModel):
    name: str 
    email: str 

class TodoResponse(TodoCreate):
    id: int
    class Config:
        orm_mode = True

@app.post("/todos/{user_id}", response_model=TodoResponse)
def create_todo(user_id: int, todo: TodoCreate, db: Session = Depends(get_db)):
    new_todo = TodoModel(
        title=todo.title,
        description=todo.description,
        status=todo.status,
        user_id=user_id  # ✅ Foreign key added
    )
    db.add(new_todo)
    db.commit()
    db.refresh(new_todo)
    return new_todo

@app.get("/todos/")
def get_todos(db: Session = Depends(get_db)):
    return db.query(TodoModel).all()

@app.get("/todos/{todo_id}")
def get_todo_by_id(todo_id: int, db: Session = Depends(get_db)):
    todo = db.query(TodoModel).filter(TodoModel.id == todo_id).first()
    if not todo:
        raise HTTPException(status_code=404, detail="Todo not found")
    return todo

@app.post("/create_user/")
def create_user(user: UserCreate, db: Session = Depends(get_db)):  # ✅ Fixed function name
    new_user = Users(
        name=user.name,
        email=user.email,
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user
