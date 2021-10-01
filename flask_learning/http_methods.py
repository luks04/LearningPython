from flask import Blueprint, request

http_methods = Blueprint('http_methods', __name__)

@http_methods.route('/login', methods = ['GET', 'POST'])
def login():
    if request.method == 'POST':
        headers = request.headers
        return f"do_the_login() with following headers: {headers}"
    else:
        return "show_the_login_form()"