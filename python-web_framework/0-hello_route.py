from flask import Flask
# '''THis script displays a text when a certain page is opened on our 
# testing server on flask
# '''
app = Flask(__name__)

# Defining the route
@app.route('/', strict_slashes=False)
def hello():
    return 'Hello HBNB'

#  Starting the server
if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')