import pytest
import sys
import os
import bcrypt
from datetime import datetime, timedelta, timezone
from flask_bcrypt import Bcrypt

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app import app, db, User, Reservation

bcrypt = Bcrypt(app)
current_time = datetime.now(timezone.utc)

# Configure test environment
@pytest.fixture
def test_client():
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'  
    client = app.test_client()

    # Set up database
    with app.app_context():
        db.create_all()
    yield client
    with app.app_context():
        db.drop_all()

# Unit test example
def test_register_user(test_client):
    response = test_client.post('/register', data=dict(
        name='Test User',
        email='test@example.com',
        password='Testpassword123'
    ), follow_redirects=True)
    assert response.status_code == 200
    assert b'Registration successful!' in response.data

def test_user_registration_login_logout(test_client):
    # register
    response = test_client.post('/register', data=dict(
        name='Test User',
        email='test@example.com',
        password='Testpassword123'
    ), follow_redirects=True)
    assert response.status_code == 200
    assert b'Registration successful!' in response.data

    # login
    response = test_client.post('/login', data=dict(
        email='test@example.com',
        password='Testpassword123'
    ), follow_redirects=True)
    assert response.status_code == 200
    assert b'<title>Dashboard</title>' in response.data  

    # logout
    response = test_client.get('/logout', follow_redirects=True)
    assert response.status_code == 200
    assert b'Login' in response.data 


def test_make_reservation(test_client):
    # create an account
    hashed_password = bcrypt.generate_password_hash('Testpassword123').decode('utf-8')
    test_user = User(name='Test User', email='test@example.com', password=hashed_password)
    with app.app_context():
        db.session.add(test_user)
        db.session.commit()

    # login
    test_client.post('/login', data=dict(
        email='test@example.com',
        password='Testpassword123'
    ), follow_redirects=True)

    # Use tomorrow's date as the appointment date
    tomorrow = datetime.now().date() + timedelta(days=1)
    reservation_date = tomorrow.strftime('%Y-%m-%d')

    # Try to create an appointment
    response = test_client.post('/make_reservation', data=dict(
        restaurant_name='Test Restaurant',
        number_of_guest=2,
        reservation_date=reservation_date,  # Use tomorrow's date
        reservation_time='12:00'  # Use valid time
    ), follow_redirects=True)

    assert response.status_code == 200
    assert b'Appointment created successfully!' in response.data
