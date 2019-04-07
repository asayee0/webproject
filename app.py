import redditScraper
from flask import Flask, render_template, request, redirect, url_for
from models import db

app = Flask(__name__)

@app.route('/')
@app.route('/home', methods=['POST','GET'])
def home():
    if request.method == 'POST':
        searchQuery = request.form['searchQuery']
    else:
        searchQuery = "cool"
    return render_template("index.html", queriedPosts=redditScraper.queryPosts(searchQuery), searchQuery=searchQuery, subreddit=redditScraper.subreddit)

@app.route('/save', methods=['POST'])
def saveToDB():
    #one database, user can put, post, get and delete for any posts
    #put will take the posts on the page and overwrite the entire db
    #post just keeps adding more