import os
import flask
# from flask.ext.pymongo import PyMongo


app = flask.Flask(__name__)


@app.route('/')
def index():
    return flask.render_template('home.html')


if __name__ == '__main__':
    app.debug = True
    app.run()
