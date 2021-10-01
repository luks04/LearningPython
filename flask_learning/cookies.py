from flask import Blueprint, request, make_response, render_template

cookies = Blueprint('cookies', __name__)

# Reading cookies:
@cookies.route('/cookies_read')
def cookies_read():
    # use cookies.get(key) instead of cookies[key] to not get a KeyError if the cookie is missing.
    username = request.cookies.get('username')
    return f"Hi {username}"

# Storing cookies:
@cookies.route('/cookies_store/<name>')
def cookies_store(name: str):
    response = make_response(render_template('index.html'))
    response.set_cookie('username', name)
    return response