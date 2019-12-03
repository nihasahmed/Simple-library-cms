from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired
from wtforms.ext.sqlalchemy.fields import QuerySelectField
from app.models import Author


class BookForm(FlaskForm):
    author = SelectField('Author', coerce=int)
    title = StringField('Title', validators=[DataRequired()])
    submit = SubmitField('Submit')


class AuthorForm(FlaskForm):
    author = StringField('Author fullname', validators=[DataRequired()])
    submit = SubmitField('Submit')


class BookSearchForm(FlaskForm):
    author = StringField('Author')
    title = StringField('Title')
    submit = SubmitField('Search')