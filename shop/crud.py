from fastapi import Depends, FastAPI
from sqlalchemy.orm import Session
import models
import main

def create_product(title: str, description:str, price:int,available: bool,  db: Session):
    db_product = models.Shop(title=title, description=description, price=price, available=available)
    db.add(db_product)
    db.commit()
    db.refresh(db_product)

    return db_product  

def product_list(db: Session):
    db_product = db.query(models.Shop).all()

    return db_product