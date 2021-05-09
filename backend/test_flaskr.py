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
        self.database_path = 'postgresql://{}/{}'.format(
            self.port, self.database_name)
        setup_db(self.app, self.database_path)

        # binds the app to the current context
        with self.app.app_context():
            self.db = SQLAlchemy()
            self.db.init_app(self.app)
            # create all tables

        self.exec_header_one = {
            'Content-Type': 'application/json',
            'Authorization': os.environ['auth_token']
        }
        self.asst_header_one = {
            'Content-Type': 'application/json',
            'Authorization': os.environ['asst_token']
        }


        movie1 = Movie(
        title="test102",
        release_date="2021-05-12 19:40:01.918917"
        )
        movie2 = Movie(
        title="test102",
        release_date="2021-05-12 19:40:01.918917"
        )
        movie3 = Movie(
        title="test102",
        release_date="2021-05-12 19:40:01.918917"
        )
        movie1.insert()
        movie2.insert()
        movie3.insert()

        artist1 = Actor(
            name="Ban Jovi",
            age=24,
            gender="male"
        )
        artist2 = Actor(
            name="Ban Jovi",
            age=24,
            gender="male"
        )
        artist3 = Actor(
            name="Ban Jovi",
            age=24,
            gender="male"
        )
        artist1.insert()
        artist2.insert()
        artist3.insert()

    def tearDown(self):
        """Executed after each test"""
        pass

    def test_add_actor(self):
        res = self.client().post('/add_actor', headers=self.exec_header_one, json={
            'name': 'Maddax Gomez',
            'age': 3,
            'gender': "Male",
        })
        data = json.loads(res.data)
        self.assertEqual(data['success'], True)
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
        self.assertEqual(res.status_code,200)

    def test_update_actor(self):
        res = self.client().patch('/actors/2', headers=self.exec_header_one, json={
            "age":25,
            "gender":"Female",
            "name":"lus"
        })
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)

    def test_update_movie(self):
        res = self.client().patch('/movies/2', headers=self.exec_header_one, json={
            "title": "Maddax Gomez",
            "release_date": '01/01/2010',
        })
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)

    # Delete Data

    def test_delete_actor(self):
        res = self.client().delete('/actors/1', headers=self.exec_header_one)
        data = json.loads(res.data)
        print(Actor.query.filter(Actor.id == 1).one_or_none())
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)

    def test_delete_movie(self):
        res = self.client().delete('/movies/1', headers=self.exec_header_one)
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
    # For patch requests

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
