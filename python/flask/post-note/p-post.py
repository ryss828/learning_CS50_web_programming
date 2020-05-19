from flask import Flask, render_template, request

app = Flask(__name__)

notes = []

@app.route("/", methods=["GET","POST"])
def f_main():
    if request.method == "POST":
        user_note = request.form.get("user-note")
        notes.append(user_note)

    return render_template("h-posted.html", all_notes=notes)
