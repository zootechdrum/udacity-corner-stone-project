import os
from flask import Flask, request, abort, jsonify
import json
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from auth.auth import AuthError, requires_auth, check_permissions

from models import db, setup_db, Actor, Movie


def create_app(test_config=None):
    app = Flask(__name__)
    setup_db(app)
    cors = CORS(app, resources={r"/api/*": {"origins": "*"}})

    @app.after_request
    def after_request(response):
        response.headers.add(
            'Access-Control-Allow_Headers',
            'Content-Type,Authorization, true')
        response.headers.add(
            'Access-Control-Allow-Methods',
            'GET,PATCH,POST,DELETE,OPTIONS')
        return response

    @app.route('/actors', methods=['GET'])
    @requires_auth('get:actors')
    def actors(self):
        actors = Actor.query.all()

        formatted_actors = [actor.format() for actor in actors]
        return jsonify({
            'actors':formatted_actors,
            'success': True
        }), 200

    @app.route('/add_actor', methods=['POST'])
    @requires_auth('post:actor')
    def add_actor(self):

        body = request.get_json()
        error = False
        try:

            name = body['name']
            age = body['age']
            gender = body['gender']
            
            actor = Actor(
                name=name,
                age=age,
                gender=gender
            )
            db.session.add(actor)
            db.session.commit()
        except:
            error = True
            db.session.rollback()
        finally:
            db.session.close()

        if error:
            abort(422)
        else:
            return jsonify({
                'success': True,
                'message':'Actor was saved!'
                
                })

    @app.route('/add_movie', methods=['POST'])
    @requires_auth('post:movie')
    def add_movie(self):

        body = request.get_json()
        error = False
        try:

            title = body['title']
            release_date = body['release_date']
            
            movie = Movie(
                title=title,
                release_date=release_date,
            )
            db.session.add(movie)
            db.session.commit()
        except:
            error = True
            db.session.rollback()
        finally:
            db.session.close()

        if error:
            abort(422)
        else:
            return jsonify({
                'success': True,
                'message':'Movie has been added!'
            })

    @app.route('/movies', methods=['GET'])
    @requires_auth('get:movies')
    def movies(self):
        movies = Movie.query.all()
        formatted_movies = [movie.format() for movie in movies ]
        return jsonify({
            'success': True,
            'movies':formatted_movies
        })

    @app.route('/actors/<actor_id>', methods=['DELETE'])
    @requires_auth('delete:actor')
    def delete_actor(self,actor_id):
        actor = {}
        error = False
        try:
            actor = Actor.query.filter(
                Actor.id == actor_id).first()

            if actor is None:
                abort(404)

            actor.delete()
        except BaseException:
            error = True
            db.session.rollback()
        finally:
            db.session.close()
        if error:
            abort(422)
        else:           
            return jsonify({
                'success': True,
                'message':"Deleted an actor"
                }), 200

    @app.route('/movies/<movie_id>', methods=['DELETE'])
    @requires_auth('delete:movie')
    def delete_movie(self,movie_id):
        movie = {}
        error = False
        try:
            movie = Movie.query.filter(
                Movie.id == movie_id).first()

            if movie is None:
                abort(404)

            movie.delete()
        except BaseException:
            error = True
            db.session.rollback()
        finally:
            db.session.close()
        if error:
            abort(422)
        else:           
            return jsonify({
                'success': True,
                'message':"Deleted a movie"
                }), 200

    @app.route('/actors/<int:actor_id>', methods=['PATCH'])
    @requires_auth('patch:actor')
    def update_actor(self,actor_id):
        error = False

        try: 
            body = request.get_json()
            name = body['name']
            age = body['age']
            gender = body['gender']
            print(age)
            update_actor = Actor.query.filter(Actor.id == actor_id).one_or_none()

            if update_actor is None:
                abort(404)
            update_actor.name = name
            update_actor.age = age
            update_actor.gender = gender
            update_actor.update()


            return jsonify({
                'success': True,
                'message':"Updated actor successfuly"
            })
        except BaseException as e:
            print('BaseException is ',e )
            error = True
            db.session.rollback()
        finally:
            db.session.close()
        if error:
            abort(422)

    @app.route('/movies/<int:id>', methods=['PATCH'])
    @requires_auth('patch:movie')
    def update_movie(self, id):
        error = False
        try: 
            body = request.get_json()
            title = body['title']
            release_date = body['release_date']
            update_movie = Movie.query.filter(Movie.id == id).one_or_none()

            if update_movie is None:
                abort(404)

            update_movie.title = title
            update_actor.release_date = release_date
            update_movie.update()


            return jsonify({
                'success': True,
                'message':"Updated movie successfuly"
            })
        except BaseException:
            error = True
            db.session.rollback()
        finally:
            db.session.close()
        if error:
            abort(422)

    

    @app.errorhandler(404)
    def not_found(error):
        return jsonify({
            'success': False,
            'error': 404,
            'message': 'Resource Not Found'
        }), 404

    @app.errorhandler(422)
    def unable_to_process(error):
        print(error)
        return jsonify({
            'success': False,
            'error': 422,
            'message': 'Could not processs'
        }), 422

    @app.errorhandler(405)
    def method_not_allowed(error):
        return jsonify({
            'success': False,
            'error': 405,
            'message': 'Method not allowed'
        }), 405

    @app.errorhandler(400)
    def bad_request(error):
        return jsonify({
            'success': False,
            'error': 400,
            'message': 'Bad Request'
        }), 400
    
    return app

app = create_app(host='0.0.0.0', port=8080, debug=True)

if __name__ == '__main__':
    app.run()
