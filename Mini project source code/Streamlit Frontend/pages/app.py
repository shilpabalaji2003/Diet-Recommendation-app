from flask import Flask, render_template, request, redirect, url_for
import feedparser
from flask import jsonify, send_from_directory
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

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

API_KEY = "AIzaSyB2TAC1-F6AzzDvuQQk-9rHSYKqUug29uE"

# Define a route to fetch health-related videos from YouTube API
@app.route('/thumbnails', methods=['GET'])
def search_videos():
    query = "Elderly Health"  # Your search query
    youtube = build('youtube', 'v3', developerKey=API_KEY)

    try:
        # Search for health-related videos
        search_response = youtube.search().list(
            q=query,
            part='snippet',
            type='video',
            maxResults=10  # Adjust the number of results as needed
        ).execute()

        # Extract video information
        videos = []
        for search_result in search_response.get('items', []):
            video = {
                'title': search_result['snippet']['title'],
                'thumbnail_url': search_result['snippet']['thumbnails']['default']['url'],
                'video_id': search_result['id']['videoId'],
                'channel_title': search_result['snippet']['channelTitle']
            }
            videos.append(video)

        return jsonify(videos)

    except HttpError as e:
        return jsonify({"error": f"An HTTP error occurred: {e.resp.status}, {e.content}"}), 500

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
