import redditScraper
from flask import Flask, render_template, request, redirect, url_for
#from models import db

app = Flask(__name__)

@app.route('/')
@app.route('/home', methods=['POST','GET'])
def home():
    searchQuery = None
    sortingMethod = "top"
    limit = 5
    if request.method == 'POST':
        if "newSubreddit" in request.form:
            redditScraper.changeSubreddit(request.form["newSubreddit"])
            searchQuery = "cool"
        else:
            searchQuery = request.form["searchQuery"]
            sortingMethod = request.form["sortingMethod"]

    else:
        searchQuery = "cool"
        #just render a default template

    return render_template("index.html", 
        queriedPosts=redditScraper.queryPosts(searchQuery, sortingMethod, limit), 
        searchQuery=searchQuery, 
        subreddit=redditScraper.subreddit,
        sortingMethod=sortingMethod
    )

""" @app.route('/save', methods=['POST'])
def saveToDB():
    #one database, user can put, post, get and delete for any posts
    #put will take the posts on the page and overwrite the entire db
    #post just keeps adding more """
