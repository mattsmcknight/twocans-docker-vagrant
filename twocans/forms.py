from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, TextAreaField
from wtforms.validators import (DataRequired, Regexp, ValidationError, Email,
                                Length, EqualTo)

from models import User, Post

Form = FlaskForm

def name_exists(form, field):
    if User.select().where(User.username == field.data).exists():
        raise ValidationError('User with that name already exists.')


def email_exists(form, field):
    if User.select().where(User.email == field.data).exists():
        raise ValidationError('User with that email already exists.')



class RegisterForm(Form):
    username = StringField(
        'Username',
        validators=[
            DataRequired(),
            Regexp(
                r'^[a-zA-Z0-9_]+$',
                message=("Username should be one word, letters, numbers, and "
                         "underscores only")
            ),
        name_exists
        ])
    email = StringField(
        'Email',
        validators=[DataRequired(),
            Email(),
            email_exists
            ])
    password = PasswordField(
        'Password',
        validators=[
        DataRequired(),
        Length(min=2),
        EqualTo('password2',message='Passwords must match')
        ])
    password2 = PasswordField(
        'confirm Password',
        validators=[DataRequired()]
    )


class LoginForm(Form):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])


class PostForm(Form):
    content = TextAreaField("What's Up?", validators=[DataRequired()])
