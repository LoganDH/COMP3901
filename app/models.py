from . import db
from werkzeug.security import generate_password_hash


class User(db.Model):
    # Uncomment the line below if you want to set your own table name
    # __tablename__ = "user_profiles"

    id = db.Column(db.Integer, primary_key=True)
    # school_id = db.Column(db.ForeignKey("schools.id"))
    username = db.Column(db.String(80), unique=True)
    first_name = db.Column(db.String(80))
    last_name = db.Column(db.String(80))
    email = db.Column(db.String(120), unique=True)
    password = db.Column(db.String(255))

    def __init__(self, username, first_name, last_name, email, password):
        self.username = username
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password = generate_password_hash(password)

    def __repr__(self):
        return '<User %r>' % self.username
    
class Schools(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), unique=True)
    address = db.Column(db.String(255), unique=True)
    phone = db.Column(db.String(15), unique=True)
    email = db.Column(db.String(120), unique=True)

    def __init__(self, name, address, phone, email):
        self.name = name
        self.address = address
        self.phone = phone
        self.email = email
    
    def __repr__(self):
        return '<School %r>' % self.name

class Events(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    # case_id = db.Column()
    date = db.Column(db.DateTime(timezone=True), server_default=db.func.now())
    entry = db.Column(db.String(500))
    # location = db.Column()
    # submitted_by = db.Column()
    # status = db.Column()

    def __init__(self, entry):
        self.entry = entry

    def __repr__(self):
        return '<Entry %r>' % self.entry