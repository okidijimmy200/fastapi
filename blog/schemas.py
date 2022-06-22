from pydantic import BaseModel

# class model
class Blog(BaseModel):
    title: str
    body: str