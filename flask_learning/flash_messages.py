import re
from flask import Blueprint,request, render_template
from flask.helpers import flash

flash_messages = Blueprint('flash_messages', __name__)

@flash_messages.route('/flashed_messages', methods = ['GET', 'POST'])
def login():
    if request.method == 'POST':
        password_form = request.form.get('password')
        if re.fullmatch(r'[A-Za-z0-9@#$%^&+=]{8,}', password_form):
            flash('Congrats, it is a secure password!')
        else:
            flash('Really? Too easy!')
            if len(password_form) == 0:
                flash('Also it is empty')
    return render_template('flash.html')
