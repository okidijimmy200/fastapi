from sqlalchemy import Boolean, TEXT, DECIMAL, Column, ForeignKey, Integer, String, DateTime
from slugify import slugify
import datetime
from sqlalchemy_utils import URLType
from sqlalchemy.orm import relationship

from database import Base

class Category(Base):
    __tablename__ = 'category'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    slug = Column(String, unique=True)

    def __init__(self, *args, **kwargs):
        if not 'slug' in kwargs:
            kwargs['slug'] = slugify(kwargs.get('name', ''))
        super(Category, self).__init__(*args, **kwargs)

    product_category = relationship('Product', back_populated='category_related')


class Product(Base):
    __table__ = 'product'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    description = Column(TEXT)
    url = Column(URLType )
    price = Column(DECIMAL(scale=2))
    available = Column(Boolean, default=True)
    created_date = Column(DateTime, default=datetime.datetime.utcnow)
    updated = Column(DateTime, onupdate=datetime.datetime.now)
    slug = Column(String, unique=True)
    


    def __init__(self, *args, **kwargs):
        if not 'slug' in kwargs:
            kwargs['slug'] = slugify(kwargs.get('name', ''))
        super(Category, self).__init__(*args, **kwargs)

    category_id = Column(Integer, ForeignKey('category.id'))
    category_related = relationship('Category', back_populated='product_category')
 
    product_order = relationship('OrderItem', back_populates='product_related')
      