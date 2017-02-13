from flask import Flask, render_template, request, redirect, url_for, session
from subprocess import call
import sqlite3
import bcrypt

DB_FILE = 'level1.sqlite'

app = Flask(__name__)
app.secret_key = 'ThisIsASecretKey'

@app.route('/')
def index():
    return render_template('level1/index.html')

@app.route('/login', methods=['POST'])
def login():
    db = sqlite3.connect(DB_FILE)
    db.text_factory = str
    cursor = db.cursor()
    cursor.execute("SELECT id, name, password, is_admin FROM users WHERE name='{0}'".format(request.form['username']))

    users = cursor.fetchall()

    if len(users) <= 0:
        return render_template('level1/login_fail.html', comment="Bad username")

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
        return render_template('level1/login_fail.html', comment="Bad password")

    return render_template('level1/login.html', name=first_user[1])

@app.route('/user', methods=['GET', 'POST'])
def user():
    if session['is_admin']:
        return redirect(url_for('admin'))
    if 'username' not in session:
        return redirect(url_for('/'))

    db = sqlite3.connect(DB_FILE)
    db.text_factory = str
    cursor = db.cursor()

    if request.method == 'POST':
        cursor.executescript("INSERT INTO comments (user, content) VALUES ('{0}', '{1}')".format(session['username'], request.form['comment']))

    cursor.execute("SELECT user, content FROM comments ORDER BY id ASC")

    comments = cursor.fetchall()

    return render_template('level1/user.html', comments=comments)

@app.route('/admin')
def admin():
    if not session['is_admin']:
        return redirect(url_for('user'))
    if 'username' not in session:
        return redirect(url_for('/'))

    call(["sudo", "systemctl", "restart", "box1_level2.service"])
    call(["sudo", "systemctl", "enable", "box1_level2.service"])
    
    return render_template('level1/admin.html', hostname=socket.gethostname(), port=1338)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=1337)