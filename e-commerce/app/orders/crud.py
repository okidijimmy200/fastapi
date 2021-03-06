from fastapi import Depends, Form
from pydantic import EmailStr
from sqlalchemy.orm import Session
from orders.models import Order, OrderItem

from dependencies import get_db


def create_orders(db: Session = Depends(get_db),
                first_name: str=Form(...),
                last_name: str=Form(...),
                email: EmailStr=Form(...),
                address: str=Form(...),
                postal_code: int=Form(...),
                city: str=Form(...)):

    db_order = Order(first_name=first_name,
                    last_name=last_name,
                    email=email,
                    address=address,
                    postal_code=postal_code,
                    city=city)
    db.add(db.order)
    db.commit()
    db.refresh(db_order)

    return db_order

def create_order_item(item, order_id, product_id, db: Session=Depends(get_db)):

    order_item = OrderItem(order_id=order_id,
                            product_id=product_id,
                            price=item['price'],
                            quantity= item['quantity']
    )

    db.add(order_item)
    db.commit()
    db.refresh(order_item)

    return order_item