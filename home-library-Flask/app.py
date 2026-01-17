# source !/venv/bin/activate
# Coding --utf-8--
'''
This is the first Flask project that demonstrates my Flask, SQLAlchemy, and DB Management skills.
'''
from flask import Flask, render_template, request, redirect, url_for, session, flash
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from flask_login import LoginManager, UserMixin, login_user, logout_user, login_required, current_user
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime, timedelta
import requests

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///example.db'
app.config['SECRET_KEY'] = 'your-secret-key-here'  # Required for Flask-Admin
db = SQLAlchemy(app)
migrate = Migrate(app, db)

# Setup Flask-Login
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    personal_name = db.Column(db.String(120), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    phone_number = db.Column(db.String(20), nullable=True)
    password_hash = db.Column(db.String(255), nullable=False)
    is_admin = db.Column(db.Boolean, default=False, nullable=False)
    city = db.Column(db.String(100), nullable=True)
    state = db.Column(db.String(2), nullable=True)
    latitude = db.Column(db.Float, nullable=True)
    longitude = db.Column(db.Float, nullable=True)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)
    
    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return f'<User {self.username}>'


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    book_id = db.Column(db.Integer, db.ForeignKey('book.id'), nullable=True)
    rating = db.Column(db.Integer, nullable=True)  # 1-5 star rating
    created_at = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)

    user = db.relationship('User', backref=db.backref('posts', lazy=True))
    book = db.relationship('Book', backref=db.backref('reviews', lazy=True))

    def __repr__(self):
        return f'<Post {self.title}>'


class Comment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    post_id = db.Column(db.Integer, db.ForeignKey('post.id'), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)

    user = db.relationship('User', backref=db.backref('comments', lazy=True))
    post = db.relationship('Post', backref=db.backref('comments', lazy=True, cascade='all, delete-orphan'))

    def __repr__(self):
        return f'<Comment on Post {self.post_id}>'

class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    author = db.Column(db.String(200), nullable=False)
    published_date = db.Column(db.String(20), nullable=True)
    copy_number = db.Column(db.Integer, nullable=False)  # Which copy (1, 2, or 3)
    is_available = db.Column(db.Boolean, default=True, nullable=False)
    checkout_date = db.Column(db.DateTime, nullable=True)
    checked_out_by = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=True)
    
    user = db.relationship('User', backref=db.backref('checked_out_books', lazy=True))

    @property
    def due_date(self):
        if self.checkout_date:
            return self.checkout_date + timedelta(days=30)
        return None
    
    @property
    def is_overdue(self):
        if self.due_date:
            return datetime.now() > self.due_date
        return False

    def __repr__(self):
        return f'<Book {self.title} (Copy {self.copy_number})>'


class UserBook(db.Model):
    """Personal reading list - joins User to Books with status/ratings"""
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    # Book info (support custom entries not in library)
    book_id = db.Column(db.Integer, db.ForeignKey('book.id'), nullable=True)
    custom_title = db.Column(db.String(200), nullable=True)
    custom_author = db.Column(db.String(200), nullable=True)

    # Status: 'wishlist', 'reading', 'completed'
    status = db.Column(db.String(20), default='wishlist', nullable=False)

    # Rating/review (for completed)
    rating = db.Column(db.Integer, nullable=True)  # 1-5 stars
    review = db.Column(db.Text, nullable=True)

    # Timestamps
    added_date = db.Column(db.DateTime, default=datetime.utcnow)
    started_date = db.Column(db.DateTime, nullable=True)
    completed_date = db.Column(db.DateTime, nullable=True)

    # Genre for weather matching
    genre = db.Column(db.String(50), nullable=True)

    user = db.relationship('User', backref=db.backref('reading_list', lazy=True))
    book = db.relationship('Book', backref=db.backref('user_entries', lazy=True))

    @property
    def title(self):
        """Get title from linked book or custom entry"""
        if self.book:
            return self.book.title
        return self.custom_title

    @property
    def author(self):
        """Get author from linked book or custom entry"""
        if self.book:
            return self.book.author
        return self.custom_author

    def __repr__(self):
        return f'<UserBook {self.title} - {self.status}>'


# Setup Flask-Admin
admin = Admin(app, name='Database Admin')
admin.add_view(ModelView(User, db.session))
admin.add_view(ModelView(Post, db.session))
admin.add_view(ModelView(Book, db.session))
admin.add_view(ModelView(Comment, db.session))
admin.add_view(ModelView(UserBook, db.session))

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

def admin_required(f):
    from functools import wraps
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if not current_user.is_authenticated or not current_user.is_admin:
            flash('You need admin privileges to access this page.')
            return redirect(url_for('home'))
        return f(*args, **kwargs)
    return decorated_function
    




@app.route('/')
def home():
    return render_template('home.html', current_user=current_user)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = User.query.filter_by(username=username).first()
        
        if user and user.check_password(password):
            login_user(user)
            flash(f'Welcome back, {user.personal_name}!')
            return redirect(url_for('home'))
        else:
            flash('Invalid username or password')
    
    return render_template('login.html')

@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash('You have been logged out.')
    return redirect(url_for('home'))

@app.route('/users')
@login_required
@admin_required
def users():
    all_users = User.query.all()
    return render_template('users.html', users=all_users)

@app.route('/users/create', methods=['GET', 'POST'])
def create_user():
    if request.method == 'POST':
        username = request.form['username']
        personal_name = request.form['personal_name']
        email = request.form['email']
        phone_number = request.form['phone_number']
        password = request.form['password']
        
        new_user = User(username=username, personal_name=personal_name, 
                       email=email, phone_number=phone_number, is_admin=False)
        new_user.set_password(password)
        db.session.add(new_user)
        db.session.commit()
        flash('Account created successfully! You can now log in.')
        return redirect(url_for('login'))
    
    return render_template('create_user.html')

@app.route('/users/edit/<int:id>', methods=['GET', 'POST'])
@login_required
@admin_required
def edit_user(id):
    user = User.query.get_or_404(id)
    
    if request.method == 'POST':
        user.username = request.form['username']
        user.personal_name = request.form['personal_name']
        user.email = request.form['email']
        user.phone_number = request.form['phone_number']
        db.session.commit()
        flash('User updated successfully!')
        return redirect(url_for('users'))
    
    return render_template('edit_user.html', user=user)

@app.route('/users/delete/<int:id>', methods=['POST'])
@login_required
@admin_required
def delete_user(id):
    user = User.query.get_or_404(id)
    db.session.delete(user)
    db.session.commit()
    flash('User deleted successfully!')
    return redirect(url_for('users'))

@app.route('/users/toggle_admin/<int:id>', methods=['POST'])
@login_required
@admin_required
def toggle_admin(id):
    user = User.query.get_or_404(id)
    user.is_admin = not user.is_admin
    db.session.commit()
    status = 'granted' if user.is_admin else 'revoked'
    flash(f'Admin privileges {status} for {user.username}')
    return redirect(url_for('users'))

@app.route('/books')
@login_required
def books():
    all_books = Book.query.order_by(Book.title, Book.copy_number).all()
    # Group books by title
    books_by_title = {}
    for book in all_books:
        if book.title not in books_by_title:
            books_by_title[book.title] = {
                'title': book.title,
                'author': book.author,
                'published_date': book.published_date,
                'copies': []
            }
        books_by_title[book.title]['copies'].append(book)
    
    return render_template('books.html', books_by_title=books_by_title)

@app.route('/books/checkout/<int:book_id>', methods=['POST'])
@login_required
def checkout_book(book_id):
    book = Book.query.get_or_404(book_id)
    
    if not book.is_available:
        flash('This book is already checked out.')
        return redirect(url_for('books'))
    
    book.is_available = False
    book.checkout_date = datetime.now()
    book.checked_out_by = current_user.id
    db.session.commit()
    
    flash(f'Successfully checked out "{book.title}" (Copy {book.copy_number}). Due back on {book.due_date.strftime("%B %d, %Y")}.')
    return redirect(url_for('books'))

@app.route('/books/return/<int:book_id>', methods=['POST'])
@login_required
def return_book(book_id):
    book = Book.query.get_or_404(book_id)
    
    if book.is_available:
        flash('This book is not currently checked out.')
        return redirect(url_for('books'))
    
    if book.checked_out_by != current_user.id and not current_user.is_admin:
        flash('You can only return books that you checked out.')
        return redirect(url_for('books'))
    
    book.is_available = True
    book.checkout_date = None
    book.checked_out_by = None
    db.session.commit()
    
    flash(f'Successfully returned "{book.title}" (Copy {book.copy_number}). Thank you!')
    return redirect(url_for('books'))


@app.route('/blog')
@login_required
def blog():
    """Display all blog posts and reviews"""
    posts = Post.query.order_by(Post.created_at.desc()).all()
    return render_template('blog.html', posts=posts)


@app.route('/blog/new', methods=['GET', 'POST'])
@login_required
def create_post():
    """Create a new blog post or book review"""
    if request.method == 'POST':
        title = request.form.get('title')
        content = request.form.get('content')
        book_id = request.form.get('book_id')
        rating = request.form.get('rating')
        
        # Convert empty string to None for book_id
        if book_id == '':
            book_id = None
        
        # Convert rating to int if provided
        if rating:
            rating = int(rating)
        else:
            rating = None
        
        post = Post(
            title=title,
            content=content,
            user_id=current_user.id,
            book_id=book_id,
            rating=rating
        )
        db.session.add(post)
        db.session.commit()
        flash('Post created successfully!')
        return redirect(url_for('blog'))
    
    # Get all books for the dropdown
    books = Book.query.order_by(Book.title).all()
    # Get unique books (title + author combination)
    unique_books = {}
    for book in books:
        key = (book.title, book.author)
        if key not in unique_books:
            unique_books[key] = book
    
    return render_template('create_post.html', books=list(unique_books.values()))


@app.route('/blog/post/<int:post_id>', methods=['GET', 'POST'])
@login_required
def view_post(post_id):
    """View a single post and its comments"""
    post = Post.query.get_or_404(post_id)
    
    if request.method == 'POST':
        content = request.form.get('content')
        if content:
            comment = Comment(
                content=content,
                user_id=current_user.id,
                post_id=post_id
            )
            db.session.add(comment)
            db.session.commit()
            flash('Comment added successfully!')
            return redirect(url_for('view_post', post_id=post_id))
    
    comments = Comment.query.filter_by(post_id=post_id).order_by(Comment.created_at.asc()).all()
    return render_template('view_post.html', post=post, comments=comments)


@app.route('/blog/post/<int:post_id>/delete', methods=['POST'])
@login_required
def delete_post(post_id):
    """Delete a post (only by author or admin)"""
    post = Post.query.get_or_404(post_id)
    
    if post.user_id != current_user.id and not current_user.is_admin:
        flash('You do not have permission to delete this post.')
        return redirect(url_for('blog'))
    
    db.session.delete(post)
    db.session.commit()
    flash('Post deleted successfully!')
    return redirect(url_for('blog'))


@app.route('/blog/comment/<int:comment_id>/delete', methods=['POST'])
@login_required
def delete_comment(comment_id):
    """Delete a comment (only by author or admin)"""
    comment = Comment.query.get_or_404(comment_id)
    post_id = comment.post_id
    
    if comment.user_id != current_user.id and not current_user.is_admin:
        flash('You do not have permission to delete this comment.')
        return redirect(url_for('view_post', post_id=post_id))
    
    db.session.delete(comment)
    db.session.commit()
    flash('Comment deleted successfully!')
    return redirect(url_for('view_post', post_id=post_id))


@app.route('/weather')
@login_required
def weather():
    # Use user's location if available, otherwise default to New York City
    if current_user.latitude and current_user.longitude:
        latitude = current_user.latitude
        longitude = current_user.longitude
        location_name = f"{current_user.city}, {current_user.state}" if current_user.city and current_user.state else "Your Location"
    else:
        latitude = 40.7128
        longitude = -74.0060
        location_name = "New York City, NY (Default - Update your profile to set your location)"
    
    try:
        # NWS API requires a User-Agent header
        headers = {
            'User-Agent': '(Flask Weather App, contact@example.com)'
        }
        
        # Get the grid point data
        points_url = f'https://api.weather.gov/points/{latitude},{longitude}'
        points_response = requests.get(points_url, headers=headers, timeout=10)
        points_response.raise_for_status()
        points_data = points_response.json()
        
        # Get the forecast URL from the points data
        forecast_url = points_data['properties']['forecast']
        
        # Get the 7-day forecast
        forecast_response = requests.get(forecast_url, headers=headers, timeout=10)
        forecast_response.raise_for_status()
        forecast_data = forecast_response.json()
        
        # Extract the periods (each period is ~12 hours)
        periods = forecast_data['properties']['periods'][:14]  # Get up to 7 days (14 periods)
        
        return render_template('weather.html', periods=periods, location=location_name)
        
    except requests.exceptions.RequestException as e:
        flash(f'Error fetching weather data: {str(e)}')
        return render_template('weather.html', periods=None, location=location_name, error=True)
    except KeyError as e:
        flash('Error parsing weather data from National Weather Service')
        return render_template('weather.html', periods=None, location=location_name, error=True)

# Common US city coordinates
CITY_COORDINATES = {
    ('NEW YORK', 'NY'): (40.7128, -74.0060),
    ('HOBOKEN', 'NJ'): (40.7439, -74.0324),
    ('JERSEY CITY', 'NJ'): (40.7178, -74.0431),
    ('NEWARK', 'NJ'): (40.7357, -74.1724),
    ('LOS ANGELES', 'CA'): (34.0522, -118.2437),
    ('SAN FRANCISCO', 'CA'): (37.7749, -122.4194),
    ('CHICAGO', 'IL'): (41.8781, -87.6298),
    ('HOUSTON', 'TX'): (29.7604, -95.3698),
    ('PHOENIX', 'AZ'): (33.4484, -112.0740),
    ('PHILADELPHIA', 'PA'): (39.9526, -75.1652),
    ('BOSTON', 'MA'): (42.3601, -71.0589),
    ('MIAMI', 'FL'): (25.7617, -80.1918),
    ('SEATTLE', 'WA'): (47.6062, -122.3321),
    ('DENVER', 'CO'): (39.7392, -104.9903),
    ('WASHINGTON', 'DC'): (38.9072, -77.0369),
    ('ATLANTA', 'GA'): (33.7490, -84.3880),
    ('DALLAS', 'TX'): (32.7767, -96.7970),
    ('PORTLAND', 'OR'): (45.5152, -122.6784),
    ('SAN DIEGO', 'CA'): (32.7157, -117.1611),
    ('LAS VEGAS', 'NV'): (36.1699, -115.1398),
}

@app.route('/profile', methods=['GET', 'POST'])
@login_required
def profile():
    if request.method == 'POST':
        current_user.personal_name = request.form['personal_name']
        current_user.email = request.form['email']
        current_user.phone_number = request.form['phone_number']
        current_user.city = request.form['city']
        current_user.state = request.form['state']
        
        # Automatically get coordinates from city and state
        if current_user.city and current_user.state:
            city_key = (current_user.city.upper(), current_user.state.upper())
            
            if city_key in CITY_COORDINATES:
                current_user.latitude, current_user.longitude = CITY_COORDINATES[city_key]
                flash('Profile and location updated successfully!')
            else:
                # Try to use a geocoding service as fallback
                try:
                    # Use nominatim with proper delay and user agent
                    import time
                    time.sleep(1)  # Be respectful with rate limiting
                    geocode_url = "https://nominatim.openstreetmap.org/search"
                    params = {
                        'q': f"{current_user.city}, {current_user.state}, USA",
                        'format': 'json',
                        'limit': 1
                    }
                    headers = {
                        'User-Agent': 'Flask-Library-App/1.0 (Educational Project)'
                    }
                    
                    response = requests.get(geocode_url, params=params, headers=headers, timeout=10)
                    
                    if response.status_code == 200:
                        data = response.json()
                        if data and len(data) > 0:
                            current_user.latitude = float(data[0]['lat'])
                            current_user.longitude = float(data[0]['lon'])
                            flash('Profile and location updated successfully!')
                        else:
                            flash('Profile updated, but could not find coordinates. Try a major city name.')
                    else:
                        flash('Profile updated, but could not geocode location. Try a major city name.')
                except Exception as e:
                    flash('Profile updated, but error finding location. Try a major city from the list.')
        else:
            flash('Profile updated successfully!')
        
        db.session.commit()
        return redirect(url_for('profile'))
    
    return render_template('profile.html', user=current_user)

@app.route('/about')
def about():
    return '<h1>About Page</h1><p>This is a simple Flask application.</p>'


# ==================== DEMO MODE ====================

DEMO_BOOKS = [
    {'title': 'The Hobbit', 'author': 'J.R.R. Tolkien', 'status': 'completed', 'rating': 5, 'genre': 'Fantasy'},
    {'title': 'Dune', 'author': 'Frank Herbert', 'status': 'reading', 'rating': None, 'genre': 'Science Fiction'},
    {'title': 'Foundation', 'author': 'Isaac Asimov', 'status': 'wishlist', 'rating': None, 'genre': 'Science Fiction'},
    {'title': '1984', 'author': 'George Orwell', 'status': 'wishlist', 'rating': None, 'genre': 'Dystopian'},
    {'title': 'Pride and Prejudice', 'author': 'Jane Austen', 'status': 'completed', 'rating': 4, 'genre': 'Romance'},
    {'title': 'The Great Gatsby', 'author': 'F. Scott Fitzgerald', 'status': 'completed', 'rating': 4, 'genre': 'Classic'},
    {'title': 'To Kill a Mockingbird', 'author': 'Harper Lee', 'status': 'reading', 'rating': None, 'genre': 'Classic'},
    {'title': 'The Catcher in the Rye', 'author': 'J.D. Salinger', 'status': 'wishlist', 'rating': None, 'genre': 'Classic'},
]


@app.route('/demo')
def demo_mode():
    """Enter demo mode with sample data"""
    session['demo_mode'] = True
    session['demo_books'] = DEMO_BOOKS.copy()
    flash('Welcome to demo mode! Explore the reading library features.')
    return redirect(url_for('reading_dashboard'))


@app.route('/demo/exit')
def exit_demo():
    """Exit demo mode"""
    session.pop('demo_mode', None)
    session.pop('demo_books', None)
    flash('You have exited demo mode.')
    return redirect(url_for('home'))


# ==================== WEATHER READING SCORE ====================

def calculate_reading_score(weather_data):
    """
    Calculate 0-100 score for reading conditions.
    Higher score = better conditions for indoor reading.
    """
    score = 50
    reasons = []

    temp = weather_data.get('temperature', 70)
    forecast = weather_data.get('shortForecast', '').lower()
    is_daytime = weather_data.get('isDaytime', True)

    # Rain/snow = excellent reading weather
    if any(w in forecast for w in ['rain', 'snow', 'storm', 'shower', 'drizzle']):
        score += 25
        reasons.append("Perfect cozy reading weather!")

    # Cloudy = good
    if 'cloudy' in forecast or 'overcast' in forecast:
        score += 10
        reasons.append("Cloudy skies - good reading light")

    # Extreme temps = stay inside
    if temp < 40:
        score += 20
        reasons.append("Cold outside - perfect for indoor reading")
    elif temp > 95:
        score += 20
        reasons.append("Too hot outside - stay in with a book")
    # Nice weather = might want to be outside
    elif 65 <= temp <= 75 and ('sunny' in forecast or 'clear' in forecast):
        score -= 15
        reasons.append("Beautiful day - consider reading outside!")

    # Evening bonus
    if not is_daytime:
        score += 10
        reasons.append("Evening - wind down with a book")

    # Cap the score
    final_score = max(0, min(100, score))

    # Determine emoji and class
    if final_score >= 70:
        emoji = "📚"
        score_class = "excellent"
        recommendation = "Perfect reading weather! Curl up with a good book."
    elif final_score >= 50:
        emoji = "📖"
        score_class = "good"
        recommendation = "Good conditions for some reading time."
    elif final_score >= 30:
        emoji = "🌤️"
        score_class = "fair"
        recommendation = "Mixed conditions - maybe a chapter or two?"
    else:
        emoji = "🌞"
        score_class = "poor"
        recommendation = "Beautiful day! Consider reading outside or doing outdoor activities."

    return {
        'score': final_score,
        'reasons': reasons,
        'emoji': emoji,
        'score_class': score_class,
        'recommendation': recommendation
    }


# ==================== READING LIBRARY ROUTES ====================

def get_user_books():
    """Get books for current user or demo mode"""
    if session.get('demo_mode'):
        return session.get('demo_books', [])
    elif current_user.is_authenticated:
        return UserBook.query.filter_by(user_id=current_user.id).all()
    return []


@app.route('/reading')
def reading_dashboard():
    """Main reading dashboard"""
    if not session.get('demo_mode') and not current_user.is_authenticated:
        flash('Please log in or try demo mode to access your reading library.')
        return redirect(url_for('login'))

    if session.get('demo_mode'):
        books = session.get('demo_books', [])
        wishlist = [b for b in books if b['status'] == 'wishlist']
        reading = [b for b in books if b['status'] == 'reading']
        completed = [b for b in books if b['status'] == 'completed']
    else:
        user_books = UserBook.query.filter_by(user_id=current_user.id).all()
        wishlist = [b for b in user_books if b.status == 'wishlist']
        reading = [b for b in user_books if b.status == 'reading']
        completed = [b for b in user_books if b.status == 'completed']

    return render_template('reading/dashboard.html',
                           wishlist=wishlist,
                           reading=reading,
                           completed=completed,
                           demo_mode=session.get('demo_mode', False))


@app.route('/reading/wishlist')
def reading_wishlist():
    """View wishlist books"""
    if not session.get('demo_mode') and not current_user.is_authenticated:
        flash('Please log in or try demo mode.')
        return redirect(url_for('login'))

    if session.get('demo_mode'):
        books = [b for b in session.get('demo_books', []) if b['status'] == 'wishlist']
    else:
        books = UserBook.query.filter_by(user_id=current_user.id, status='wishlist').all()

    return render_template('reading/wishlist.html', books=books, demo_mode=session.get('demo_mode', False))


@app.route('/reading/completed')
def reading_completed():
    """View completed books"""
    if not session.get('demo_mode') and not current_user.is_authenticated:
        flash('Please log in or try demo mode.')
        return redirect(url_for('login'))

    if session.get('demo_mode'):
        books = [b for b in session.get('demo_books', []) if b['status'] == 'completed']
    else:
        books = UserBook.query.filter_by(user_id=current_user.id, status='completed').all()

    return render_template('reading/completed.html', books=books, demo_mode=session.get('demo_mode', False))


@app.route('/reading/add', methods=['GET', 'POST'])
def add_to_reading_list():
    """Add a book to the reading list"""
    if not session.get('demo_mode') and not current_user.is_authenticated:
        flash('Please log in or try demo mode.')
        return redirect(url_for('login'))

    if request.method == 'POST':
        title = request.form.get('title')
        author = request.form.get('author')
        status = request.form.get('status', 'wishlist')
        genre = request.form.get('genre')

        if session.get('demo_mode'):
            demo_books = session.get('demo_books', [])
            demo_books.append({
                'title': title,
                'author': author,
                'status': status,
                'rating': None,
                'genre': genre
            })
            session['demo_books'] = demo_books
            flash(f'"{title}" added to your {status} list!')
        else:
            user_book = UserBook(
                user_id=current_user.id,
                custom_title=title,
                custom_author=author,
                status=status,
                genre=genre
            )
            db.session.add(user_book)
            db.session.commit()
            flash(f'"{title}" added to your {status} list!')

        return redirect(url_for('reading_dashboard'))

    return render_template('reading/add_book.html', demo_mode=session.get('demo_mode', False))


@app.route('/reading/<int:book_id>/update', methods=['POST'])
def update_reading_status(book_id):
    """Update a book's status"""
    if not current_user.is_authenticated:
        flash('Please log in to update books.')
        return redirect(url_for('login'))

    new_status = request.form.get('status')
    user_book = UserBook.query.filter_by(id=book_id, user_id=current_user.id).first_or_404()

    user_book.status = new_status
    if new_status == 'reading' and not user_book.started_date:
        user_book.started_date = datetime.utcnow()
    elif new_status == 'completed' and not user_book.completed_date:
        user_book.completed_date = datetime.utcnow()

    db.session.commit()
    flash(f'Book status updated to "{new_status}"!')
    return redirect(url_for('reading_dashboard'))


@app.route('/reading/<int:book_id>/rate', methods=['GET', 'POST'])
def rate_book(book_id):
    """Rate and review a book"""
    if not current_user.is_authenticated:
        flash('Please log in to rate books.')
        return redirect(url_for('login'))

    user_book = UserBook.query.filter_by(id=book_id, user_id=current_user.id).first_or_404()

    if request.method == 'POST':
        rating = request.form.get('rating')
        review = request.form.get('review')

        if rating:
            user_book.rating = int(rating)
        user_book.review = review
        db.session.commit()
        flash('Your rating has been saved!')
        return redirect(url_for('reading_completed'))

    return render_template('reading/rate_book.html', book=user_book)


@app.route('/reading/<int:book_id>/delete', methods=['POST'])
def delete_from_reading_list(book_id):
    """Remove a book from reading list"""
    if not current_user.is_authenticated:
        flash('Please log in to manage your books.')
        return redirect(url_for('login'))

    user_book = UserBook.query.filter_by(id=book_id, user_id=current_user.id).first_or_404()
    title = user_book.title
    db.session.delete(user_book)
    db.session.commit()
    flash(f'"{title}" removed from your reading list.')
    return redirect(url_for('reading_dashboard'))


@app.route('/weather/recommendations')
def weather_recommendations():
    """Get book recommendations based on weather"""
    if not session.get('demo_mode') and not current_user.is_authenticated:
        flash('Please log in or try demo mode.')
        return redirect(url_for('login'))

    # Get weather data
    if current_user.is_authenticated and current_user.latitude and current_user.longitude:
        latitude = current_user.latitude
        longitude = current_user.longitude
        location_name = f"{current_user.city}, {current_user.state}"
    else:
        latitude = 40.7128
        longitude = -74.0060
        location_name = "New York City, NY (Default)"

    reading_score = None
    try:
        headers = {'User-Agent': '(Flask Weather App, contact@example.com)'}
        points_url = f'https://api.weather.gov/points/{latitude},{longitude}'
        points_response = requests.get(points_url, headers=headers, timeout=10)
        points_response.raise_for_status()
        forecast_url = points_response.json()['properties']['forecast']
        forecast_response = requests.get(forecast_url, headers=headers, timeout=10)
        forecast_response.raise_for_status()
        current_period = forecast_response.json()['properties']['periods'][0]
        reading_score = calculate_reading_score(current_period)
    except Exception:
        reading_score = {'score': 50, 'emoji': '📖', 'score_class': 'good',
                         'reasons': ['Unable to fetch weather data'],
                         'recommendation': 'Check the weather and find a good time to read!'}

    # Get user's wishlist for recommendations
    if session.get('demo_mode'):
        wishlist = [b for b in session.get('demo_books', []) if b['status'] == 'wishlist']
    else:
        wishlist = UserBook.query.filter_by(user_id=current_user.id, status='wishlist').all()

    return render_template('reading/recommendations.html',
                           reading_score=reading_score,
                           wishlist=wishlist,
                           location=location_name,
                           demo_mode=session.get('demo_mode', False))


if __name__ == '__main__':
    app.run(debug=True)
