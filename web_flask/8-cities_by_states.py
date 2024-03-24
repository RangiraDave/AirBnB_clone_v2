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


@app.route('/cities_by_states')
def cities_by_states():
    """ Function to disaplay a HTML page with states """

    states = storage.all('State')
    # sorted_list = sorted(states, key=lambda state: state.name)

    return render_template('8-cities_by_states.html', states=states)


if __name__ == "__main__":
    app.run(host='0.0.0.0')
