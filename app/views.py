from app import app, db
from flask import render_template, request, redirect, url_for, flash
from .models import User, Events
from .forms import UserForm, EventForm


###
# Routing for your application.
###

@app.route('/')
def home():
    """Render website's home page."""
    return render_template('home.html')


@app.route('/about/')
def about():
    """Render the website's about page."""
    return render_template('about.html', name="LAMRtech's Capstone Project")

@app.route('/users')
def users():
    users = User.query.all()

    return render_template('users.html', users=users)

@app.route('/events')
def events():
    events = Events.query.all()

    return render_template('events.html', events=events)

@app.route('/users/new', methods=['post', 'get'])
def new_user():
    new_user_form = UserForm()
    if new_user_form.validate_on_submit():
        username = new_user_form.username.data
        email = new_user_form.email.data
        # password = new_user_form.password.data

        user = User(username, email) # , password
        db.session.add(user)
        db.session.commit()

        flash('User successfully added!', 'success')
        redirect(url_for('users'))

    flash_errors(new_user_form)
    return render_template('add_user.html', form=new_user_form)

@app.route('/events/new', methods=['post', 'get'])
def new_event():
    new_event_form = EventForm()
    if new_event_form.validate_on_submit():
        event = new_event_form.event.data

        entry = Events(event)
        db.session.add(entry)
        db.session.commit()

        flash('Message successfully added!', 'success')
        redirect(url_for('events'))

    flash_errors(new_event_form)
    return render_template('add_event.html', form=new_event_form)


###
# The functions below should be applicable to all Flask apps.
###

# Flash errors from the form if validation fails
def flash_errors(form):
    for field, errors in form.errors.items():
        for error in errors:
            flash(u"Error in the %s field - %s" % (
                getattr(form, field).label.text,
                error
            ), 'danger')

@app.route('/<file_name>.txt')
def send_text_file(file_name):
    """Send your static text file."""
    file_dot_text = file_name + '.txt'
    return app.send_static_file(file_dot_text)


@app.after_request
def add_header(response):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also tell the browser not to cache the rendered page. If we wanted
    to we could change max-age to 600 seconds which would be 10 minutes.
    """
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'public, max-age=0'
    return response


@app.errorhandler(404)
def page_not_found(error):
    """Custom 404 page."""
    return render_template('404.html'), 404