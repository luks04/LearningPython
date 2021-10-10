from flask import Blueprint, request, jsonify
import sqlite3
from models.student import User
from database import db

db_api_example = Blueprint('db_api_example', __name__)

# Without SQLAlchemy
@db_api_example.route('/api/create_user', methods = ['POST'])
def create_user():
    new_name = request.json['name'] # Taked from body request
    new_phone = request.json['phone'] # Taked from body request
    try:
        '''
            HEADERS: {
                Content-Type: application/json
            }
        '''
        conn = sqlite3.connect("database_name")
        cursor = conn.cursor()
        query = f'''
                INSERT INTO users (name, phone)
                VALUES ({new_name}, {new_phone});
                '''
        print("Executing query...")
        cursor.execute(query)
        conn.commit()
        cursor.close()
        response = jsonify({'message': f'User {str(new_name)} created successfully'})
        response.status_code = 201
    except sqlite3.Error as error:
        response = jsonify({'message': str(error).capitalize()})
        response.status_code = 500
        conn.rollback()
        print("Error: ", str(error))
    finally:
        if(conn):
            conn.close()
            print("Sqlite connection is closed...")
    return response

# With SQLAlchemy
@db_api_example.route('/api/new_user', methods = ['POST'])
def new_user():
    new_name = request.json['name'] # Taked from body request
    new_phone = request.json['phone'] # Taked from body request
    try:
        if not new_name or not new_phone:
            return bad_request()
        new_user = User(new_name, new_phone)
        print(new_user.id)
        print(new_user.name)
        print(new_user.phone)
        db.session.add(new_user)
        db.session.commit()
        response = jsonify({'message': f'User {str(new_name)} created successfully'})
        response.status_code = 201
    except sqlite3.Error as error:
        response = jsonify({'message': str(error).capitalize()})
        response.status_code = 500
        print("Error: ", str(error))
    return response

@db_api_example.errorhandler(400)
def bad_request(error = None):
    response = jsonify({'message': f'Please enter all the fields'})
    response.status_code = 400
    return response