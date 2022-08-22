from fastapi import FastAPI
from schemas import Book


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
def create_book(item: Book):
    return item
