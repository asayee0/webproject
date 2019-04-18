from flask import Flask
from models import db

def initdb():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db/savedPosts.db'

    app.app_context().push()
    db.init_app(app)
    db.create_all()
    return app