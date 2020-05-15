from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/<string:specified>")
def headline_specified(specified):
    hl = specified.capitalize()
    return render_template("index.html", headline=hl)
