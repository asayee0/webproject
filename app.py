import redditScraper
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
@app.route('/home', methods=['POST','GET'])
def home():
    if request.method == 'POST':
        return render_template("index.html", queriedPosts=redditScraper.queryPosts(request.form['searchQuery']))
    else:
        return render_template("index.html", queriedPosts=redditScraper.queryPosts("cool"))

""" @app.route('/query', methods=['POST','GET'])
def query():
    queriedPosts = request.form['searchQuery']
    return render_template("index.html", queriedPosts=redditScraper.queryPosts(queriedPosts))
 """