from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField
from wtforms.validators import DataRequired

# Define the required fields in item form
class ItemForm(FlaskForm):
    name = StringField('name', validators=[DataRequired()])
    quantity = IntegerField('quantity', validators=[DataRequired(message="Enter a valid number")])
    description = StringField('description', validators=[DataRequired()])

