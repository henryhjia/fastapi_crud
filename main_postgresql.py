# main_postgresql.py
# Use postgreSQL
# Written by Henry Jia
# Date: 2025-12-11
# Comparing this with main_sqlite.py, we can see that the only difference is the database setup
# in line 18 and line 20.  The rest of codes are identical

from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Boolean

app = FastAPI()

# --- Database Setup ---
SQLALCHEMY_DATABASE_URL = "postgresql://stock_user:test123@localhost/fastapi_db"
engine = create_engine(
    SQLALCHEMY_DATABASE_URL
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# --- SQLAlchemy Model (Table) ---
class ItemDB(Base):
    __tablename__ = "items"
    id = Column(Integer, primary_key=True, index=True)
    text = Column(String)
    is_done = Column(Boolean, default=False)

# Create tables
Base.metadata.create_all(bind=engine)

# --- Pydantic Schemas (API Data) ---
from schemas import ItemCreate, ItemResponse

# --- Dependency ---
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# --- Endpoints ---
@app.post("/items", response_model=ItemResponse)
def create_item(item: ItemCreate, db: Session = Depends(get_db)):
    db_item = ItemDB(text=item.text, is_done=item.is_done)
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item

@app.get("/items", response_model=list[ItemResponse])
def list_items(limit: int = 10, db: Session = Depends(get_db)):
    # .all() returns a list of ItemDB objects
    # Pydantic will convert them to ItemResponse automatically because from_attributes=True
    return db.query(ItemDB).limit(limit).all()

@app.get("/items/{item_id}", response_model=ItemResponse)
def read_item(item_id: int, db: Session = Depends(get_db)):
    item = db.query(ItemDB).filter(ItemDB.id == item_id).first()
    if item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return item

@app.put("/items/{item_id}", response_model=ItemResponse)
def update_item(item_id: int, item: ItemCreate, db: Session = Depends(get_db)):
    db_item = db.query(ItemDB).filter(ItemDB.id == item_id).first()
    if db_item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    db_item.text = item.text
    db_item.is_done = item.is_done
    db.commit()
    db.refresh(db_item)
    return db_item

@app.delete("/items/{item_id}", response_model=ItemResponse)
def delete_item(item_id: int, db: Session = Depends(get_db)):
    db_item = db.query(ItemDB).filter(ItemDB.id == item_id).first()
    if db_item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    db.delete(db_item)
    db.commit()
    return db_item
