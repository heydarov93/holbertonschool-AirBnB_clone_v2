#!/usr/bin/python3
"""Script that starts a Flask web application"""
from models import storage
from models.state import State
from flask import Flask, render_template


app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route("/states_list")
def to_states_list():
    """Displays HTML page that shows list of states"""
    states_tmp = storage.all(State)
    states = []
    for obj in states_tmp.values():
        states.append(obj.to_dict())
    return render_template("7-states_list.html", states=states)


@app.teardown_appcontext
def close(exception):
    """Handles teardown_appcontext"""
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
