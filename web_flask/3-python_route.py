#!/usr/bin/python3
""" Script to add /python/<text> functionality """

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

    text = text.replace('_', ' ') if '_' in text else text

    return f'C {text}'


@app.route('/python/')
def print(text='is cool'):
    """ Printing python followed by the message """

    text = text.replace('_', ' ') if '_' in text else text

    return f'Python {text}'


if __name__ == '__main__':
    app.run(host='0.0.0.0')
