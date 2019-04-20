from flask import Flask
from models import db

app = Flask(__name__)

def initdb():
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db/savedPosts.db'

    app.app_context().push()
    db.init_app(app)
    db.create_all()
    return app