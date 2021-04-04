from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())

import os
from sqlalchemy import Column, String, Integer, create_engine
from flask_sqlalchemy import SQLAlchemy
import json

database_name = os.environ.get('database_name')
database_port = os.environ.get('database_port')
print(database_name)

database_path = 'postgres://{}/{}',format(database_port,database_name)