import sqlite3
from werkzeug.security import generate_password_hash, check_password_hash

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

def create_feedback_table():
    conn = sqlite3.connect('database/feedbacks.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS feedbacks (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    text TEXT NOT NULL,
                    likes INTEGER DEFAULT 0
                )''')
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

def get_feedbacks():
    conn = sqlite3.connect('database/feedbacks.db')
    c = conn.cursor()
    c.execute("SELECT * FROM feedbacks")
    feedbacks = c.fetchall()
    conn.close()
    return feedbacks

def add_feedback(text):
    conn = sqlite3.connect('database/feedbacks.db')
    c = conn.cursor()
    c.execute("INSERT INTO feedbacks (text, likes) VALUES (?, ?)", (text, 0))
    conn.commit()
    conn.close()

def like_feedback(feedback_id):
    conn = sqlite3.connect('database/feedbacks.db')
    c = conn.cursor()
    c.execute("UPDATE feedbacks SET likes = likes + 1 WHERE id = ?", (feedback_id,))
    conn.commit()
    conn.close()
