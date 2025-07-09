from fastapi import FastAPI, Header
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

@app.get("/headers", status_code=200)
async def read_headers(
  user_agent: str = Header(None), 
  accept: str = Header(None),
  host: str = Header(None),
  content_type: str = Header(None)
) -> dict:
    return {
      "User-Agent": user_agent, 
      "Accept": accept,
      "Host": host,
      "Content-Type": content_type
      }
