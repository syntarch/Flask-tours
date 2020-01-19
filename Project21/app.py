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
    tours_from = {}
    pricelist = []
    duration_list = []
    for tour_id, tour in tours.items():
        if tour['departure'] == direction:
            tours_from[tour_id] = tour
            pricelist += [tour['price']]
            duration_list += [tour['nights']]
    max_price, min_price = max(pricelist), min(pricelist)
    max_nights, min_nights = max(duration_list), min(duration_list)

    return render_template('direction.html', title=title, departures=departures, direction=direction,
                           max_price=max_price, min_price=min_price, max_nights=max_nights, min_nights=min_nights,
                           tours_from=tours_from)

@app.route('/tours/<id>/')
def tour(id):
    return render_template('tour.html', title=title, departures=departures)

app.run()
