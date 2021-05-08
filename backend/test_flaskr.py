from models import db, setup_db, Movie, Actor
from app import create_app
from flask_sqlalchemy import SQLAlchemy
import json
import unittest
import os
from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())


class MovieCastingTestCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app(test_config=True)
        self.client = self.app.test_client
        self.port = os.environ.get('database_port')
        self.database_name = "capstone_test"
        """Define test variables and initialize app."""
        self.database_path = 'postgresql://{}/{}'.format(self.port,self.database_name)
        setup_db(self.app, self.database_path)

        # binds the app to the current context
        with self.app.app_context():
            self.db = SQLAlchemy()
            self.db.init_app(self.app)
            # create all tables

        
        self.exec_header_one = {
            'Content-Type': 'application_json',
            'Authorization': os.environ['auth_token']
        }
        self.asst_header_one = {
            'Content-Type': 'application_json',
            'Authorization': os.environ['asst_token']
        }

    def tearDown(self):
        """Executed after each test"""
        pass


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

    def test_get_movies(self):
        res = self.client().get('/movies', headers=self.exec_header_one)
        self.assertEqual(res.status_code,200)

    def test_get_actors(self):
        res = self.client().get('/actors', headers=self.exec_header_one)
        data = json.loads(res.data)
        print(data)
        self.assertEqual(res.status_code,200)

    # For patch requests

    def test_update_actor(self):
        res = self.client().patch('actors/2', headers=self.exec_header_one, json={
            'name': 'Maddax Gomezz',
            'age': 3,
            'gender': "Male",
        })
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)

    # Delete Data

    def test_delete_actor(self):
        res = self.client().delete('/actors/1', headers=self.exec_header_one)
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)

    def test_delete_movie(self):
        res = self.client().delete('/movies/1', headers=self.exec_header_one)
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)

    def test_fail_delete_actor(self):
        res = self.client().delete('/actors/100', headers=self.exec_header_one)
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 422)
        self.assertEqual(data['success'], False)

    def test_fail_delete_movie(self):
        res = self.client().delete('/movies/100', headers=self.exec_header_one)
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 422)
        self.assertEqual(data['success'], False)




    








if __name__ == "__main__":
    unittest.main()