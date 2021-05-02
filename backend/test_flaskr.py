
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
        
        self.exec_header_one = {
            'Content-Type': 'application_json',
            'Authorization': os.environ['auth_token']
        }
        self.asst_header_one = {
            'Content-Type': 'application_json',
            'Authorization': os.environ['asst_token']
        }

    def tearDown(self):
        """Executed after reach test"""
        pass

    def test_get_movies(self):
        res = self.client().get('/movies', headers=self.exec_header_one)
        self.assertEqual(res.status_code,200)

    def test_get_actors(self):
        res = self.client().get('/actors', headers=self.exec_header_one)
        self.assertEqual(res.status_code,200)

    def test_add_actor(self):
        res = self.client().post('/add_actor', headers=self.exec_header_one, json={
            'name': 'Maddax Gomez',
            'age': 3,
            'gender': "Male",
        })
        # data = json.loads(res.data).json()
        # self.assertEqual(data['success'], True)
        self.assertEqual(res.status_code, 200)
    
    # SHould not add to db. Permissions are not correct. 
    def test_wrong_role_add_actor(self):
        res = self.client().post('/add_actor',headers=self.asst_header_one, json={
            'name': 'Maddax Gomez',
            'age': 3,
            'gender': "Male",
        })

        self.assertEqual(res.status_code, 401)

    def test_add_movie_with_apprvd_role(self):
        res = self.client().post('/add_movie', headers=self.exec_header_one, json={
            'title': 'cats',
            'release_date': '4-25-2021',
        })

        self.assertEqual(res.status_code, 200)

    def test_add_movie_with_wrong_role(self):
        res = self.client().post('/add_movie', headers=self.asst_header_one, json={
            'title': 'cats',
            'release_date': '4-25-2021',
        })

        self.assertEqual(res.status_code, 401)



    








if __name__ == "__main__":
    unittest.main()