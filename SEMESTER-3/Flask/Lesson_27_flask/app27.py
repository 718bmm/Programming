import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy


basedir = os.path.abspath(os.path.dirname(__file__))
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///" + os.path.join(basedir, "myDB.db")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False # to supress warnings
db = SQLAlchemy(app)




class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), index=True, unique=True)
    author_name = db.Column(db.String(50), index=True, unique=False)
    author_surname = db.Column(db.String(80), index=True, unique=False)
    month = db.Column(db.String(20), index=True, unique=False)
    year = db.Column(db.Integer, index=True, unique=False)
    reviews = db.relationship("Review", backref="book", lazy="dynamic")
    annotations = db.relationship("Annotation", backref="book", lazy="dynamic")

    def __repr__(self):
        return "{} in: {},{}".format(self.title, self.month, self.year)


class Reader(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), index=True, unique=False)
    surname = db.Column(db.String(80), unique=False, index=True)
    email = db.Column(db.String(120), unique=True, index=True)
    reviews = db.relationship("Review", backref="reviewer", lazy="dynamic")
    annotations = db.relationship("Annotation", backref="author", lazy="dynamic")

    def __repr__(self):
        return "Reader ID: {}, email: {}".format(self.id, self.email)


class Review(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    stars = db.Column(db.Integer, unique=False)
    text = db.Column(db.String(200), unique=False)
    book_id = db.Column(db.Integer, db.ForeignKey("book.id"))
    reviewer_id = db.Column(db.Integer, db.ForeignKey("reader.id"))

    def __repr__(self):
        return "Review ID: {}, {} stars {}".format(self.id, self.stars, self.book_id)


class Annotation(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(200), unique=False)
    reviewer_id = db.Column(db.Integer, db.ForeignKey("reader.id"))
    book_id = db.Column(db.Integer, db.ForeignKey("book.id"))

    def __repr__(self):
        return "<Annotation {}-{}:{} >".format(
            self.reviewer_id, self.book_id, self.text
        )


with app.app_context():
    db.drop_all()
    db.create_all()

# ctx = app.app_context()
# ctx.push()
# db.create_all()
# ctx.pop()
