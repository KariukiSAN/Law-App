import os
from flask import Flask, render_template, request, send_from_directory, session, redirect
from database import create_table, insert_user, verify_credentials

app = Flask(__name__)

# Get the absolute path to the current directory
basedir = os.path.abspath(os.path.dirname(__file__))

# Set the path to the SQLite database file inside the 'database' folder
db_path = os.path.join(basedir, 'database', 'users.db')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + db_path

app.secret_key = 'your_secret_key'

create_table()
create_feedback_table()

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

@app.route('/feedbacks', methods=['GET'])
def get_feedbacks_route():
    feedbacks = get_feedbacks()
    formatted_feedbacks = [
        {"id": feedback[0], "text": feedback[1], "likes": feedback[2]} for feedback in feedbacks
    ]
    return jsonify(formatted_feedbacks)

# New API endpoint to add new feedback
@app.route('/feedbacks', methods=['POST'])
def add_feedback_route():
    data = request.get_json()
    add_feedback(data.get('text'))
    return jsonify({"message": "Feedback added successfully"}), 201

@app.route('/feedbacks/<int:feedback_id>/like', methods=['PUT'])
def like_feedback_route(feedback_id):
    try:
        like_feedback(feedback_id)
        return jsonify({"message": "Feedback liked successfully"})
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    
    
if __name__ == '__main__':
    app.run(debug=True)
