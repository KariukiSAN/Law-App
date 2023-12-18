from models import db
from app import app

def seed_data():
    with app.app_context():

        db.create_all()


if __name__ == '__main__':
    seed_data()