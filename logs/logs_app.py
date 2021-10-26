import os
from flask import Flask, jsonify

logs_app = Flask(__name__)

@logs_app.route("/api/logs_app", methods = ['GET'])
def api_logs_app():
    try:
        response = jsonify({'message': f'Message from logs_app.py - Dockerfile 3'})
        response.status_code = 200
    except Exception as error:
        response = jsonify({'message': str(error).capitalize() + ' from logs_app.py - Dockerfile 3'})
        response.status_code = 500
        print("Error: ", str(error))
    return response

@logs_app.route("/test_logs_app")
def test_logs_app():
    return "<p>Hello World from Docker 3</p>"

if __name__ == '__main__':
    port = os.environ.get('PORT', 8082) # Heroku will set the PORT environment variable
    logs_app.run(host = '0.0.0.0', port = port, debug = False) # Set debug to False before deployment
