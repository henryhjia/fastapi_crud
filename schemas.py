from pydantic import BaseModel

class ItemCreate(BaseModel):
    text: str
    is_done: bool = False

class ItemResponse(ItemCreate):
    id: int

    class Config:
        from_attributes = True
