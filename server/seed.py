import sqlite3
from database import create_feedback_table, add_feedback
from models import db
from app import app

def seed_feedback_data():
    # Add your fake feedback entries here
    fake_feedback_data = [
        {"text": "Great job!", "likes": 5},
        {"text": "Excellent service.", "likes": 3},
        {"text": "The legal expertise of this law firm is truly impressive. They helped me navigate through a complex legal situation with ease.", "likes": 2},
        {"text": "I highly recommend this law firm for their professionalism and commitment to client success. Excellent service.", "likes": 8},
        {"text": "The attorneys here are knowledgeable and dedicated. They provided clear guidance and achieved a favorable outcome for my case.", "likes": 8},
        {"text": "If you are looking for a trustworthy legal partner, this law firm is the one. They prioritize client satisfaction and go the extra mile.", "likes": 8},
        {"text": "I am grateful for the support and legal assistance I received from this firm. Top-notch service and results!", "likes": 8},
        {"text": "Very professional team.", "likes": 8},
       
    
]
        # Add more fake feedback entries as needed

    # Create the feedbacks table (if not exists)
    create_feedback_table()

    # Add fake feedback entries to the database
    for feedback_entry in fake_feedback_data:
        add_feedback(feedback_entry["text"])

    print("Seed data added successfully.")

def seed_data():
    with app.app_context():

        db.create_all()


if __name__ == '__main__':
    seed_feedback_data()
    seed_data()
