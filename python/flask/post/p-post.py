from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def f_main():
    return render_template("h-index.html")

@app.route("/u-post", methods=["post"])
def f_post():
    posted_name = request.form.get("username")
    return render_template("h-posted.html", name=posted_name)
