from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/<string:specified>")
def headline_specified(specified):
    hl = specified.capitalize()
    return render_template("index.html", headline=hl)

@app.route("/array")
def arary_template():
    these = ["Ryu", "Emma", "Luka", "Hugo"]
    return render_template("array-handling.html", names=these)
