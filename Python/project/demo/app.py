import json

from flask import Flask
from flask_cors import CORS
from book import Book

app = Flask(__name__)
CORS(app)


@app.route('/')
def hello_world():  # put application's code here
    harry = Book("Harry Potter", "JK")
    return json.dumps(harry.__dict__)


if __name__ == '__main__':
    app.run()
