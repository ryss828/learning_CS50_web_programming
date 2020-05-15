from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "web server by Python flask"

@app.route("/<string:name>")
def greet(name):
    return "web server by Python flask: hello {}".format(name)
