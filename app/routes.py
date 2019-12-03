from app import app, db
from app.forms import BookForm, AuthorForm, BookSearchForm
from app.models import Book, Author
from flask import render_template, flash, redirect, url_for
from sqlalchemy import or_,and_


@app.route('/')
@app.route('/index')
def index():
    books = Book.query.all()
    return render_template('index.html', title='Home', books=books)



@app.route('/createbook', methods=['GET', 'POST'])
def createbook():
    form = BookForm()
    form.author.choices =[(c.id, c.author) for c in Author.query.all()]
    if form.validate_on_submit():
        book = Book(author=form.author.data, title=form.title.data)
        db.session.add(book)
        db.session.commit()
        flash('Book by author {}, title {}'.format(
            form.author.data, form.title.data))
        return redirect(url_for('index'))
    return render_template('createbook.html', title='Create book', form=form)


@app.route('/createauthor', methods=['GET', 'POST'])
def createauthor():

    form = AuthorForm()
    if form.validate_on_submit():
        auth = Author(author=form.author.data)
        db.session.add(auth)
        db.session.commit()
        flash('Added author {}'.format(
            form.author.data))
        return redirect(url_for('index'))

    return render_template('createauthor.html', title='Create author', form=form)


@app.route('/search', methods=['GET', 'POST'])
def searchbook():

    form = BookSearchForm()
    books = 'unsearched'
    if form.validate_on_submit():
        print(form.author.data)
        books = Book.query.join(Author).filter(and_(Author.author.like('%'+form.author.data+'%'),Book.title.like('%'+form.title.data+'%'))).all()
        print(books)
    return render_template('searchbook.html', title='Search books', form=form, books=books)