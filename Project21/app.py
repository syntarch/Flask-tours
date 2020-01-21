from flask import Flask
from flask import render_template
from .tours_data import *
import random

departures = {"msk":"Из Москвы","spb":"Из Петербурга","nsk":"Из Новосибирска","ekb":"Из Екатеринбурга","kazan":"Из Казани"}


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
    from_city = departures[direction]

    return render_template('direction.html',
                           title=title,  departures=departures, pricelist=pricelist, duration_list=duration_list,
                           tours_from=tours_from, from_city=from_city)

@app.route('/tours/<int:id>/')
def tour(id):
    hotel = tours[id]
    direction = hotel['departure']
    from_city = departures[direction]
    return render_template('tour.html', title=title, departures=departures, hotel=hotel, from_city=from_city)


if __name__ == '__main__':
    app.run()

