from flask import Flask
from datetime import datetime
app = Flask(__name__)


@app.route("/")
def welcome():
    return "Welcome to my Flash Cards application!"


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