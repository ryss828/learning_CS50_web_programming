from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "Web server by Python flask"

@app.route("/<string:name>")
def greet(name):
    name = name.capitalize()
    return "<h1>Web server by Python flask: hello {}!</h1>".format(name)
