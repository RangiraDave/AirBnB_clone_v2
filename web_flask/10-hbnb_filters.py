#!/usr/bin/python3
""" Python script to start the Flask web app with /states_list route """

from flask import Flask, render_template
from models import storage


app = Flask(__name__)
app.url_map.strict_slashes = False


@app.teardown_appcontext
def teardown(exception):
    """ Function to clear the SQLAlchemy session """

    storage.close()


@app.route('/hbnb_filters')
def hbnb_filters():
    """ Function to render the templates to the index HTML. """

    states = storage.all('State')
    amenities = storage.all('Amenity')

    return render_template('10-hbnb_filters.html', states=states, amenities=amenities)


if __name__ == "__main__":
    app.run(host='0.0.0.0')
