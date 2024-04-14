from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from models import db, Users
import feedparser

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:shilpa@localhost/miniproj'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

def fetch_news(feed_url, num_articles):
    feed = feedparser.parse(feed_url)
    articles = []
    for entry in feed.entries[:num_articles]:
        articles.append({'title': entry.title, 'link': entry.link})
    return articles

@app.route('/login.html', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Check if the form is for login or sign up
        if 'signin' in request.form:
            # Login
            email = request.form['email']
            password = request.form['password']
            user = Users.query.filter_by(email=email).first()
            if user and check_password_hash(user.password, password):
                # Authentication successful, redirect to the home page
                return redirect(url_for('index'))
            else:
                # Authentication failed, render the login page with an error message
                return render_template('login.html', error='Invalid email or password')
        elif 'signup' in request.form:
            # Sign Up
            name = request.form['name']
            email = request.form['email']
            password = request.form['password']
            # Check if user already exists
            existing_user = Users.query.filter_by(email=email).first()
            if existing_user:
                return render_template('login.html', error='User already exists. Please login.')
            else:
                # Hash the password and add the user to the database
                hashed_password = generate_password_hash(password)
                new_user = Users(name=name, email=email, password=hashed_password)
                db.session.add(new_user)
                db.session.commit()
                # Redirect to login page after successful sign up
                return redirect(url_for('login'))
    # Render the login page for GET requests
    return render_template('login.html', error='')

@app.route('/latest_news')
def latest_news():
    # URL of the BBC News RSS feed
    NEWS_FEED_URL = "http://feeds.bbci.co.uk/news/world/asia/india/rss.xml"
    
    # Number of articles to display
    NUM_ARTICLES = 5
    
    articles = fetch_news(NEWS_FEED_URL, NUM_ARTICLES)
    
    return render_template('latest_news.html', articles=articles)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/cognitive_games.html')
def cognitive_games():
    return render_template('cognitive_games.html')

@app.route('/sudoku.html')
def sudoku():
    return render_template('sudoku.html')

@app.route('/cards.html')
def cards():
    return render_template('cards.html')

if __name__ == "__main__":
    app.run(debug=True)
