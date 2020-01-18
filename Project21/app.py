from flask import Flask, render_template

app = Flask(__name__)
@app.route('/')
def main():
    return render_template('index.html')

@app.route('/from/<direction>')
def direction(direction):
    return render_template('direction.html')

@app.route('/tours/<id>/')
def tour(id):
    return render_template('tour.html')

app.run()
