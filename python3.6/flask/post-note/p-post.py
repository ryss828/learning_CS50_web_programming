from flask import Flask, render_template, request, session
from flask_session import Session

app = Flask(__name__)

app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

@app.route("/", methods=["GET","POST"])
def f_main():
    if session.get("notes") is None:
        session["notes"] = []
    if request.method == "POST":
        user_note = request.form.get("user-note")
        session["notes"].append(user_note)

    return render_template("h-posted.html", all_notes=session["notes"])
