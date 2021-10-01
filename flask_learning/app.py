from flask import Flask, render_template
from http_methods import http_methods
from url_building import url_building
from cookies import cookies
from static_files import static_files

app = Flask(__name__)
app.register_blueprint(http_methods)
app.register_blueprint(url_building)
app.register_blueprint(cookies)
app.register_blueprint(static_files)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/hello_world")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/hello/<name>/<city>/<int:id>")
def hello(name: str, city: str, id: int):
    return render_template("hello.html", name = name, city = city, id = id)

if __name__ == '__main__':
    app.run(host = '0.0.0.0', port = 5000, debug = True)