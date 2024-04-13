#!/usr/bin/python3
"""Script that starts a Flask web application"""

from flask import Flask


app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route("/")
def index():
    """Home page"""
    return "Hello HBNB!"


@app.route("/hbnb")
def to_hbnb():
    """Hbnb page"""
    return "HBNB"


@app.route("/c/<text>")
def to_ctext(text):
    """C/text page"""
    text = text.replace("_", " ")
    return "C {}".format(text)


@app.route("/python")
@app.route("/python/<text>")
def to_python_text(text="is cool"):
    """Python/text page"""
    text = text.replace("_", " ")
    return "Python {}".format(text)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
