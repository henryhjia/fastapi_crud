from typing import Optional, List
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

class Item(BaseModel):
    id: int
    name: str
    price: float
    is_offer: Optional[bool] = None

app = FastAPI()

# Simulating a database with a list
items_db: List[Item] = []
@app.get("/")
async def read_root():
    return {"Hello": "World"} 

@app.get("/hello")
def say_hello():
    return {"message": "Hello, World!"}

@app.post("/items/", response_model=Item)
def create_item(item: Item):
    items_db.append(item)
    return item

@app.get("/items/", response_model=List[Item])
def read_items():
    return items_db

@app.get("/items/{item_id}", response_model=Item)
def read_item(item_id: int):
    for item in items_db:
        if item.id == item_id:
            return item
    raise HTTPException(status_code=404, detail="Item not found")

@app.put("/items/{item_id}", response_model=Item)
def update_item(item_id: int, item: Item):
    for index, existing_item in enumerate(items_db):
        if existing_item.id == item_id:
            items_db[index] = item
            return item
    raise HTTPException(status_code=404, detail="Item not found")

@app.delete("/items/{item_id}")
def delete_item(item_id: int):
    for index, item in enumerate(items_db):
        if item.id == item_id:
            items_db.pop(index)
            return {"message": "Item deleted successfully"}
    raise HTTPException(status_code=404, detail="Item not found")
