#!/usr/bin/python3
"""Start flask with c"""
from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    """Print Hello HBNB!"""
    return "Hello HBNB!"


@app.route('/hbnb')
def hbnb():
    """Print HBNB"""
    return "HBNB"


@app.route('/c/<text>')
def ctext(text):
    """Print C with text"""
    return "C {}".format(text.replace("_", " "))


if __name__ == '__main__':
    app.url_map.strict_slashes = False
    app.run(host='0.0.0.0', port=5000)
