from app import app
from .extractor import get_schools as get_schls, get_datasets
from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, DecimalField, IntegerField, PasswordField, SelectField
from wtforms.validators import InputRequired, Email

class UserForm(FlaskForm):
    def get_schools():
        with app.app_context():
            return([(school.id, school.name) for school in get_schls()])
    # For school_id, we should be using 'wtforms_sqlalchemy.QuerySelectField'
    # Due to time constraints we did not get to make that change.
    school_id = SelectField('School', choices=get_schools())
    username = StringField('Username', validators=[InputRequired()])
    first_name = StringField('First Name', validators=[InputRequired()])
    last_name = StringField('Last Name', validators=[InputRequired()])
    email = StringField('Email', validators=[InputRequired(), Email()])
    password = PasswordField('Password', validators=[InputRequired()])

class EventForm(FlaskForm):
    event = TextAreaField('Event', validators=[InputRequired()])

class SchoolForm(FlaskForm):
    name = StringField('School Name', validators=[InputRequired()])
    address = StringField('Address', validators=[InputRequired()])
    phone = StringField('Phone', validators=[InputRequired()])
    email = StringField('E-Mail', validators=[InputRequired(), Email()])

class DistanceForm(FlaskForm):
    file = SelectField('Select a File', choices=get_datasets())
    distance = DecimalField('Distance', places=2, rounding=None)
    min_samples = IntegerField('min_samples')

class NewDistanceForm(FlaskForm):
    distance = DecimalField('Distance', places=2, rounding=None)
    min_samples = IntegerField('min_samples')