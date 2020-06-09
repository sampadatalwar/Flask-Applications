import datetime
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def birthday():
    today= datetime.datetime.now()
    isBirthday= today.month == 8 and today.day == 27
    return render_template("IsTodayBirthday.html", birthday=isBirthday)