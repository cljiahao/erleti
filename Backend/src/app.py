from fastapi import FastAPI
from pydantic import BaseModel
from sqlalchemy.orm import Session

import database.dbModels as models
from database.database import SessionLocal, engine

app = FastAPI()

models.Base.metadata.create_all(bind=engine)

class Item(BaseModel):
    name: str
    price: float

@app.get("/")
def main():
    return {"Hello": "World"}