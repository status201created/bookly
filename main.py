from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

app = FastAPI()

books = [
  {
    "id": 1,
    "title": "1984",
    "author": "George Orwell",
    "publisher": "Secker & Warburg",
    "published_date": "1949-06-08",
    "page_count": 328,
    "language": "English"
  }, 
  {
    "id": 2,
    "title": "To Kill a Mockingbird",
    "author": "Harper Lee",
    "publisher": "J.B. Lippincott & Co.",
    "published_date": "1960-07-11",
    "page_count": 281,
    "language": "English"
  },
  {
    "id": 3,
    "title": "The Great Gatsby",
    "author": "F. Scott Fitzgerald",
    "publisher": "Charles Scribner's Sons",
    "published_date": "1925-04-10",
    "page_count": 180,
    "language": "English"
  },
  {
    "id": 4,
    "title": "Brave New World",
    "author": "Aldous Huxley",
    "publisher": "Chatto & Windus",
    "published_date": "1932-08-18",
    "page_count": 268,
    "language": "English"
  },
  {
    "id": 5,
    "title": "Fahrenheit 451",
    "author": "Ray Bradbury",
    "publisher": "Ballantine Books",
    "published_date": "1953-10-19",
    "page_count": 158,
    "language": "English"
  }
]

class Book(BaseModel):
  id: int
  title: str
  author: str
  publisher: str
  published_date: str
  page_count: int
  language: str
  
@app.get("/books", response_model=List[Book])
async def get_books():
    return books

@app.get("/books/{book_id}", response_model=Book)
async def get_book(book_id: int):
    for book in books:
        if book["id"] == book_id:
            return book
    raise HTTPException(status_code=404, detail="Book not found")
  
@app.post("/books", response_model=Book)
async def create_book(book: Book):
    if any(b["id"] == book.id for b in books):
        raise HTTPException(status_code=400, detail="Book with this ID already exists")
    books.append(book.model_dump())
    return book
  
@app.put("/books/{book_id}", response_model=Book)
async def update_book(book_id: int, book: Book):
    for index, b in enumerate(books):
        if b["id"] == book_id:
            books[index] = book.model_dump()
            return book
    raise HTTPException(status_code=404, detail="Book not found")
  
@app.delete("/books/{book_id}", response_model=Book)
async def delete_book(book_id: int):
    for index, book in enumerate(books):
        if book["id"] == book_id:
            deleted_book = books.pop(index)
            return deleted_book
    raise HTTPException(status_code=404, detail="Book not found")