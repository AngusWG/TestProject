#!/usr/bin/python3
# encoding: utf-8 
# @Time    : 2020/6/21 18:03
# @author  : zza
# @Email   : 740713651@qq.com
# @File    : fastapi_main.py
from typing import List, Optional

import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()



class Item(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    tax: Optional[float] = None
    tags: List[str] = []


@app.post("/items/", response_model=Item)
async def create_item(item: Item):
    return item


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "q": q}


@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item):
    return {"item_name": item.name, "item_id": item_id}


if __name__ == '__main__':
    uvicorn.run(app, port=8080, host='127.0.0.1')
