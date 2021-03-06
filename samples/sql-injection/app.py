from flask import Flask, render_template, request, redirect, url_for, session
import sqlite3
import bcrypt

app = Flask(__name__)
app.secret_key = 'ThisIsASecretKey'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['POST'])
def login():
    db = sqlite3.connect('database.sqlite')
    db.text_factory = str
    cursor = db.cursor()
    cursor.executescript("SELECT id, name, password, is_admin FROM users WHERE name='{0}'".format(request.form['username']))

    users = cursor.fetchall()

    if len(users) <= 0:
        return render_template('login_fail.html', comment="Bad username")

    first_user = users[0]
    (id, username, password, is_admin) = first_user

    if bcrypt.hashpw(request.form['password'].encode('utf-8'), password) == password:

        session['username'] = username
        session['is_admin'] = is_admin

        if is_admin:
            return redirect(url_for('admin'))
        else:
            return redirect(url_for('user'))
    else:
        return render_template('login_fail.html', comment="Bad password")

    return render_template('login.html', name=first_user[1])

@app.route('/user')
def user():
    if session['is_admin']:
        return redirect(url_for('admin'))
    if 'username' not in session:
        return redirect(url_for('/'))

    return render_template('user.html')

@app.route('/admin')
def admin():
    if not session['is_admin']:
        return redirect(url_for('user'))
    if 'username' not in session:
        return redirect(url_for('/'))

    return render_template('admin.html')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')