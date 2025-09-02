from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, DateField, SelectField, TextAreaField
from wtforms.validators import DataRequired, Email, EqualTo, Length, Regexp, ValidationError
from datetime import date

class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[
        DataRequired(),
        Length(min=8),
        Regexp(r'^(?=.*[0-9])(?=.*[^A-Za-z0-9])', message="Password must include a number and a special character.")
    ])
    confirm = PasswordField('Confirm Password', validators=[
        DataRequired(),
        EqualTo('password', message='Passwords must match.')
    ])
    submit = SubmitField('Register')

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Login')

class BookingForm(FlaskForm):
    location = SelectField('Location', choices=[
        ('London', 'London'),
        ('Hove', 'Hove'),
        ('Cardiff', 'Cardiff')
    ], validators=[DataRequired()])

    floor = SelectField('Floor', choices=[
        ('1', 'Floor 1'),
        ('2', 'Floor 2'),
        ('3', 'Floor 3')
    ], validators=[DataRequired()])

    desk = SelectField('Desk', choices=[
        (f'Desk {i}', f'Desk {i}') for i in range(1, 101)
    ], validators=[DataRequired()])

    date = DateField('Date', format='%Y-%m-%d', validators=[DataRequired()])
    notes = TextAreaField('Additional Notes')
    submit = SubmitField('Submit Booking')

    def validate_date(self, field):
        if field.data < date.today():
            raise ValidationError("Booking date cannot be in the past.")
