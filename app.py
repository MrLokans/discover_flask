import os
from functools import wraps

from flask import (
    Flask, g, flash, render_template, request,
    url_for, session, redirect
)

from flask.ext.sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config.from_object(os.environ.get('APP_SETTINS',
                                      'config.ProductionConfig'))

db = SQLAlchemy(app)

from models import *


USERNAME = 'admin'
PASSWORD = 'password'


def login_required(func):
    @wraps(func)
    def wrap(*args, **kwargs):
        if 'logged_in' in session:
            return func(*args, **kwargs)
        else:
            flash('Login required')
            return redirect(url_for('login'))
    return wrap


@app.route('/')
@login_required
def home():
    posts = db.session.query(BlogPost).all()
    return render_template('index.html', posts=posts)


@app.route('/welcome')
def welcome():
    return render_template("welcome.html")


@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        username = request.form.get('username', '')
        password = request.form.get('password', '')
        if username != USERNAME or password != PASSWORD:
            error = 'Invalid username'
        else:
            session['logged_in'] = True
            flash('Successfully logged in')
            return redirect(url_for('home'))
    return render_template('login.html', error=error)


@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    flash("Logged out.")
    return redirect(url_for('welcome'))


if __name__ == '__main__':
    app.run()
