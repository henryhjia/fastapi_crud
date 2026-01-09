from pydantic import BaseModel

class ItemCreate(BaseModel):
    name: str # text: str
    price: float
    is_offer: bool = False # is_done: bool = False

class ItemResponse(ItemCreate):
    id: int

    class Config:
        from_attributes = True

# Alias for legacy main.py compatibility
Item = ItemResponse
