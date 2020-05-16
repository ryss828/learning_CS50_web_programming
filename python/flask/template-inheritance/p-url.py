from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def f_main():
    return render_template("h-index.html")

@app.route("/u-more")
def f_more():
    return render_template("h-more.html")
