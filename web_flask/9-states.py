#!/usr/bin/python3
"""Script that starts a Flask web application"""

from models import storage
from models.state import State
from flask import Flask, render_template


app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route("/states")
@app.route("/states/<id>")
def to_states(id=None):
    """
    Fetchs states and cities by id
    then renders html page with that data
    """
    states_tmp = storage.all(State)
    state_by_id = None
    states = None

    if id:
        try:
            state = states_tmp[f"State.{id}"]
            state_by_id = state
        except KeyError:
            pass
    else:
        states = []
        for obj in states_tmp.values():
            states.append(obj)

    return render_template(
                            "9-states.html",
                            states=states,
                            single_state=state_by_id
                          )


@app.teardown_appcontext
def close(exc):
    """Closes session"""
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
