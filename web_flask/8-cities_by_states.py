#!/usr/bin/python3
"""Script that starts a Flask web application"""

from flask import Flask, render_template
from models import storage
from models.state import State


app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route("/cities_by_states")
def to_cities_by_state():
    """Displays HTML page that shows cities by states"""
    states = storage.all(State)
    cities_by_state = []

    for key, state in states.items():
        cities_by_state.append({
                                    "state": state,
                                    "cities": state.cities
                               })

    return render_template("8-cities_by_states.html", states=cities_by_state)


@app.teardown_appcontext
def close(exc):
    """Close session"""
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
