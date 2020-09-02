#!/usr/bin/python3
"""Script that starts a Flask web application"""
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
    return "C " + " ".join(text.split("_"))


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
