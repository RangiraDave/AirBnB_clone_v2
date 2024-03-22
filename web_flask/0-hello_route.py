#!/usr/bin/python3
# Script to start a simple Flask web app

from flask import Flask


app = Flask(__name__)
# app.url_map.strict_slashes = False


@app.route("/", strict_slashes = False)
def hello():
    """
    Function to return the message.
    """
    return "Hello HBNB!"


if __name__ == "__main__":
    app.run(host="0.0.0.0")
