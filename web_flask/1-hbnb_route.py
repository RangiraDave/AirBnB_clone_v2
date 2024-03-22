#!/usr/bin/python3
"""
Python script to start flask web app that returns HBNB
"""

from flask import Flask


app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/')
def hello():
    """
    Function to print the mesage.
    """

    return 'Hello HBNB!'


@app.route('/hbnb')
def hbnb():
    """
    Function that displays the simple message.
    """

    return 'HBNB'


if __name__ == '__main__':
    app.run(host='0.0.0.0')
