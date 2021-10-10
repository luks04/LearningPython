from flask import Blueprint, url_for, redirect, abort, request, jsonify
from markupsafe import escape

url_building = Blueprint('url_building', __name__)

@url_building.route("/admin")
def hello_admin():
    return "Hello admin!"

@url_building.route("/guest/<guest>")
def hello_guest(guest: str):
    return f"Hello {escape(guest)} as guest!"

@url_building.route("/user/<name>")
def hello_user(name: str):
    if name == 'admin':
        return redirect(url_for('url_building.hello_admin'))
    elif name == 'hacker':
        return not_found()
    else:
        return redirect(url_for('url_building.hello_guest', guest = name))

@url_building.errorhandler(404)
def not_found(error = None):
    response = jsonify({
        'message': 'Resource not found ' + request.url
    })
    response.status_code = 404
    return response
