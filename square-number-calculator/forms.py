from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class QueryForm(FlaskForm):
    number = StringField("Enter number to be squared")
    submit = SubmitField("Calculate")