import os
from flask import Flask, render_template, request, send_from_directory, session, redirect
from database import create_table, insert_user, verify_credentials

app = Flask(__name__)
#app = Flask(__name__, static_folder='static', template_folder='static/build')

#Need to discuss this
app.secret_key = 'your_secret_key'  # Set a secret key for session encryption. TBD

create_table()  # Call the create_table function to create the users table

# Defining the routes for login and signup pages
@app.route('/')
def landing():
    return render_template('landing.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        # Verify credentials against the stored user information in the database
        if verify_credentials(username, password):
            # User authentication succeeded
            session['username'] = username  # Store the username in the session
            return redirect('/dashboard')  # Redirect the user to the dashboard page
        else:
            # User authentication failed
            return "Invalid credentials. Please try again."
    else:
        return render_template('login.html')

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        


        
        insert_user(username, email, password)

        session['username'] = username  
        return redirect('/dashboard')  
    else:
        return render_template('signup.html')

@app.route('/dashboard')
def dashboard():
    return send_from_directory(os.path.join(app.static_folder, 'build'), 'index.html')

@app.route('/static/js/<path:filename>')
def serve_static(filename):
    return send_from_directory(os.path.join(app.static_folder, 'build', 'static', 'js'), filename)

if __name__ == '__main__':
    app.run(debug=True)


    