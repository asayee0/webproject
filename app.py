import redditScraper
from flask import Flask, render_template, request, redirect, url_for
import models
from models import Post
import init

app = init.app
db = models.db
init.initdb()

queriedPosts = None

@app.route('/')
@app.route('/home', methods=['POST','GET'])
def home():
    global queriedPosts
    searchQuery = ""
    sortingMethod = "top"
    limit = 5
    if request.method == 'POST':
        if "newSubreddit" in request.form:
            redditScraper.changeSubreddit(request.form["newSubreddit"])
        else:
            searchQuery = request.form["searchQuery"]
            sortingMethod = request.form["sortingMethod"]
            limit = int(request.form["limit"])
        queriedPosts=redditScraper.queryPosts(searchQuery, sortingMethod, limit)

    return render_template("index.html", 
        queriedPosts=queriedPosts, 
        searchQuery=searchQuery, 
        subreddit=redditScraper.subreddit,
        sortingMethod=sortingMethod
    )

@app.route("/savedPosts")
def dbInterface():
    posts = Post.query.order_by(Post.score).all()
    return render_template("savedPosts.html", posts=posts)

@app.route("/add", methods=["POST"])
def addAllToDB():
    global queriedPosts
    if request.method == "POST":
        for post in queriedPosts:
            postToSave = Post(post["title"], post["score"], post["id"], post["url"], post["comments"], post["created"], post["body"], post["media"])
            db.session.add(postToSave)
        db.session.commit()
    return redirect(url_for("dbInterface"))

@app.route("/add/<postID>", methods=["POST"])
def addToDB(postID):
    if request.method == "POST":
        post = None
        for p in queriedPosts:
            if p.get("id") == postID:
                post = p
                break
        postToSave = Post(post["title"], post["score"], post["id"], post["url"], post["comments"], post["created"], post["body"], post["media"])
        db.session.add(postToSave)
        db.session.commit()
    return redirect(url_for("home"))

@app.route("/deletePost/<postID>", methods=["POST"])
def deletePost(postID):
    if request.method == "POST":
        postToDelete = Post.query.filter_by(databaseID=postID).first()
        db.session.delete(postToDelete)
        db.session.commit()
    return redirect(url_for("dbInterface"))

@app.route("/deleteAll", methods=["POST"])
def deleteAllFromDB():
    if request.method == "POST":
        Post.query.delete()
        db.session.commit()
    return redirect(url_for("dbInterface"))