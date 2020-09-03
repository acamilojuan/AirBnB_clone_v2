#!/usr/bin/python3
"""Script that starts a Flask web application"""
from flask import render_template
from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    """Method to start the Flask Web app"""
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """Method to start the Flask Web app"""
    return "HBNB"


@app.route('/c/<text>')
def cfun(text):
    """Method to start the Flask Web app"""
    return ("C {}".format(text.replace("_", " ")))


@app.route('/python/')
@app.route('/python/<text>')
def py(text="is cool"):
    return ("Python {}".format(text.replace("_", " ")))


@app.route('/number/<int:n>', strict_slashes=False)
def number(n):
    return str(n) + " is a number"


@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n=None):
    return render_template('5-number.html', n=n)


@app.route('/number_odd_or_even/', strict_slashes=False)
@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def odd_or_even(n=None):
    if n % 2 == 0:
        return render_template('6-number_odd_or_even.html', n=n, string='even')
    return render_template('6-number_odd_or_even.html', n=n, string="odd")


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
