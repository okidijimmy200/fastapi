from fastapi import Depends, FastAPI
from pytest import Session
import models
from database import SessionLocal, engine
import crud
import schemas
models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# create new dependencies
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post('/create/')
def create_product(product:schemas.Product, db: Session = Depends(get_db)):

    return crud.create_product(title=product.title, description=product.description, price=product.price, available=product.available, db=db)

@app.get('/list/')
def product_list(db: Session = Depends((get_db))):

    return crud.product_list(db=db)