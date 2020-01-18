from flask import Flask
from flask import render_template
from Project21.tours_data import *
import random


app = Flask(__name__)
@app.route('/')
def main():
    list = random.sample(range(1, len(tours)+1), 6)
    tours_shortlist = {}
    for x in list:
        tours_shortlist[x] = tours[x]
    return render_template('index.html',
                           title=title, departures=departures, subtitle=subtitle, description=description, tours=tours_shortlist)

@app.route('/from/<direction>')
def direction(direction):
    return render_template('direction.html')

@app.route('/tours/<id>/')
def tour(id):
    return render_template('tour.html', title=title, departures=departures)

app.run()
