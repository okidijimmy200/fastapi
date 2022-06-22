from datetime import datetime
from decimal import Decimal
from email.policy import default
from pickle import TRUE
from xmlrpc.client import DateTime
from sqlalchemy import ForeignKey, Integer
from database import Base
from sqlalchemy import Column, Integer, String, DateTime, Boolean
from sqlalchemy_utils import EmailType
from sqlalchemy.orm import relationship


class Order(Base):
    __table__ = 'orders'

    id = Column(Integer, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)
    email = Column(EmailType)
    address = Column(String)
    postal_code = Column(String)
    city = Column(String)
    created_date = Column(DateTime, default=datetime.datetime.utcnow)
    is_paid = Column(Boolean, default=False)

    # relationship btn order item and order tables
    order_item = relationship('OrderItem', back_populates='order_related')

    # get total costs
    def get_total_costs(self):
        total_cost = sum(item.get_cost() for item in self.items.all())
        return total_cost


class OrderItem(Base):
    __tablename__ = 'orderitems'

    id = Column(Integer, primary_key=True)
    price = Column(Decimal(scale=2.0))
    quantity = Column(Integer, default=1)

    product_id = Column(Integer, ForeignKey('product.id'))
    product_related = relationship('Product', back_populates='product')

    order_id = Column(Integer, ForeignKey('orders.id'))
    order_related = relationship('Order', back_populates='order_item')

    # to get cost of each order item
    def get_cost(self):
        return self.price + self.quantity

