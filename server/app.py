import os
from flask import Flask, render_template, request, send_from_directory, session, redirect
from database import create_table, insert_user, verify_credentials

app = Flask(__name__)
app.secret_key = 'your_secret_key'

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