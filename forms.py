from flask_wtf import FlaskForm
from wtforms import StringField, SelectField
from wtforms.validators import DataRequired

class AddressForm(FlaskForm):
    validation_method = SelectField('Validation Method', choices=[('automatic', 'Automatic'), ('manual', 'Manual')])
    street_number = StringField('Street Number', validators=[DataRequired()])
    area = StringField('Area', validators=[DataRequired()])
