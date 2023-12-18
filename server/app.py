import os
from flask import Flask, render_template, request, session, redirect
from flask_migrate import Migrate
from models import db
from database import create_table, insert_user, verify_credentials

app = Flask(__name__)

# Get the absolute path to the current directory
basedir = os.path.abspath(os.path.dirname(__file__))

# Set the path to the SQLite database file inside the 'database' folder
db_path = os.path.join(basedir, 'database', 'users.db')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + db_path

app.secret_key = 'your_secret_key'
db.init_app(app)

# Initialize Flask-Migrate
migrate = Migrate(app, db)

create_table()

@app.route('/')
def landing():
    return render_template('landing.html')

@app.route('/signup', methods=['POST'])
def signup():
    name = request.form.get('name')
    email = request.form.get('email')
    password = request.form.get('password')

    # Perform signup logic here
    insert_user(name, email, password)

    return redirect('/dashboard')

@app.route('/login', methods=['POST'])
def login():
    username = request.form.get('username')
    password = request.form.get('password')

    # Perform login logic here
    if verify_credentials(username, password):
        session['username'] = username
        return redirect('/dashboard')
    else:
        return redirect('/')

@app.route('/dashboard')
def dashboard():
    if 'username' in session:
        return render_template('dashboard.html', username=session['username'])
    else:
        return redirect('/')

@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)
