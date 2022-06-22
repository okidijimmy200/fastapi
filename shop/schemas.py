from pydantic import BaseModel


from pydantic import BaseModel

class Product(BaseModel):
    title: str
    description: str
    price: int
    available: bool

    class Config:
        orm_mode = True