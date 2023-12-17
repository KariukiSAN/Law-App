import os
from flask import Flask, render_template, request, send_from_directory, session, redirect
from database import create_table, insert_user, verify_credentials
from flask_cors import CORS
from flask_migrate import Migrate
from database import db, Message
from flask import Flask, request, make_response, jsonify

app = Flask(__name__)

app.secret_key = 'your_secret_key' 

create_table()  

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
            session['username'] = username  
            return redirect('/dashboard') 
        else:
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

CORS(app)
migrate = Migrate(app, db)

db.init_app(app)

@app.route('/messages/<int:id>', methods=['PATCH', 'DELETE'])
def messages_by_id(id):
    message = Message.query.filter_by(id=id).first()
    if request.method == 'PATCH':
        for attribute in request.json:
            setattr(message, attribute, request.json.get(attribute))
        db.session.commit()
        message_to_dict = message.to_dict() 
        response = jsonify(message_to_dict)
        response_body = make_response(response, 200)
        response_body.headers["Content-Type"] = "application/json"
        return response_body
    elif request.method == "DELETE":
        db.session.delete(message)
        db.session.commit()
        response_body = {'message': 'Delete was successful'}
        response = make_response(jsonify(response_body), 200)
        response.headers["Content-Type"] = "application/json"
        return response

@app.route('/messages', methods=['GET', 'POST'])
def get_messages():
    if request.method == 'GET':
        messages = Message.query.order_by(Message.created_at.asc()).all()
        messages_list = [{'id': msg.id, 'body': msg.body, 'created_at': msg.created_at, 'updated_at': msg.updated_at} for msg in messages]
        response = jsonify(messages_list)
        return make_response(response, 200)
    elif request.method == 'POST':
        new_message = Message(
            body=request.json.get("body"),
            username=request.json.get("username"),
            created_at=request.json.get("created_at"),
            updated_at=request.json.get("updated_at")
        )
        db.session.add(new_message)
        db.session.commit()
        new_message_to_dict = new_message.to_dict()
        response = jsonify(new_message_to_dict)
        return make_response(response, 200)

if __name__ == '__main__':
    app.run(port=5555)



    