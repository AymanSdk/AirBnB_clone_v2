#!/usr/bin/python3
"""
script starts Flask web app
    listen on 0.0.0.0 port 5000
    routes: /states_list: display HTML page
        /hbnb_filters: display HTML page
"""
from models import storage
from models import *
from flask import Flask, render_template
app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/')
def hello_hbnb():
    """display text"""
    return "Hello HBNB!"


@app.route('/hbnb')
def hbnb():
    """display text"""
    return "HBNB"


@app.route('/c/<text>')
def c_text(text):
    """display C + text"""
    return "C {}".format(text.replace('_', ' '))


@app.route('/python')
@app.route('/python/<text>')
def python_text(text='is cool'):
    """display Python + text"""
    return "Python {}".format(text.replace('_', ' '))


@app.route('/number/<int:n>')
def number(n):
    """display n is a number only if n is an integer"""
    return "{:d} is a number".format(n)