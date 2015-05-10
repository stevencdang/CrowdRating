import os
from flask import Flask
from flask.ext.pymongo import PyMongo


app = Flask(__name__)


@app.route('/')
def index():
    return 'Hello World!'
