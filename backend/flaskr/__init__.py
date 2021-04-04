
import os
from flask import Flask, request, abort, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS


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

    return app
