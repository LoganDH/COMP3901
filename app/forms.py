from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from wtforms.validators import InputRequired, Email

class UserForm(FlaskForm):
    username = StringField('Username', validators=[InputRequired()])
    first_name = StringField('First Name', validators=[InputRequired()])
    last_name = StringField('Last Name', validators=[InputRequired()])
    email = StringField('Email', validators=[InputRequired(), Email()])
    # password = PasswordField('Password', validators=[InputRequired()])

class EventForm(FlaskForm):
    event = StringField('Event', validators=[InputRequired()])

class SchoolForm(FlaskForm):
    name = StringField('School Name', validators=[InputRequired()])
    address = StringField('Address', validators=[InputRequired()])
    phone = StringField('Phone', validators=[InputRequired()])
    email = StringField('E-Mail', validators=[InputRequired(), Email()])