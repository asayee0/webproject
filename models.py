from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db/anime.db'
db = SQLAlchemy()

def initdb():
    app.app_context().push()
    db.init_app(app)
    db.create_all()
    return app

class Post(db.Model):
    title = db.Column(db.String(80), nullable=False)
    score = db.Column(db.Integer)
    id = db.Column(db.String(80), primary_key=True)
    url = db.Column(db.String(300), nullable=False)
    comments = db.Column(db.String(40000))
    created = db.Column(db.String(80))
    body = db.Column(db.String(40000))
    media = db.Column(db.String(300))

    def __init__(self, username, email):
        self.title = title
        self.score = score
        self.id = id
        self.url = url
        self.comments = comments
        self.created = created
        self.body = body
        self.media = media

    def __repr__(self):
        return ('<Post Title %r> <URL %r>' % (self.title, self.url))
