
from models import setup_db, Movie, Actor
from app import create_app
from flask_sqlalchemy import SQLAlchemy
import json
import unittest
import os
from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())

print(create_app)

class MovieCastingTestCase(unittest.TestCase):
    def setUp(self):
        database_port = os.environ.get('database_port')
        """Define test variables and initialize app."""
        self.app = create_app()
        self.client = self.app.test_client
        self.port = os.environ.get('database_port')
        self.database_name = os.environ.get('database_name')
        self.database_path = 'postgresql://{}/{}'.format(self.port,self.database_name)
        setup_db(self.app, self.database_path)

        # binds the app to the current context
        with self.app.app_context():
            self.db = SQLAlchemy()
        #     self.db.init_app(self.app)
            # create all tables
            # self.db.create_all()

    def tearDown(self):
        """Executed after reach test"""
        pass

    def test_get_movies(self):
        res = self.client().get('/movies')
 

        self.assertEqual(res.status_code,200)

    def test_get_actors(self):
        res = self.client().get('/actors')
 

        self.assertEqual(res.status_code,200)








if __name__ == "__main__":
    unittest.main()