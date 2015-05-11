from flask_wtf import Form
from wtforms import RadioField

class LikertRatingForm(Form):
    rating = RadioField(choices=[1,2,3,4,5,6,7]);
