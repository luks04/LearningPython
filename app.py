import os
from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/api/app", methods = ['GET'])
def api_app():
    try:
        response = jsonify({'message': f'Message from app.py - Dockerfile 1'})
        response.status_code = 200
    except Exception as error:
        response = jsonify({'message': str(error).capitalize() + ' from app.py - Dockerfile 1'})
        response.status_code = 500
        print("Error: ", str(error))
    return response

@app.route("/test_app")
def test_app():
    return "<p>Hello World from Docker 1</p>"

if __name__ == '__main__':
    port = os.environ.get('PORT', 8080) # Heroku will set the PORT environment variable
    app.run(host = '0.0.0.0', port = port, debug = False) # Set debug to False before deployment
