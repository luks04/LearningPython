from flask import Blueprint, request, render_template

static_files = Blueprint('static_files', __name__)

@static_files.route('/show_static_files_working')
def show_static_files_working():
    return render_template("static.html")
