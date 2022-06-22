from fastapi import FastAPI
import shop
from database import engine
from starlette.staticfiles import StaticFiles
from starlette.middleware.sessions import SessionMiddleware
from starlette.middleware import Middleware 
from context_processor import CartMiddleware
from orders import main, models
import orders

from dependencies import env
import cart
from cart import main

secret_key = 'cart'

middleware = [
    Middleware(SessionMiddleware, secret_key=secret_key),
    Middleware(CartMiddleware)
]

app=FastAPI(middleware=middleware)

# make the variable global
env.globals['cart_context'] = CartMiddleware.cart

app.mount('/static', StaticFiles(directory='static'), name='static')

shop.models.Base.metadata.create_all(bind=engine)
orders.models.Base.metadata.create_all(bind=engine)

app.include_router(shop.main.router)
app.include_router(cart.main.router)
app.include_router(orders.main.router)