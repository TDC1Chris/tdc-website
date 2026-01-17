#!/usr/bin/env python
"""
Script to populate the database with books - 3 copies of each book
"""
from app import app, db, Book

books_data = [
    {"title": "The Lord of the Rings", "author": "J.R.R. Tolkien", "published_date": "1954-07-29", "isbn": "978-0544003415"},
    {"title": "Pride and Prejudice", "author": "Jane Austen", "published_date": "1813-01-28", "isbn": "978-0141439518"},
    {"title": "To Kill a Mockingbird", "author": "Harper Lee", "published_date": "1960-07-11", "isbn": "978-0061120084"},
    {"title": "1984", "author": "George Orwell", "published_date": "1949-06-08", "isbn": "978-0451524935"},
    {"title": "Moby Dick", "author": "Herman Melville", "published_date": "1851-10-18", "isbn": "978-0142437247"},
    {"title": "The Great Gatsby", "author": "F. Scott Fitzgerald", "published_date": "1925-04-10", "isbn": "978-0743273565"},
    {"title": "Made in America", "author": "Bill Bryson", "published_date": "1994-09-01", "isbn": "978-0380727384"},
    {"title": "Weapons of Math Destruction", "author": "Cathy O'Neil", "published_date": "2016-09-06", "isbn": "978-0553418835"},
    {"title": "Entangled Life", "author": "Merlin Sheldrake", "published_date": "2020-05-12", "isbn": "978-0525510314"},
    {"title": "Tree", "author": "Melina Sempill Watts", "published_date": "2019-03-05", "isbn": "978-0399580765"}
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
                isbn=book_data.get('isbn'),
                copy_number=copy_num,
                is_available=True
            )
            db.session.add(book)
        
        db.session.commit()
        print(f"Successfully added '{book_data['title']}' (3 copies) to the database!")
    
    total_books = Book.query.count()
    print(f"\nTotal books in library: {total_books}")
