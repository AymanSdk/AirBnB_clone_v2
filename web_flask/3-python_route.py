#!/usr/bin/python3
""" Script to starts a Flask application  on
port 5000 and add a new route /c/<text> """

from flask import Flask
app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/')
def hello_hbnb():
    """ Hello HBNB! """
    return "Hello HBNB!"


@app.route('/hbnb')
def hbnb():
    """ HBNB """
    return "HBNB"


@app.route('/c/<text>')
def c_text(text):
    """ C + text """
    return "C {}".format(text.replace('_', ' '))


@app.route('/python')
@app.route('/python/<text>')
def python_text(text='is cool'):
    """ Python + text
    first route: /python
    to ensure that text is set to “is cool” if the argument text is not passed
    """
    return "Python {}".format(text.replace('_', ' '))


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
