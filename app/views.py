from app import app, db
from flask import render_template, request, redirect, url_for, flash
from .models import User as UserTBL, Events as EventsTBL, Schools as SchoolsTBL
from .forms import UserForm, EventForm, DistanceForm, NewDistanceForm, SchoolForm
from .extractor import fetch_data, cluster_data, get_schools

###
# Routing for your application.
###


@app.route('/')
def home():
    """Render website's home page."""
    return render_template('home.html')

@app.route('/schools')
def schools():
    schools = get_schools()
    return render_template('schools.html', schools=schools)

@app.route('/users')
def users():
    users = UserTBL.query.all()
    schools = []
    for user in users:
        school_id = user.school_id
        if school_id:
            school = SchoolsTBL.query.filter_by(id=school_id).first()
            schools.append(school.name)
        else:
            schools.append('None')
    results = list(zip(users, schools))
    
    return render_template('users.html', results=results)

@app.route('/events', methods=['post', 'get'])
def events():
    events = EventsTBL.query.all()
    new_distance_form = NewDistanceForm()
    if new_distance_form.validate_on_submit():
        distance = float(new_distance_form.distance.data)
        min_samples = new_distance_form.min_samples.data
        data = [event.entry for event in events]
        if data:
            clusters = cluster_data(data, min_samples, distance)
            print(clusters)
            return render_template('events.html', form=new_distance_form, events=events, clusters=clusters)

    return render_template('events.html', form=new_distance_form, events=events)

@app.route('/process-data', methods=['post', 'get'])
def process_data():
    new_distance_form = DistanceForm()
    if new_distance_form.validate_on_submit():
        file = new_distance_form.file.data
        distance = float(new_distance_form.distance.data)
        min_samples = new_distance_form.min_samples.data
        data = fetch_data(file)
        clusters = cluster_data(data, min_samples, distance)
        return render_template('process_data.html', form=new_distance_form, data=data, clusters=clusters)

    return render_template('process_data.html', form=new_distance_form)

@app.route('/schools/new', methods=['post', 'get'])
def new_school():
    new_school_form = SchoolForm()
    if new_school_form.validate_on_submit():
        name = new_school_form.name.data
        address = new_school_form.address.data
        phone = new_school_form.phone.data
        email = new_school_form.email.data

        school = SchoolsTBL(name, address, phone, email)
        db.session.add(school)
        db.session.commit()

        flash('School successfully added!', 'success')
        redirect(url_for('schools'))

    flash_errors(new_school_form)
    return render_template('add_school.html', form=new_school_form)

@app.route('/users/new', methods=['post', 'get'])
def new_user():
    new_user_form = UserForm()
    if new_user_form.validate_on_submit():
        school_id = new_user_form.school_id.data
        username = new_user_form.username.data
        first_name = new_user_form.first_name.data
        last_name = new_user_form.last_name.data
        email = new_user_form.email.data
        password = new_user_form.password.data

        print(school_id, username, first_name, last_name, email, password)
        user = UserTBL(school_id, username, first_name, last_name, email, password)
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
        entry = EventsTBL(event)
        db.session.add(entry)
        db.session.commit()
        flash('Message successfully added!', 'success')
        return redirect(url_for('events'))

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
