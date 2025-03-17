from fastapi import FastAPI
from pymongo import MongoClient 
from dotenv import load_dotenv
import os

load_dotenv()


# We can test either load_dotenv is loaded or not by printing the following things
# print(os.getenv("DB_URI"))

app = FastAPI()
client = MongoClient(os.getenv("DB_URI"))

def get_database_client():
    try:
        client = MongoClient(os.getenv("DB_URI"))
        print("Successfully connected to MongoDB!")
        return client
    


    except Exception as e:
        print(f"Error connecting to MongoDB: {e}")
        return None
client = get_database_client()
db = client["my_database"]


@app.get("/")
def read_root():
    return {"hello": "world"}
print(list(db.todos.find()))


@app.get("/todos")
def read_todos():
    try:
        todos = db.todos.find()
        listTodos = {}
        for todo in todos:
            print(todo)
            listTodos.append({
                "id": str(todo["_id"]),
                "title": todo["title"],
                "description": todo["description"],
                "completed at": todo["completed at"]
            })
            
        return {
            "status": "ok",
            "message": "Todos retrieved successfully",
            "data": listTodos
            }
    except Exception as e:
        return {
            "data":[],
            "error": "Error reading todos",
            "message": str(e),
            "status": "failed"}