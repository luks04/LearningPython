from flask import Blueprint, session, redirect, url_for, request, render_template, abort

auth = Blueprint('auth', __name__)

@auth.route('/login', methods = ['GET', 'POST'])
def login():
    if request.method == 'POST':
        username_form = request.form.get('username')
        if username_form == 'admin':
            session['username'] = username_form
            return redirect(url_for('auth.admin_index'))
        elif username_form == 'hacker':
            abort(401)
        return redirect(url_for('index'))
    return render_template('session.html')

@auth.route('/logout')
def logout():
    # Remove de username from session if it exists
    session.pop('username', None)
    return redirect(url_for('index'))

@auth.route('/admin_index')
def admin_index():
    return '<a href="/logout">Logout from admin_index...</a>'
