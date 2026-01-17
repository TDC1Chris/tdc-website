#!/usr/bin/env python
"""
Script to populate the database with books - 3 copies of each book
"""
from app import app, db, Book

books_data = [
    {"title": "The Lord of the Rings", "author": "J.R.R. Tolkien", "published_date": "1954-07-29"},
    {"title": "Pride and Prejudice", "author": "Jane Austen", "published_date": "1813-01-28"},
    {"title": "To Kill a Mockingbird", "author": "Harper Lee", "published_date": "1960-07-11"},
    {"title": "1984", "author": "George Orwell", "published_date": "1949-06-08"},
    {"title": "Moby Dick", "author": "Herman Melville", "published_date": "1851-10-18"},
    {"title": "The Great Gatsby", "author": "F. Scott Fitzgerald", "published_date": "1925-04-10"}
]

with app.app_context():
    # Check which books already exist
    for book_data in books_data:
        existing = Book.query.filter_by(title=book_data['title']).first()
        if existing:
            print(f"'{book_data['title']}' already exists. Skipping...")
            continue
        
        # Add 3 copies of the new book
        for copy_num in [1, 2, 3]:
            book = Book(
                title=book_data['title'],
                author=book_data['author'],
                published_date=book_data['published_date'],
                copy_number=copy_num,
                is_available=True
            )
            db.session.add(book)
        
        db.session.commit()
        print(f"Successfully added '{book_data['title']}' (3 copies) to the database!")
    
    total_books = Book.query.count()
    print(f"\nTotal books in library: {total_books}")
