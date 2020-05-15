from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "web server by Python flask"

@app.route("/store")
def store():
    return "web server by Python flask: it's a store here"
