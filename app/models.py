from app import db


class Poster(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    id_poster = db.Column(db.String(10), unique=True, nullable=False)
    author = db.Column(db.String(30), unique=False, nullable=False)
    content = db.Column(db.String(120), unique=False, nullable=False)
