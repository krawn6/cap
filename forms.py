from flask_wtf import Flaskform
from wtforms import StringField

class KeywordForm(FlaskForm):
    kw = StringField('keyword')


