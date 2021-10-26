import os
from flask import Flask, jsonify, request

database_app = Flask(__name__)

@database_app.route("/api/database_app", methods = ['POST'])
def api_database_app():
    try:
        body = request.json['body']
        response = jsonify({'message': f'Body received successfully / Message from database_app.py - Dockerfile 2',
                            'received_body': body})
        response.status_code = 200
    except Exception as error:
        response = jsonify({'message': str(error).capitalize() + ' from database_app.py - Dockerfile 2'})
        response.status_code = 500
        print("Error: ", str(error))
    return response

@database_app.route("/test_database_app")
def test_database_app():
    return "<p>Hello World from Docker 2</p>"

if __name__ == '__main__':
    port = os.environ.get('PORT', 8081) # Heroku will set the PORT environment variable
    database_app.run(host = '0.0.0.0', port = port, debug = False) # Set debug to False before deployment
