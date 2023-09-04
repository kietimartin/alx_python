#! /usr/bin/python3
"""
Basic Flask Web Server

This script creates a simple Flask web server that defines routes to handle various URLs.
- Root URL ("/") responds with a greeting message.
- "/hbnb" URL responds with "HBNB".
- "/c/<text>" URL responds with formatted text.
- "/python/<text>" URL responds with Python-related text (default value: "is cool").

This script requires Flask and markupsafe to be installed.

Author:
    Martin Kieti

Date:
    August 31, 2023
"""
from flask import Flask
from markupsafe import escape

app = Flask(__name__)

'''Defining the route'''
@app.route('/', strict_slashes=False)
def hello_hbnb():
    """
    Root URL Route
    
    Responds with a greeting message.
    """
    return 'Hello HBNB!'

'''Added new route'''
@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """
    /hbnb URL Route
    
    Responds with "HBNB".
    """
    return 'HBNB'

'''Adding a new route'''
@app.route('/c/<text>', strict_slashes=False)
def c_is_fun(text):
    """
    /c/<text> URL Route
    
    Responds with formatted text.
    
    Args:
        text (str): Text to be formatted.
    """
    return f'C {escape(text.replace("_", " "))}'

'''Adding a new python route'''
@app.route('/python/<text>',
           defaults={'text': 'is cool'}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_show_text(text):
    """
    /python/<text> URL Route
    
    Responds with Python-related text.
    
    Args:
        text (str): Text related to Python.
    """
    return f'Python {escape(text.replace("_", " "))}'

'''Starting the server'''
if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
