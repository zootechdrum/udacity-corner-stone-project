import os
from flask import Flask, request, abort, jsonify
import json
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS


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
    def actors():
        actors = Actor.query.all()

        formatted_actors = [actor.format() for actor in actors]
        print(formatted_actors)
        return jsonify({
            'actors':formatted_actors,
            'success': True
        }), 200

    @app.route('/add_actor', methods=['POST'])
    def add_actor():

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
    def add_movie():

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
    def movies():
        movies = Movie.query.all()
        formatted_movies = [movie.format() for movie in movies ]
        return jsonify({
            'success': True,
            'movies':formatted_movies
        })

    @app.route('/actors/<actor_id>', methods=['DELETE'])
    def delete_actor(actor_id):
        actor = {}
        error = False
        try:
            actor = Actor.query.filter(
                Actor.id == actor_id).first()

            if actor is None:
                abort(404)
                print(actor)
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
    def delete_movie(movie_id):
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

    @app.route('/actors/<int:id>', methods=['PATCH'])
    def update_actor(id):
        error = False

        try: 
            body = request.get_json()
            print(body)
            name = body['name']
            age = body['age']
            gender = body['gender']
            update_actor = Actor.query.filter(Actor.id == id).one_or_none()


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
        except BaseException:
            error = True
            db.session.rollback()
        finally:
            db.session.close()
        if error:
            abort(422)

    @app.route('/movies/<int:id>', methods=['PATCH'])
    def update_movie(id):
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
            print(update_movie)
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
