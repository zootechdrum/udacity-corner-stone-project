from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())
import os
from sqlalchemy import Column, String, Integer, create_engine, DateTime
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import json



database_name = os.environ.get('database_name')
database_port = os.environ.get('database_port')

db = SQLAlchemy()

database_path = 'postgresql://{}/{}'.format(database_port,database_name)

def setup_db(app,database_name=database_path):
    app.config["SQLALCHEMY_DATABASE_URI"] = database_path
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.app = app
    db.init_app(app)
    migrate = Migrate(app, db)


class Movie(db.Model):
    __tablename__='movies'

    id = Column(Integer, primary_key=True)
    title = Column(String)
    release_date = Column(DateTime)

    def format(self):
        return {
            'id': self.id,
            'title': self.title,
            'release_date': self.release_date,
        }

    def delete(self):
        db.session.delete(self)
        db.session.commit()    

class Actor(db.Model):
    __tablename__='actors'

    id = Column(Integer, primary_key=True)

    name = Column(String)
    age = Column(Integer)
    gender = Column(String)


    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def insert(self):
        db.session.add(self)
        db.session.commit()

    def format(self):
        return {
            'id': self.id,
            'name': self.name,
            'age': self.age,
            'gender': self.gender
        }
        
    def delete(self):
        db.session.delete(self)
        db.session.commit()  