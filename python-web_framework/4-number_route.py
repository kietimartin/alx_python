"""importing flask module"""
from flask import Flask
"""create an instance"""
app = Flask(__name__)
"""route definitiion"""
@app.route('/', strict_slashes=False)
def hello_hbnb():
    return "Hello HBNB!"
"""/hbnb: display “HBNB”"""
@app.route('/hbnb', strict_slashes=False)
def hbnb():
    return "HBNB"

"""C is fun!"""
@app.route('/c/<text>', strict_slashes=False)
def show_c(text):
    return "C " + text.replace("_", " ")

"""Python is cool!"""
@app.route('/python/', defaults={'text': 'is cool'}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_text(text):
    return "Python " + text.replace("_", " ")

"""Is that a number"""
@app.route('/number/<int:n>', strict_slashes=False)
def this_is_a_number(n):
    if isinstance(n, int):
        return f"{n} is a number"
    else:
        pass 

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)