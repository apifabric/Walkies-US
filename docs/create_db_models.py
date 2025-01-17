import decimal

import logging



logging.getLogger('sqlalchemy.engine.Engine').disabled = True  # remove for additional logging

import sqlalchemy



from sqlalchemy.sql import func  # end imports from system/genai/create_db_models_inserts/create_db_models_prefix.py

from logic_bank.logic_bank import Rule

from sqlalchemy import create_engine, Column, Integer, String, DateTime, ForeignKey, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import datetime

# Establish a connection to the SQLite database
engine = create_engine('sqlite:///system/genai/temp/create_db_models.sqlite')
Base = declarative_base()
Session = sessionmaker(bind=engine)
session = Session()

class Owner(Base):
    """description: Represents a dog owner"""
    __tablename__ = 'owners'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    email = Column(String, unique=True)

class Dog(Base):
    """description: Represents a dog with details about its owner"""
    __tablename__ = 'dogs'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    breed = Column(String)
    owner_id = Column(Integer, ForeignKey('owners.id'))

class Walker(Base):
    """description: Represents a dog walker"""
    __tablename__ = 'walkers'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    phone = Column(String)

class Walk(Base):
    """description: Represents a walking session, tracks time and distance"""
    __tablename__ = 'walks'
    id = Column(Integer, primary_key=True, autoincrement=True)
    dog_id = Column(Integer, ForeignKey('dogs.id'))
    walker_id = Column(Integer, ForeignKey('walkers.id'))
    time = Column(DateTime, default=datetime.datetime.now)
    duration = Column(Integer)
    distance = Column(Float)

class Service(Base):
    """description: Represents different walking services offered"""
    __tablename__ = 'services'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    price = Column(Float)

class WalkService(Base):
    """description: Represents a walk associated with a particular service"""
    __tablename__ = 'walk_services'
    id = Column(Integer, primary_key=True, autoincrement=True)
    walk_id = Column(Integer, ForeignKey('walks.id'))
    service_id = Column(Integer, ForeignKey('services.id'))

class Location(Base):
    """description: Represents a location for dog walking"""
    __tablename__ = 'locations'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)
    address = Column(String)

class WalkerSchedule(Base):
    """description: Represents a schedule for walkers"""
    __tablename__ = 'walker_schedules'
    id = Column(Integer, primary_key=True, autoincrement=True)
    walker_id = Column(Integer, ForeignKey('walkers.id'))
    day_of_week = Column(String)
    start_time = Column(DateTime)
    end_time = Column(DateTime)

class Appointment(Base):
    """description: Represents a booked appointment for walking"""
    __tablename__ = 'appointments'
    id = Column(Integer, primary_key=True, autoincrement=True)
    owner_id = Column(Integer, ForeignKey('owners.id'))
    dog_id = Column(Integer, ForeignKey('dogs.id'))
    schedule_id = Column(Integer, ForeignKey('walker_schedules.id'))

class Payment(Base):
    """description: Represents a payment made for a service"""
    __tablename__ = 'payments'
    id = Column(Integer, primary_key=True, autoincrement=True)
    owner_id = Column(Integer, ForeignKey('owners.id'))
    amount = Column(Float)
    date = Column(DateTime, default=datetime.datetime.now)

class Feedback(Base):
    """description: Represents feedback for a walking session"""
    __tablename__ = 'feedbacks'
    id = Column(Integer, primary_key=True, autoincrement=True)
    walk_id = Column(Integer, ForeignKey('walks.id'))
    owner_id = Column(Integer, ForeignKey('owners.id'))
    comments = Column(String)
    rating = Column(Integer)

class Subscription(Base):
    """description: Represents a subscription plan for walking services"""
    __tablename__ = 'subscriptions'
    id = Column(Integer, primary_key=True, autoincrement=True)
    owner_id = Column(Integer, ForeignKey('owners.id'))
    service_id = Column(Integer, ForeignKey('services.id'))
    start_date = Column(DateTime, default=datetime.datetime.now)
    end_date = Column(DateTime)

# Create all tables
Base.metadata.create_all(engine)

# Insert sample data
# Owners
owner1 = Owner(name='John Doe', email='john@example.com')
owner2 = Owner(name='Jane Smith', email='jane@example.com')

# Dogs
dog1 = Dog(name='Rex', breed='German Shepherd', owner_id=1)
dog2 = Dog(name='Fido', breed='Labrador', owner_id=2)

# Walkers
walker1 = Walker(name='Alice', phone='555-1234')
walker2 = Walker(name='Bob', phone='555-5678')

# Walks
walk1 = Walk(dog_id=1, walker_id=1, duration=30, distance=3.2)
walk2 = Walk(dog_id=2, walker_id=2, duration=45, distance=4.1)

# Services
service1 = Service(name='Basic Walk', price=15.0)
service2 = Service(name='Extended Walk', price=25.0)

# WalkService
walk_service1 = WalkService(walk_id=1, service_id=1)

# Locations
location1 = Location(name='Central Park', address='Central Park, NY')
location2 = Location(name='Golden Gate Park', address='San Francisco, CA')

# WalkerSchedules
schedule1 = WalkerSchedule(walker_id=1, day_of_week='Monday', start_time=datetime.datetime.now(), end_time=datetime.datetime.now() + datetime.timedelta(hours=2))
schedule2 = WalkerSchedule(walker_id=2, day_of_week='Tuesday', start_time=datetime.datetime.now(), end_time=datetime.datetime.now() + datetime.timedelta(hours=3))

# Appointments
appointment1 = Appointment(owner_id=1, dog_id=1, schedule_id=1)

# Payments
payment1 = Payment(owner_id=1, amount=15.0, date=datetime.datetime.now())

# Feedbacks
feedback1 = Feedback(walk_id=1, owner_id=1, comments='Great service!', rating=5)

# Subscriptions
subscription1 = Subscription(owner_id=1, service_id=1, start_date=datetime.datetime.now(), end_date=datetime.datetime.now() + datetime.timedelta(days=30))

# Add all records to the session
session.add_all([
    owner1, owner2, dog1, dog2, walker1, walker2, walk1, walk2,
    service1, service2, walk_service1, location1, location2, 
    schedule1, schedule2, appointment1, payment1, feedback1, 
    subscription1
])

# Commit the session to the database
session.commit()

# Close the session
session.close()
