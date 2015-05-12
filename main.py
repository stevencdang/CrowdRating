#!/usr/bin/env python

# Author: Steven Dang stevencdang.com
# Copyright 2015

# from urlparse import urlsplit
import flask
import logging
import forms
import task_manager
from models import Rating
from flask.ext.pymongo import PyMongo
from flask import request
from db_params import ALL_DBs as DBS


logging.basicConfig(format='%(levelname)s:%(message)s',
                    level=logging.DEBUG)

logger = logging.getLogger("Main Routes")

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


@app.route('/')
def index():
    return flask.render_template('home.html')


@app.route('/rating/likert', methods=('GET', 'POST'))
def likert():
    form = forms.LikertRatingForm(csrf_enabled=False)
    # store the rating submitted
    if request.method == 'POST':
        score = request.form['rating']
        data_ID = request.form['data-id']
        rating = Rating('likert', data_ID, score)
        mongo.db['ratings'].insert(rating.__dict__)

    # Get the next idea to rate
    idea = mongo.db.ideas.find_one()
    idea = task_manager.get_random(mongo.db, 'ideas')
    logger.debug(idea)
    data = idea
    return flask.render_template('rating.html', form=form, data=data)



if __name__ == '__main__':
    app.debug = True
    app.run(host="0.0.0.0", port=5000)
    # mongo.db.create_collection("ratings")
