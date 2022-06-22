from fastapi import Depends
import jinja2
from sqlalchemy.orm import Session
from fastapi.encoders import jsonable_encoder
from starlette_context.middleware import context_middleware

from cart.cart import Cart
from dependencies import get_db

class CartMiddleware(context_middleware):

    @jinja2.pass_context
    def cart(context: dict, db: Session = Depends(get_db)):
        request = context['request']
        return jsonable_encoder(Cart(request, db))

    