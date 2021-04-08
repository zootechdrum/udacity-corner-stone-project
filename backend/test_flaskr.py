
from models import setup_db, Question, Category
from flaskr import create_app
from flask_sqlalchemy import SQLAlchemy
import json
import unittest
import os
from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())


class MovieCastingTestCase(unittest.TestCase):
    """This class represents the trivia test case"""

    def setUp(self):
        database_port = os.environ.get('database_port')
        """Define test variables and initialize app."""
        self.app = create_app()
        self.client = self.app.test_client
        self.port = os.environ.get('database_port')
        self.database_name = os.environ.get('database_name')
        self.database_path = "postgres://{}/{}".format(
            self.port, self.database_name)
        setup_db(self.app, self.database_path)

        # binds the app to the current context
        with self.app.app_context():
            self.db = SQLAlchemy()
            self.db.init_app(self.app)
            # create all tables
            self.db.create_all()

    def tearDown(self):
        """Executed after reach test"""
        pass