# TDC Reading Library - Flask Application

A personal reading library management system built with Flask, demonstrating database management, user authentication, and RESTful API design.

## Features

- **User Authentication**: Login/logout functionality with admin roles
- **Book Management**: Track library books with multiple copies
- **Reading Lists**: Personal wishlist, currently reading, and completed books
- **Book Reviews**: Blog-style posts and reviews with ratings
- **Weather Integration**: Get reading recommendations based on current weather
- **RESTful API**: API endpoints for book CRUD operations

## Tech Stack

- **Backend**: Flask 3.x
- **Database**: SQLite with SQLAlchemy ORM
- **Authentication**: Flask-Login
- **Admin Panel**: Flask-Admin
- **API**: Flask-RESTful
- **Database Migrations**: Flask-Migrate (Alembic)

## Installation

### Prerequisites

- Python 3.8 or higher
- Virtual environment (recommended)

### Setup

1. Navigate to the Flask project directory:
   ```bash
   cd home-library-Flask
   ```

2. Activate the virtual environment (it should already exist):
   ```bash
   source venv/bin/activate  # On Linux/Mac
   # or
   venv\Scripts\activate  # On Windows
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Initialize the database (if not already done):
   ```bash
   flask db upgrade
   ```

5. Run the application:
   ```bash
   python app.py
   ```

The application will be available at `http://127.0.0.1:5000`

## Database Models

- **User**: User accounts with authentication and location data
- **Book**: Library books with copy tracking and availability
- **UserBook**: Personal reading lists with status and ratings
- **Post**: Blog posts and book reviews
- **Comment**: Comments on posts

## API Endpoints

### Books API (app_api.py)

- `GET /books` - List all books
- `POST /books` - Create a new book
- `GET /books/<id>` - Get a specific book
- `PUT /books/<id>` - Update a book
- `DELETE /books/<id>` - Delete a book

## Routes

### Authentication
- `/login` - User login
- `/logout` - User logout
- `/users/create` - Create new user account

### Library Management
- `/books` - Browse library books
- `/books/checkout/<id>` - Check out a book
- `/books/return/<id>` - Return a book

### Reading Lists
- `/reading` - Personal reading dashboard
- `/reading/wishlist` - Books to read
- `/reading/completed` - Finished books
- `/reading/add` - Add book to reading list

### Blog & Reviews
- `/blog` - View all posts
- `/blog/new` - Create a post or review
- `/blog/post/<id>` - View a specific post

### Weather & Recommendations
- `/weather` - Current weather for user location
- `/weather/recommendations` - Get reading suggestions based on weather

### Demo Mode
- `/demo` - Try the app with sample data (no login required)
- `/demo/exit` - Exit demo mode

## Admin Features

Users with admin privileges can:
- Manage all users
- Toggle admin status for other users
- Delete any posts or comments
- Access Flask-Admin panel at `/admin`

## Configuration

The application uses the following configuration:
- **Database**: `sqlite:///example.db` (in instance folder)
- **Secret Key**: Should be changed in production (currently in app.py)
- **Debug Mode**: Enabled by default (disable in production)

## Security Notes

⚠️ **For Production Use**:
1. Change the `SECRET_KEY` to a secure random value
2. Set `DEBUG = False`
3. Use a production-ready database (PostgreSQL, MySQL)
4. Implement proper SSL/TLS
5. Add rate limiting
6. Implement CSRF protection for all forms
7. Use environment variables for sensitive configuration

## Development

### Database Migrations

To create a new migration after model changes:
```bash
flask db migrate -m "Description of changes"
flask db upgrade
```

### Running the API separately

The `app_api.py` file contains a separate Flask-RESTful API that can run independently:
```bash
python app_api.py
```

## Project Structure

```
home-library-Flask/
├── app.py                 # Main application
├── app_api.py            # RESTful API
├── populate_books.py     # Database seeding script
├── requirements.txt      # Python dependencies
├── instance/             # Database and instance-specific files
├── migrations/           # Alembic database migrations
├── static/               # CSS and static assets
│   └── css/
│       └── tdc-theme.css
└── templates/            # HTML templates
    ├── base.html
    ├── home.html
    ├── login.html
    ├── books.html
    ├── blog.html
    ├── weather.html
    ├── partials/
    │   ├── header.html
    │   └── footer.html
    └── reading/
        ├── dashboard.html
        ├── wishlist.html
        ├── completed.html
        ├── add_book.html
        ├── rate_book.html
        └── recommendations.html
```

## License

Part of the Total Design Consulting portfolio website.

## Author

Christopher Clubb - [Total Design Consulting](https://totaldesignconsulting.net)
