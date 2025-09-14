from flask import Blueprint, render_template, redirect, url_for, flash
from flask_login import login_required, current_user
from .models import Booking
from .forms import BookingForm
from . import db
from datetime import datetime

main = Blueprint('main', __name__)

@main.route('/')
def home():
    return render_template('home.html')

@main.route('/dashboard')
@login_required
def dashboard():
    bookings = Booking.query.filter_by(user_id=current_user.id).all()
    return render_template('dashboard.html', bookings=bookings)

@main.route('/admin/dashboard')
@login_required
def admin_dashboard():
    if not current_user.is_admin:
        flash("Access denied. Admins only.", "danger")
        return redirect(url_for('main.dashboard'))
    bookings = Booking.query.all()
    return render_template('admin_dashboard.html', bookings=bookings)

@main.route('/booking/new', methods=['GET', 'POST'])
@login_required
def create_booking():
    form = BookingForm()
    if form.validate_on_submit():
        existing = Booking.query.filter_by(
            date=form.date.data,
            location=form.location.data,
            floor=form.floor.data,
            desk=form.desk.data
        ).first()
        if existing:
            flash('Error: This desk is already booked for the selected date.', 'danger')
        else:
            booking = Booking(
                user_id=current_user.id,
                desk=form.desk.data,
                location=form.location.data,
                floor=form.floor.data,
                date=form.date.data,
                notes=form.notes.data
            )
            db.session.add(booking)
            db.session.commit()
            flash('Booking created successfully!', 'success')
            return redirect(url_for('main.dashboard'))
    return render_template('create_booking.html', form=form, now=datetime.now())

@main.route('/booking/update/<int:booking_id>', methods=['GET', 'POST'])
@login_required
def update_booking(booking_id):
    booking = Booking.query.get_or_404(booking_id)
    if not (current_user.is_admin or booking.user_id == current_user.id):
        flash("You are not authorized to edit this booking.", "danger")
        return redirect(url_for('main.dashboard'))

    form = BookingForm(obj=booking)
    if form.validate_on_submit():
        conflict = Booking.query.filter(
            Booking.id != booking.id,
            Booking.date == form.date.data,
            Booking.location == form.location.data,
            Booking.floor == form.floor.data,
            Booking.desk == form.desk.data
        ).first()
        if conflict:
            flash('Error: This desk is already booked for the selected date.', 'danger')
        else:
            booking.location = form.location.data
            booking.floor = form.floor.data
            booking.desk = form.desk.data
            booking.date = form.date.data
            booking.notes = form.notes.data
            db.session.commit()
            flash('Booking updated successfully!', 'success')
            return redirect(url_for('main.dashboard'))
    return render_template('update_booking.html', form=form, booking=booking)

@main.route('/booking/delete/<int:booking_id>', methods=['POST'])
@login_required
def delete_booking(booking_id):
    booking = Booking.query.get_or_404(booking_id)
    if booking.user_id != current_user.id and not current_user.is_admin:
        flash("Unauthorized deletion attempt.", "danger")
        return redirect(url_for('main.dashboard'))

    db.session.delete(booking)
    db.session.commit()
    flash("Booking deleted successfully.", "success")
    return redirect(url_for('main.admin_dashboard') if current_user.is_admin else url_for('main.dashboard'))
