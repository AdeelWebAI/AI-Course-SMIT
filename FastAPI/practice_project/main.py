# from typing import Union

from fastapi import FastAPI
from fastapi import Depends

# from pydantic import BaseModel
# from typing import Optional

# class Person(BaseModel):
#     id : int
#     name: Optional[str] = None
#     email: str
#     age: int
#     Roll: int

# app = FastAPI()

# @app.post("/users")
# def create_root(variable: Person,id:int,query: Optional[str]= None):
#     try:
#         if id < 10:
#             raise ValueError("ID must be greater than or equal to 10")
#         return{
#             "id": id,
#             "query": query,
#             "status": "success",
#             "data": variable 
#         }
        
#     except Exception as e:
#         return{
#             "Message": str(e),
#             "status": "ERROR",
#             "data": None,
#         }



# @app.get("/users")

# def read_root(q: str, classs: str):
#     try:
#         # Simulate some delay to simulate a slow API call

#         return{
#         "id": 2 ,
#         "status": "success",
#         "query": q,
#         "class": classs ,
#         "data": {
#             "email": "adeelwaraich27@gmail.com",
#             "phone": "03191408024",
#             "address": "Faisalabad",
#             },
#         }
        
#     except Exception as e:
#         return {"Message": str(e),
#                 "status": "ERROR",
#                 "data": None,
#                 }
    
    
    

    # return {
    #         "data":{
    #             "email": "adeelwaraich27@gmail.com",
    #             "phone": "03191408024",
    #             "address": "Faisalabad",
                
    #             },
    #         "status": "OK",
    #         }
    
    
# @app.get("/")
# def read_root():
#     return {"Hello": "World"}

# def common_dependency():
#     return {"key": "value"}

# @app.get("/items")
# def read_items(data: dict = Depends(common_dependency)):
#     return data

