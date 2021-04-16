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
        return jsonify({
            'success': 'Hello:World'
        })

    @app.route('/actors', methods=['DELETE'])
    def delete_actor():
        return jsonify({
            'success': 'Hello:World'
        })

    @app.route('/movies', methods=['DELETE'])
    def delete_movie():
        return jsonify({
            'success': 'Hello:World'
        })

    @app.route('/actors', methods=['PATCH'])
    def update_actor():
        return jsonify({
            'success': 'Hello:World'
        })

    @app.route('/movies', methods=['PATCH'])
    def update_movie():
        return jsonify({
            'success': 'Hello:World'
        })

    

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
