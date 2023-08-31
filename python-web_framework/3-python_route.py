#! /usr/bin/python3
'''Basic flask web server
-Creates a route on 0.0.0.0/5000
-Added new route '/hbnb'
-Added new route '/c/<text>'
-Added the python route
-Default value of text is "is cool"
'''
from flask import Flask
from markupsafe import escape

app = Flask(__name__)

'''Defining the route'''
@app.route('/', strict_slashes=False)
def hello_hbnb():
    return 'Hello HBNB!'

'''Added new route'''
@app.route('/hbnb', strict_slashes=False)
def hbnb():
    return 'HBNB'

'''Adding a new route'''
@app.route('/c/<text>', strict_slashes=False)
def c_is_fun(text):
    return f'C {escape(text.replace("_", " "))}'

'''Adding a new python route'''
@app.route('/python/<text>', strict_slashes=False)
def python_show_text(text):
    return f'Python {escape(text.replace("_", " "))}'

'''Starting the server'''
if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')