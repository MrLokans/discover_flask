import os
from flask import Flask, render_template, request, url_for, session, redirect

app = Flask(__name__)
app.config['SECRET_KEY'] = os.urandom(32)

USERNAME = 'admin'
PASSWORD = 'password'


@app.route('/')
def home():
    return "Hello, world"


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
            return redirect(url_for('home'))
    return render_template('login.html', error=error)


@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    return redirect(url_for('welcome'))

if __name__ == '__main__':
    app.run(debug=True)
