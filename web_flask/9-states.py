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


@app.route('/states')
def states():
    """ Function to disaplay a HTML page with states """

    states = storage.all('State')

    return render_template('9-states.html', states=states)


@app.route('/states/<id>')
def state_id(state_id):
    """ Function to render a HTML with state id """

    states = storage.all('State')
    if states.id == state_id:
        return render_template('9-state.html', states=states)
    else:
        return 'Not found!'


if __name__ == "__main__":
    app.run(host='0.0.0.0')
