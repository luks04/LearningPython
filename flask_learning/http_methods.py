from flask import Blueprint, request

http_methods = Blueprint('http_methods', __name__)

@http_methods.route('/login', methods = ['GET', 'POST'])
def login():
    if request.method == 'POST':
        return "do_the_login()"
    else:
        return "show_the_login_form()"