from typing import Union

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World1",
            }


@app.get("/about-us")
def read_root1():
    return {"Hello": "World2",
            "another":"wold"}

@app.get("/contact-us")
def read_root2():
    return {"Hello": "World3",
            "another":"wold"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}