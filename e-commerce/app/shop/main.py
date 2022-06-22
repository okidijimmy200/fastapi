from http.client import HTTPException
from fastapi.encoders import jsonable_encoder
from fastapi import APIRouter, Depends, FastAPI, Request
from requests import Session
from dependencies import get_db
import crud
from models import Category
from dependencies import templates, env

app = FastAPI()

router = APIRouter(
    prefix='/product'
)

@app.get('/{category_slug}')
def product_list(request: Request, category_slug: str, db:Session = Depends(get_db()),
                page: int=1):
    products = crud.product_list(db=db, category_slug=category_slug)[16*(page-1): 16*(page)]
    categories = db.query(Category).all()
    category = db.query(Category).filter_by(slug=category_slug).first()

    template = env.get_template('list.html')
    return templates.TemplateResponse(template, {'request': request,
    'page': page,
    'products': jsonable_encoder(products),
    'category': jsonable_encoder(category),
    'categories': jsonable_encoder(categories)})

@router.get('/{product_id}/{product_slug}')
def product_detail(request: Request, product_id: int, product_slug: str, db:Session=Depends(get_db)):
    product = jsonable_encoder(crud.product_detail(db=db, id=product_id, slug=product_slug))

    if product is None:
        raise HTTPException(status_code=404, detail='product does not exist')
    template = env.get_template('detail.html')

    return templates.TemplateResponse(template, {'request': request,
                                                'product': jsonable_encoder(product)})
