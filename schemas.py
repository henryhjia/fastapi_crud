from typing import Optional, List
from pydantic import BaseModel

class ItemBase(BaseModel):
    name: str
    price: float
    is_offer: Optional[bool] = None

class ItemCreate(ItemBase):
    pass

class Item(ItemBase):
    id: int

    class Config:
        from_attributes = True
