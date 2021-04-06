from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())

import os
from sqlalchemy import Column, String, Integer, create_engine, DateTime
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import json

database_name = os.environ.get('database_name')
database_port = os.environ.get('database_port')
print(database_name)

database_path = 'postgres://{}/{}'.format(database_port,database_name)

db = SQLAlchemy()

class Movie(db.Model):
    __tablename__='movies'

    id = Column(Integer, primary_key=True)
    title = Column(String)
    release_date = Column(DateTime)

class Actor(db.Model):
    __tablename__='actors'

    id = Column(Integer, primary_key=True)

    name = Column(String)
    age = Column(Integer)
    gender = Column(String)