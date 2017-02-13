import sqlite3
import bcrypt

db = sqlite3.connect('web/level1.sqlite')
cursor = db.cursor()
cursor.execute("""CREATE TABLE IF NOT EXISTS users (
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name TEXT NOT NULL UNIQUE, 
    password TEXT NOT NULL, 
    is_admin INTEGER NOT NULL)""")

users = [("admin", "x", 1),
         ("user", bcrypt.hashpw("password", bcrypt.gensalt()), 0)]
cursor.executemany("INSERT INTO users (name, password, is_admin) VALUES (?, ?, ?)", users)

cursor.execute("""CREATE TABLE IF NOT EXISTS comments (
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    user TEXT NOT NULL,
    content TEXT NOT NULL )""")

db.commit()
db.close()