
import os
from flask import Flask, request, abort, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from flask_migrate import Migrate

from models import db


def create_app(test_config=None):
    app = Flask(__name__)
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
        return jsonify({
            'success': 'Hello:World'
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
