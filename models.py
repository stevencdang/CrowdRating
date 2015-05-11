#!/usr/bin/env python

# Author: Steven Dang stevencdang.com

# from main import login_manager
# from flask.ext.login import UserMixin, AnonymousUserMixin


# class Rater(AnonymousUserMixin):
    # """
    # An anonymous rating user
#
    # """
#
    # def __init__(self, name=None, type='Rater'):
        # self.name = name
        # self.type = type


class Rating:
    """
    A user submitted rating

    """
    def __init__(self, type, itemIDs, selection):
        self.type = type
        self.itemIDs = itemIDs
        self.selection = selection


class Item:
    """
    An item to be rated

    """
    def __init__(self, data):
        self.data = data


