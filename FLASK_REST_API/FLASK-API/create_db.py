# import app, db from app
from api import app, db

# create database
with app.app_context():
    db.create_all()
