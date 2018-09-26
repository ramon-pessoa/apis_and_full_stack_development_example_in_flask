from flask import render_template
from app import app
from app.forms import LoginForm


@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Ramon'}
    posts = [
        {
            'author': {'username': 'user1'},
            'body': 'Body text 1'
        },
        {
            'author': {'username': 'user2'},
            'body': 'Body text 2'
        }
    ]
    return render_template('index.html', title='Home', user=user, posts=posts)


@app.route('/login')
def login():
    form = LoginForm()
    return render_template('login.html', title='Sign In', form=form)