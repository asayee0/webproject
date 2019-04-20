from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Post(db.Model):
    databaseID = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(80), nullable=False)
    score = db.Column(db.Integer)
    redditID = db.Column(db.String(80))
    url = db.Column(db.String(300), nullable=False)
    comments = db.Column(db.String(40000))
    created = db.Column(db.String(80))
    body = db.Column(db.String(40000))
    media = db.Column(db.String(300))

    def __init__(self, title, score, id, url, comments, created, body, media):
        self.title = title
        self.score = score
        self.id = id
        self.url = url
        self.comments = comments
        self.created = created
        self.body = body
        self.media = media

    def toDict(self):
        return {
            "title" : self.title,
            "score" : self.score,
            "id" : self.id,
            "url" : self.url,
            "comments" : self.comments,
            "created" : self.created,
            "body" : self.body,
            "media" : self.media
        }

    def __repr__(self):
        return ('<Post Title %r> <URL %r>' % (self.title, self.url))
