import os
from flask import Flask
from flask import jsonify
from flask import request
from dotenv import load_dotenv

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

@app.route("/get_env_var", methods = ["GET"])
def get_env_var():
    env_var_name = request.args.get('env_var_name')
    env_var_value = os.environ.get(env_var_name)
    return f"<p>Env var {env_var_name} = {env_var_value}</p>"

if __name__ == '__main__':
    load_dotenv()
    port = os.environ.get('PORT', 8080) # Heroku will set the PORT environment variable
    app.run(host = '0.0.0.0', port = port, debug = False) # Set debug to False before deployment
