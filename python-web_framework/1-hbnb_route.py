#! /usr/bin/python3
'''Basic flask web server
-Creates a route on 0.0.0.0/5000
-Added new route '/hbnb'
'''
from flask import Flask

app = Flask(__name__)

'''Defining the route'''
@app.route('/', strict_slashes=False)
def hello_hbnb():
    return 'Hello HBNB!'

'''Added new route'''
@app.route('/hbnb', strict_slashes=False)
def hbnb():
    return 'HBNB'

'''Starting the server'''
if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')