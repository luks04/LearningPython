from flask import Blueprint, session, redirect, url_for, request, render_template

auth = Blueprint('auth', __name__)

@auth.route('/login', methods = ['GET', 'POST'])
def login():
    if request.method == 'POST':
        session['username'] = request.form.get('username')
        return redirect(url_for('index'))
    return render_template('session.html')

@auth.route('/logout')
def logout():
    # Remove de username from session if it exists
    session.pop('username', None)
    return redirect(url_for('index'))
