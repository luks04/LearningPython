from flask import Flask, session, render_template, redirect, url_for, request
from url_building import url_building
from cookies import cookies
from static_files import static_files
from auth import auth
from flash_messages import flash_messages
import os
from werkzeug import *
from werkzeug.utils import secure_filename

UPLOAD_FOLDER_PATH = r'/uploaded_files/'
ALLOWED_EXTENSIONS = {'txt', 'png', 'jpg', 'jpeg'} # Set

app = Flask(__name__)
app.register_blueprint(url_building)
app.register_blueprint(cookies)
app.register_blueprint(static_files)
app.register_blueprint(flash_messages)

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER_PATH

########################################################################
############################# FOR SESSIONS #############################
########################################################################

# Random secure string
app.secret_key = 'r4nd0m_53cur3_57r1ng'
app.register_blueprint(auth)

@app.route("/")
def index():
    if 'username' in session:
        username = session['username']
        if username == 'admin':
            return redirect(url_for('auth.admin_index'))
        return f'<h2>Logged in as {username}</h2><br/>' + \
                '<b><a href="/logout">Click here to logout</a></b>'
    return f'<h2>You are not logged in</h2><br/>' + \
            '<b><a href="/login">Click here to login</a></b>'

########################################################################
########################### FOR FILE UPLOAD ############################
########################################################################

def allowed_file(filename) -> bool:
    return '.' in filename and \
        filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/upload')
def upload():
    print(type(ALLOWED_EXTENSIONS))
    return render_template('upload.html')

@app.route('/uploader', methods = ['GET', 'POST'])
def uploader():
    if request.method == 'POST':
        file = request.files['myfile']
        filename = secure_filename(file.filename)
        if file and allowed_file(filename):
            file.save(os.getcwd() + app.config['UPLOAD_FOLDER'] + filename)
            return 'File uploaded successfully!'

########################################################################

@app.route("/hello_world")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/hello/<name>/<city>/<int:id>")
def hello(name: str, city: str, id: int):
    return render_template("hello.html", name = name, city = city, id = id)

if __name__ == '__main__':
    app.run(host = '0.0.0.0', port = 5000, debug = True)