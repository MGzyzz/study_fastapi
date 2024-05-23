from typing import Union
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World!"}


class Item(BaseModel):
    name: str
    price: float
    is_offer: Union[bool, None] = None


@app.put("/items/{item_id}")
def read_time(item_id: int, item: Item):
    return {"item_name": item.name, "item_id": item_id}

