from fastapi import APIRouter, HTTPException, status
from typing import List
from src.books.book_data import books
from src.books.schemas import Book, BookUpdate

book_router = APIRouter()

@book_router.get("/", response_model=List[Book], status_code=status.HTTP_200_OK)
async def get_books():
    return books

@book_router.get("/{book_id}", response_model=Book, status_code=status.HTTP_200_OK)
async def get_book(book_id: int):
    for book in books:
        if book["id"] == book_id:
            return book
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Book not found")
  
@book_router.post("/", response_model=Book, status_code=status.HTTP_201_CREATED)
async def create_book(book: Book):
    if any(b["id"] == book.id for b in books):
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Book with this ID already exists")
    books.append(book.model_dump())
    return book
  
@book_router.patch("/{book_id}", response_model=Book, status_code=status.HTTP_200_OK)
async def update_book(book_id: int, book: BookUpdate):
    for index, b in enumerate(books):
        if b["id"] == book_id:
            if book.title is not None:
                b["title"] = book.title
            if book.author is not None:
                b["author"] = book.author
            if book.publisher is not None:
                b["publisher"] = book.publisher
            if book.published_date is not None:
                b["published_date"] = book.published_date
            if book.page_count is not None:
                b["page_count"] = book.page_count
            if book.language is not None:
                b["language"] = book.language
            return b
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Book not found")
  
@book_router.delete("/{book_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_book(book_id: int):
    for index, book in enumerate(books):
        if book["id"] == book_id:
            books.remove(book)
            return {}
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Book not found")
