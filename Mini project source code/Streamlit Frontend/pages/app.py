from flask import Flask, render_template
import feedparser

app = Flask(__name__)

def fetch_news(feed_url, num_articles):
    feed = feedparser.parse(feed_url)
    articles = []
    for entry in feed.entries[:num_articles]:
        articles.append({'title': entry.title, 'link': entry.link})
    return articles

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
