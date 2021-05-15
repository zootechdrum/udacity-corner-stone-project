import json
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, String, Integer, create_engine, DateTime
import os
from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())


database_name = os.environ.get('database_name')
database_port = os.environ.get('database_port')

db = SQLAlchemy()

db_path = 'postgres://purdtfkuhaaelh:9975938a64a807937bb1852e8783ac7e701378ece60cfe5c329a9ae3fbec003e@ec2-52-21-153-207.compute-1.amazonaws.com:5432/d5rbjl44msl3mc'


def setup_db(app, database_path=db_path):
    app.config['SQLALCHEMY_DATABASE_URI'] = database_path
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.app = app
    db.init_app(app)
    # migrate = Migrate(app, db)
    db.create_all()


class Movie(db.Model):
    __tablename__ = 'movies'

    id = Column(Integer, primary_key=True)
    title = Column(String)
    release_date = Column(DateTime)

    def format(self):
        return {
            'id': self.id,
            'title': self.title,
            'release_date': self.release_date,
        }

    def insert(self):
        db.session.add(self)
        db.session.flush()
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def update(self):
        db.session.commit()


class Actor(db.Model):
    __tablename__ = 'actors'

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

    def update(self):
        db.session.commit()
