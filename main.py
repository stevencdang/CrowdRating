#!/usr/bin/env python

# Author: Steven Dang stevencdang.com

# from urlparse import urlsplit
import flask
from flask.ext.pymongo import PyMongo
from db_params import ALL_DBs as DBS


app = flask.Flask(__name__)
# Get the URL from the Heroku setting.
# url = os.environ.get('MONGOLAB_URI', db_params.get_url())
# Parse is
# parsed = urlsplit(url)
# The database name is derived from the path minus the leading /
# app.config['MONGODB_DATABASE'] = parsed.path[1:]

# if '@' in parsed.netloc:
    # If there are authentication details, split the network locality.
    # auth, server = parsed.netloc.split('@')
    # The username and password are in the first part, separated by a
    # :.
    # app.config['MONGODB_USERNAME'], app.config['MONGODB_PASSWORD'] = auth.split(':')
# else:
    # Otherwise the whole thing is the host and port.
    # server = parsed.netloc
    # Split whatever version of netloc we have left to get the host and
    # port.
    # app.config['MONGODB_HOST'], app.config['MONGODB_PORT'] = server.split(':')

app.config['MONGO_DBNAME'] = DBS['ideagensscd']['dbName']
app.config['MONGO_USERNAME'] = DBS['ideagensscd']['user']
app.config['MONGO_PASSWORD'] = DBS['ideagensscd']['pswd']
app.config['MONGO_HOST'] = DBS['ideagensscd']['url']
app.config['MONGO_PORT'] = DBS['ideagensscd']['port']
mongo = PyMongo(app)
# db = mongo.db


@app.route('/')
def index():
    prompt = mongo.db.prompts.find_one()
    question = prompt['question']

    return flask.render_template('home.html', question=question)


@app.route('/rating')
def rating():
    idea = mongo.db.ideas.find_one()
    data = idea['content']

    return flask.render_template('rating.html', data=data)


if __name__ == '__main__':
    app.debug = True
    app.run()
