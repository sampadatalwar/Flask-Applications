from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def introduction():
    return render_template("introduction.html")