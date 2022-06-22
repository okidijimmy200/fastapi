from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel
import uvicorn

app = FastAPI()

# uvicorn main:app --reload

@app.get('/blog')
# query the db '/blog?limit=50'
def index(limit=10, published: bool = True, sort: Optional[str] = None):
    if published:
        return {'data': f'{limit} published from the db'}
    else:
         return {'data': f'{limit} blogs from the db'}

@app.get('/blog/unpublished')
def unpublished():
    return {'data': 'return all unpublished blogs'}

@app.get('/blog/{id}')
def show(id: int):
    return {'data': id}


# fetch comments with blog
@app.get('/blog/{id}/comments')
def comments(id, limit=10):
    return {'data': {'1', '2'}}

#  blog model
class Blog(BaseModel):
    title: str
    body: str
    publihsed: Optional[bool]
#  post method to create a new blog
@app.post('/blog')
def create_blog(request: Blog): # use the blog model
    return {'data': f'blog is created with {request.title}'}


if __name__ == "__main__":
    uvicorn.run(app, host='127.0.0.1', port=9000)