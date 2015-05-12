#!/usr/bin/env python

# Author: Steven Dang stevencdang.com
# Copyright 2015

import pymongo
import logging
import numpy


logging.basicConfig(format='%(levelname)s:%(message)s',
                    level=logging.DEBUG)

logger = logging.getLogger("Task Manager")

def get_random(db, collection, exclude=None):
    """
    Return a random element from the given collection with no
    likelihood of drawing an element with _id in exclude
    
    """
    if exclude is None:
        elms = db[collection].find()
    else:
        elms = db[collection].find({'_id': {'$nin': exclude}})
    
    num = elms.count()
    logger.debug("Number of items to choose from %d" % num)
    index = numpy.random.choice(num)
    logger.debug(elms[index])
    return elms[index]
