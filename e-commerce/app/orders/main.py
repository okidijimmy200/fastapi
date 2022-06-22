from fastapi import APIRouter, Depends, Request, status
from sqlalchemy.orm import Session
from starlette.responses import RedirectResponse
from dependencies import get_db, env, templates

from fastapi import Form
from cart.cart import Cart
from pydantic import EmailStr
from dependencies import get_db, templates
import crud


router = APIRouter(
    prefix='/order'
)

@router.get('/create_order')
def order_add(request: Request, db: Session=Depends(get_db)):

    cart = Cart(request, db)
    template = env.get_template('order.html')

    return templates.TemplateResponse(template, {'request': request,
                                    'cart': cart})

@router.post('/create-order')
def order_add(request: Request,
            db: Session=Depends(get_db),
            first_name: str=Form(...),
            last_name: str=Form(...),
            email: EmailStr=Form(...),
            address: str=Form(...),
            postal_code: int=Form(...),
            city: str=Form(...)):

    cart = Cart(request, db)
    db.order = crud.create_orders(db, first_name, last_name, email, address, postal_code, city)
    order_id = db.order.id

    for item in cart:
        product_id = item['product']['id']
        crud.create_order_item(item, order_id, product_id, db)

    cart.remove_all()

    return RedirectResponse(url='/cart', status_code=status.HTTP_303_SEE_OTHER)
