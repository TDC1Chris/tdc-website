from flask import Flask, request
from flask_restful import Resource, Api, abort

app = Flask(__name__)
api = Api(app)

# In-memory data storage
books = {
    1: {"id": 1, "title": "The Lord of the Rings", "author": "J.R.R. Tolkien", "published_date": "1954-07-29"},
    2: {"id": 2, "title": "Pride and Prejudice", "author": "Jane Austen", "published_date": "1813-01-28"},
    3: {"id": 3, "title": "To Kill a Mockingbird", "author": "Harper Lee", "published_date": "1960-07-11"},
    4: {"id": 4, "title": "1984", "author": "George Orwell", "published_date": "1949-06-08"},
    5: {"id": 5, "title": "Moby Dick", "author": "Herman Melville", "published_date": "1851-10-18"}
}
next_id = 6

class BookList(Resource):
    def get(self):
        # Logic to retrieve and return the list of books
        return {"books": list(books.values())}, 200

    def post(self):
        # Logic to create a new book entry
        global next_id
        data = request.get_json()
        
        if not data or 'title' not in data or 'author' not in data:
            abort(400, message="Missing required fields: title and author")
        
        new_book = {
            "id": next_id,
            "title": data['title'],
            "author": data['author'],
            "published_date": data.get('published_date', '')
        }
        
        books[next_id] = new_book
        next_id += 1
        
        return {"message": "Book created successfully!", "book": new_book}, 201

class Book(Resource):
    def get(self, book_id):
        # Logic to retrieve a specific book by its ID
        if book_id not in books:
            abort(404, message=f"Book {book_id} not found")
        
        return {"book": books[book_id]}, 200

    def put(self, book_id):
        # Logic to update a specific book by its ID
        if book_id not in books:
            abort(404, message=f"Book {book_id} not found")
        
        data = request.get_json()
        
        if 'title' in data:
            books[book_id]['title'] = data['title']
        if 'author' in data:
            books[book_id]['author'] = data['author']
        if 'published_date' in data:
            books[book_id]['published_date'] = data['published_date']
        
        return {"message": "Book updated successfully!", "book": books[book_id]}, 200

    def delete(self, book_id):
        # Logic to delete a specific book by its ID
        if book_id not in books:
            abort(404, message=f"Book {book_id} not found")
        
        deleted_book = books.pop(book_id)
        return {"message": "Book deleted successfully!", "book": deleted_book}, 200

api.add_resource(BookList, '/books')
api.add_resource(Book, '/books/<int:book_id>')

if __name__ == '__main__':
    app.run(debug=True)

