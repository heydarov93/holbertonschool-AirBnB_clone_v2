#!/usr/bin/python3
"""Script that starts a Flask web application"""
from flask import Flask, render_template


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


@app.route("/number/<int:n>")
def to_number(n):
    """Number page displays dynamic int"""
    return "{:d} is a number".format(n)


@app.route("/number_template/<int:n>")
def to_number_template(n):
    """Displays number html template"""
    return render_template("5-number.html", n=n)


@app.route("/number_odd_or_even/<int:n>")
def to_number_odd_even(n):
    """Renders html page that shows number coming
    from dynamic url whether is odd or is even"""
    return render_template("6-number_odd_or_even.html", n=n)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
