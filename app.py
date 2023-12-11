from flask import Flask, render_template, request, session, redirect
from database import create_table, insert_user, verify_credentials

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Set a secret key for session encryption. TBD

create_table()  # Call the create_table function to create the users table

# DefiNING the routes for login and signup pages
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
            return redirect('/')
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
        
        # Perform form validation and additional registration logic here
        # For example, check for unique usernames or password strength requirements

        # Insert the user information into the database
        insert_user(username, email, password)

        return "User registered successfully!"
    else:
        return render_template('signup.html')

if __name__ == '__main__':
    app.run(debug=True)