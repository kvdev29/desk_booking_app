from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from . import db

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=True, nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)
    
    role = db.Column(db.String(10), default='regular')  # ✅ Add this line
    is_admin = db.Column(db.Boolean, default=False)     # ✅ already there
    
    bookings = db.relationship('Booking', backref='user', lazy=True)



class Booking(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    location = db.Column(db.String(50), nullable=False)
    floor = db.Column(db.String(50), nullable=False)
    desk = db.Column(db.String(50), nullable=False)
    date = db.Column(db.Date, nullable=False)
    notes = db.Column(db.Text)
