from flask import Flask, render_template
from model import db
from datetime import datetime
app = Flask(__name__)


@app.route("/")
def welcome():
    return render_template("welcome.html",message= " this the message from the view")


@app.route("/card")
def card_view():
    card = db[0]
    return render_template("cards.html",card=card)

@app.route("/date")
def date():
    return "This page as served at " + str(datetime.now())

# Please add: A page that shows how many times it has been visited


counter = 0
@app.route("/count_view")
def count_view():
    global counter
    counter += 1
    return "This page was viewed " + str(counter) + " times"