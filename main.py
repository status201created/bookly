from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel

app = FastAPI()

@app.get("/")
async def read_root():
  return {"message": "Hello World!"}

class BookCreateModel(BaseModel):
  title: str
  author: str

@app.get("/greet")
async def greet_name(name: Optional[str] = None, age: Optional[int] = None) -> dict:
  return {"message": f"Hello {name}", "age": age}

@app.post("/books")
async def create_book(book: BookCreateModel) -> dict:
  return {"title": book.title, "author": book.author}
