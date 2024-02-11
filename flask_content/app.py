from flask import Flask, request, redirect, url_for, render_template, session, flash
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from datetime import datetime, timezone
import os

# Initialize Flask application
app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'

# Set the secret key and database configuration
app.secret_key = os.urandom(24)  # Generate a random key
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize database and bcrypt
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)

# users database
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(200))

# reservation database
class Reservation(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)  
    restaurant_name = db.Column(db.String(100), nullable=False)
    number_of_guest = db.Column(db.Integer, nullable=False)
    reservation_date = db.Column(db.Date, nullable=False)
    reservation_time = db.Column(db.Time, nullable=False)
    created_at = db.Column(db.DateTime, default=lambda: datetime.now(timezone.utc))


# register
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        password = request.form['password']

        existing_user = User.query.filter_by(email=email).first()
        if existing_user is None:
            hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')
            new_user = User(name=name, email=email, password=hashed_password)
            db.session.add(new_user)
            db.session.commit()
            flash('Registration successful!', 'success')
            return redirect(url_for('success'))  # to the success page
        else:
            flash('Email already registered.', 'error')

    return render_template('register.html')

# login
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        user = User.query.filter_by(email=email).first()
        if user and bcrypt.check_password_hash(user.password, password):
            session['user_id'] = user.id
            session['user_name'] = user.name
            flash('Login successful!', 'success')
            return redirect(url_for('dashboard'))  
        else:
            flash('Invalid email or password.', 'error')

    return render_template('login.html')

# exit
@app.route('/logout')
def logout():
    session.pop('user_id', None)
    session.pop('user_name', None)
    return redirect(url_for('login'))

# reservation
@app.route('/make_reservation', methods=['POST'])
def make_reservation():
    if 'user_id' not in session:
        return redirect(url_for('login'))  

    restaurant_name = request.form['restaurant_name']
    number_of_guest = int(request.form['number_of_guest'])
    if number_of_guest < 0:
        flash('Number of guests cannot be negative.', 'error')
        return redirect(url_for('dashboard'))

    reservation_date = datetime.strptime(request.form['reservation_date'], '%Y-%m-%d').date()
    reservation_time = datetime.strptime(request.form['reservation_time'], '%H:%M').time()

    current_datetime = datetime.now(timezone.utc)
    current_date = current_datetime.date()
    current_time = datetime.now(timezone.utc)


    # Check if the date is valid
    if reservation_date < current_date:
        flash('Appointment date must be today or a future date', 'error')
        return redirect(url_for('dashboard'))

    # Check if the time is valid
    if reservation_date == current_date and reservation_time < current_time:
        flash('Appointment time must be later than the current time', 'error')
        return redirect(url_for('dashboard'))

    # Create new reservation
    new_reservation = Reservation(
        user_id=session['user_id'],
        restaurant_name=restaurant_name,
        number_of_guest=number_of_guest,
        reservation_date=reservation_date,
        reservation_time=reservation_time
    )
    db.session.add(new_reservation)
    db.session.commit()

    flash('Appointment created successfully!', 'success')
    return redirect(url_for('dashboard'))

# dashboard
@app.route('/dashboard')
def dashboard():
    if 'user_id' not in session:
        return redirect(url_for('login'))  # if user is not login, return to the login page
    user_reservations = Reservation.query.filter_by(user_id=session['user_id']).all()
    return render_template('dashboard.html', name=session['user_name'], reservations=user_reservations)
    # display dashboard

@app.route('/coffee_drinks')
def coffee_drinks():
    return render_template('coffee_drinks.html')

@app.route('/restaurant')
def restaurant():
    return render_template('restaurant.html')

@app.route('/shop')
def shop():
    return render_template('shop.html')

@app.route('/speciality_foods')
def speciality_foods():
    return render_template('speciality_foods.html')


# success
@app.route('/success')
def success():
    return render_template('success.html')

# main page
@app.route('/')
def home():
    return redirect(url_for('login'))

# Main program entry
if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
