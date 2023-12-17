import sqlite3
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData
from sqlalchemy_serializer import SerializerMixin
from datetime import datetime

metadata = MetaData(naming_convention={
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
})

db = SQLAlchemy(metadata=metadata)

class Message(db.Model, SerializerMixin):
    __tablename__ = 'messages'

    id = db.Column(db.Integer, primary_key=True)
    body=db.Column(db.String)
    username=db.Column(db.String)
    created_at=db.Column(db.DateTime ,default=datetime.utcnow)
    updated_at=db.Column(db.DateTime)

def create_table():
    # Connect to the database
    conn = sqlite3.connect('database/users.db')
    c = conn.cursor()

    # Create the users table if it doesn't exist
    c.execute('''CREATE TABLE IF NOT EXISTS users (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    username TEXT NOT NULL,
                    email TEXT NOT NULL,
                    password TEXT NOT NULL
                )''')

    # Commit the changes and close the connection
    conn.commit()
    conn.close()

def insert_user(username, email, password):
    # Connect to the database
    conn = sqlite3.connect('database/users.db')
    c = conn.cursor()

    # Generate a password hash
    password_hash = generate_password_hash(password)

    # Insert the user information into the users table
    c.execute("INSERT INTO users (username, email, password) VALUES (?, ?, ?)", (username, email, password_hash))

    # Commit the changes and close the connection
    conn.commit()
    conn.close()

def verify_credentials(username, password):
    # Connect to the database
    conn = sqlite3.connect('database/users.db')
    c = conn.cursor()

    # Query for the user with the given username
    c.execute("SELECT password FROM users WHERE username = ?", (username,))
    result = c.fetchone()

    if result:
        stored_password_hash = result[0]
        return check_password_hash(stored_password_hash, password)

    return False
