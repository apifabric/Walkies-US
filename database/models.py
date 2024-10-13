# coding: utf-8
from sqlalchemy import DECIMAL, DateTime  # API Logic Server GenAI assist
from sqlalchemy import Column, DateTime, Float, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

########################################################################################################################
# Classes describing database for SqlAlchemy ORM, initially created by schema introspection.
#
# Alter this file per your database maintenance policy
#    See https://apilogicserver.github.io/Docs/Project-Rebuild/#rebuilding
#
# Created:  October 13, 2024 15:36:57
# Database: sqlite:////tmp/tmp.JnLp6xKH9T/Walkies-US/database/db.sqlite
# Dialect:  sqlite
#
# mypy: ignore-errors
########################################################################################################################
 
from database.system.SAFRSBaseX import SAFRSBaseX
from flask_login import UserMixin
import safrs, flask_sqlalchemy
from safrs import jsonapi_attr
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import relationship
from sqlalchemy.orm import Mapped
from sqlalchemy.sql.sqltypes import NullType
from typing import List

db = SQLAlchemy() 
Base = declarative_base()  # type: flask_sqlalchemy.model.DefaultMeta
metadata = Base.metadata

#NullType = db.String  # datatype fixup
#TIMESTAMP= db.TIMESTAMP

from sqlalchemy.dialects.sqlite import *



class Location(SAFRSBaseX, Base):
    """
    description: Represents a location for dog walking
    """
    __tablename__ = 'locations'
    _s_collection_name = 'Location'  # type: ignore
    __bind_key__ = 'None'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    address = Column(String)

    # parent relationships (access parent)

    # child relationships (access children)



class Owner(SAFRSBaseX, Base):
    """
    description: Represents a dog owner
    """
    __tablename__ = 'owners'
    _s_collection_name = 'Owner'  # type: ignore
    __bind_key__ = 'None'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    email = Column(String, unique=True)

    # parent relationships (access parent)

    # child relationships (access children)
    DogList : Mapped[List["Dog"]] = relationship(back_populates="owner")
    PaymentList : Mapped[List["Payment"]] = relationship(back_populates="owner")
    SubscriptionList : Mapped[List["Subscription"]] = relationship(back_populates="owner")
    AppointmentList : Mapped[List["Appointment"]] = relationship(back_populates="owner")
    FeedbackList : Mapped[List["Feedback"]] = relationship(back_populates="owner")



class Service(SAFRSBaseX, Base):
    """
    description: Represents different walking services offered
    """
    __tablename__ = 'services'
    _s_collection_name = 'Service'  # type: ignore
    __bind_key__ = 'None'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    price = Column(Float)

    # parent relationships (access parent)

    # child relationships (access children)
    SubscriptionList : Mapped[List["Subscription"]] = relationship(back_populates="service")
    WalkServiceList : Mapped[List["WalkService"]] = relationship(back_populates="service")



class Walker(SAFRSBaseX, Base):
    """
    description: Represents a dog walker
    """
    __tablename__ = 'walkers'
    _s_collection_name = 'Walker'  # type: ignore
    __bind_key__ = 'None'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    phone = Column(String)

    # parent relationships (access parent)

    # child relationships (access children)
    WalkerScheduleList : Mapped[List["WalkerSchedule"]] = relationship(back_populates="walker")
    WalkList : Mapped[List["Walk"]] = relationship(back_populates="walker")



class Dog(SAFRSBaseX, Base):
    """
    description: Represents a dog with details about its owner
    """
    __tablename__ = 'dogs'
    _s_collection_name = 'Dog'  # type: ignore
    __bind_key__ = 'None'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    breed = Column(String)
    owner_id = Column(ForeignKey('owners.id'))

    # parent relationships (access parent)
    owner : Mapped["Owner"] = relationship(back_populates=("DogList"))

    # child relationships (access children)
    AppointmentList : Mapped[List["Appointment"]] = relationship(back_populates="dog")
    WalkList : Mapped[List["Walk"]] = relationship(back_populates="dog")



class Payment(SAFRSBaseX, Base):
    """
    description: Represents a payment made for a service
    """
    __tablename__ = 'payments'
    _s_collection_name = 'Payment'  # type: ignore
    __bind_key__ = 'None'

    id = Column(Integer, primary_key=True)
    owner_id = Column(ForeignKey('owners.id'))
    amount = Column(Float)
    date = Column(DateTime)

    # parent relationships (access parent)
    owner : Mapped["Owner"] = relationship(back_populates=("PaymentList"))

    # child relationships (access children)



class Subscription(SAFRSBaseX, Base):
    """
    description: Represents a subscription plan for walking services
    """
    __tablename__ = 'subscriptions'
    _s_collection_name = 'Subscription'  # type: ignore
    __bind_key__ = 'None'

    id = Column(Integer, primary_key=True)
    owner_id = Column(ForeignKey('owners.id'))
    service_id = Column(ForeignKey('services.id'))
    start_date = Column(DateTime)
    end_date = Column(DateTime)

    # parent relationships (access parent)
    owner : Mapped["Owner"] = relationship(back_populates=("SubscriptionList"))
    service : Mapped["Service"] = relationship(back_populates=("SubscriptionList"))

    # child relationships (access children)



class WalkerSchedule(SAFRSBaseX, Base):
    """
    description: Represents a schedule for walkers
    """
    __tablename__ = 'walker_schedules'
    _s_collection_name = 'WalkerSchedule'  # type: ignore
    __bind_key__ = 'None'

    id = Column(Integer, primary_key=True)
    walker_id = Column(ForeignKey('walkers.id'))
    day_of_week = Column(String)
    start_time = Column(DateTime)
    end_time = Column(DateTime)

    # parent relationships (access parent)
    walker : Mapped["Walker"] = relationship(back_populates=("WalkerScheduleList"))

    # child relationships (access children)
    AppointmentList : Mapped[List["Appointment"]] = relationship(back_populates="schedule")



class Appointment(SAFRSBaseX, Base):
    """
    description: Represents a booked appointment for walking
    """
    __tablename__ = 'appointments'
    _s_collection_name = 'Appointment'  # type: ignore
    __bind_key__ = 'None'

    id = Column(Integer, primary_key=True)
    owner_id = Column(ForeignKey('owners.id'))
    dog_id = Column(ForeignKey('dogs.id'))
    schedule_id = Column(ForeignKey('walker_schedules.id'))

    # parent relationships (access parent)
    dog : Mapped["Dog"] = relationship(back_populates=("AppointmentList"))
    owner : Mapped["Owner"] = relationship(back_populates=("AppointmentList"))
    schedule : Mapped["WalkerSchedule"] = relationship(back_populates=("AppointmentList"))

    # child relationships (access children)



class Walk(SAFRSBaseX, Base):
    """
    description: Represents a walking session, tracks time and distance
    """
    __tablename__ = 'walks'
    _s_collection_name = 'Walk'  # type: ignore
    __bind_key__ = 'None'

    id = Column(Integer, primary_key=True)
    dog_id = Column(ForeignKey('dogs.id'))
    walker_id = Column(ForeignKey('walkers.id'))
    time = Column(DateTime)
    duration = Column(Integer)
    distance = Column(Float)

    # parent relationships (access parent)
    dog : Mapped["Dog"] = relationship(back_populates=("WalkList"))
    walker : Mapped["Walker"] = relationship(back_populates=("WalkList"))

    # child relationships (access children)
    FeedbackList : Mapped[List["Feedback"]] = relationship(back_populates="walk")
    WalkServiceList : Mapped[List["WalkService"]] = relationship(back_populates="walk")



class Feedback(SAFRSBaseX, Base):
    """
    description: Represents feedback for a walking session
    """
    __tablename__ = 'feedbacks'
    _s_collection_name = 'Feedback'  # type: ignore
    __bind_key__ = 'None'

    id = Column(Integer, primary_key=True)
    walk_id = Column(ForeignKey('walks.id'))
    owner_id = Column(ForeignKey('owners.id'))
    comments = Column(String)
    rating = Column(Integer)

    # parent relationships (access parent)
    owner : Mapped["Owner"] = relationship(back_populates=("FeedbackList"))
    walk : Mapped["Walk"] = relationship(back_populates=("FeedbackList"))

    # child relationships (access children)



class WalkService(SAFRSBaseX, Base):
    """
    description: Represents a walk associated with a particular service
    """
    __tablename__ = 'walk_services'
    _s_collection_name = 'WalkService'  # type: ignore
    __bind_key__ = 'None'

    id = Column(Integer, primary_key=True)
    walk_id = Column(ForeignKey('walks.id'))
    service_id = Column(ForeignKey('services.id'))

    # parent relationships (access parent)
    service : Mapped["Service"] = relationship(back_populates=("WalkServiceList"))
    walk : Mapped["Walk"] = relationship(back_populates=("WalkServiceList"))

    # child relationships (access children)
