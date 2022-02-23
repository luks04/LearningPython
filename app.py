from flask import Flask, session, render_template, redirect, url_for, request
from flask_learning.url_building import url_building
from flask_learning.cookies import cookies
from flask_learning.static_files import static_files
from flask_learning.auth import auth
from flask_learning.flash_messages import flash_messages
from flask_learning.db_api_example import db_api_example
import os
from werkzeug import *
from werkzeug.utils import secure_filename
from flask_mail import Mail, Message
from flask_learning.database import db

UPLOAD_FOLDER_PATH = r'/uploaded_files/'
ALLOWED_EXTENSIONS = {'txt', 'png', 'jpg', 'jpeg'} # Set

app = Flask(__name__)
app.register_blueprint(url_building)
app.register_blueprint(cookies)
app.register_blueprint(static_files)
app.register_blueprint(flash_messages)
app.register_blueprint(db_api_example)

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER_PATH
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////absolute/path/to/file.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'email@gmail.com'
app.config['MAIL_PASSWORD'] = '**********'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True

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
############################### FOR MAIL ###############################
########################################################################

mail = Mail(app)

@app.route("/send_mail/<mail_title>/<mail_content>")
def send_mail(mail_title: str, mail_content: str):
    msg = Message(mail_title, 
                  sender = app['MAIL_USERNAME'], 
                  recipients = ['example@gmail.com', 'example@outlook.com'])
    msg.body = mail_content
    mail.send(msg)
    return "Sending mail..."

########################################################################

@app.route("/hello_world")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/hello/<name>/<city>/<int:id>")
def hello(name: str, city: str, id: int):
    return render_template("hello.html", name = name, city = city, id = id)
