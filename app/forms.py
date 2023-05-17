from app import app
from .extractor import get_datasets
from flask_wtf import FlaskForm
from wtforms import SelectField
from wtforms_sqlalchemy.fields import QuerySelectField
from app.models import Schools as SchoolsTBL  # Replace with your actual model
from wtforms import StringField, TextAreaField, DecimalField, IntegerField, PasswordField, SelectField
from wtforms.validators import InputRequired, Email

class UserForm(FlaskForm):
    def query_factory():
        with app.app_context():
            return SchoolsTBL.query.all()
    def get_pk(obj):
        return obj.id
    school_id = QuerySelectField('School', query_factory=query_factory, get_label='name', get_pk=get_pk, allow_blank=True, validators=[InputRequired()])
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