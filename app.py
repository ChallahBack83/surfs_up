#import dependency
from flask import Flask

#create new flask instance

app = Flask(__name__)

#create flask routes

@app.route('/')
def hello_world():
    return 'Hello world'
