from app import db

class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    author = db.Column(db.Integer, db.ForeignKey('author.id'))
    title = db.Column(db.String(120))

    def __repr__(self):
        return '<book {}>'.format(self.title)


class Author(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    author = db.Column(db.String(120))
    books = db.relationship('Book', backref='workby', lazy='dynamic')

    def __repr__(self):
        return '<author {}>'.format(self.author)


