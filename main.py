from typing import List


from fastapi import FastAPI, Query, Path, Body
from schemas import Book, Author

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}


@app.get('/{pk}')
def get_item(pk: int, q: str = None):
    return {'key': pk, 'q': q}


@app.get('/user/{pk}/items/{item}')
def get_user_item(pk: int, item: str):
    return {'user': pk, 'item': item}


@app.post('/book')
def create_book(item: Book, author: Author, quantity: int = Body(...,)):
    return {'item': item, 'author': author, 'quantity': quantity}


@app.get('/book')
def get_book(q: List[str] = Query([], description='Search book', deprecated=True)):
    return q


@app.get('/book/{pk}')
def get_single_book(pk: int = Path(..., gt=1, le=20),
                    pages: int = Query(None, gt=10, le=50)):
    return {'pk': pk,
            'pages': pages
            }


@app.post('/author')
def create_author(author: Author = Body(..., embed=True)):
    return {'author': author}






























