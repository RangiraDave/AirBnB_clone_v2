#!/usr/bin/python3
"""
Python script that added
'/c/<text>: display “C ” followed by the value of the text variable'
functionality
"""

from flask import Flask


app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/')
def hello():
    """" Desplaying hello hbnb """

    return 'Hello HBNB!'

@app.route('/hbnb')
def hbnb():
    """ Desplaying HBNB """

    return 'HBNB'

@app.route('/c/<text>')
def c(text):
    """ Desplaying C with the following text """

    a.replace('_', ' ') if '_' in text else _

    return f'C is {text}'


if __name__ == '__main__':
    app.run(host='0.0.0.0')
