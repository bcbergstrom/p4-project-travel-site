from sqlalchemy_serializer import SerializerMixin
from sqlalchemy.orm import validates, relationship
from sqlalchemy.ext.associationproxy import association_proxy
from config import db

class Activity(db.Model, SerializerMixin):
    __tablename__ = 'activities'
    
    id = db.Column(db.Integer, primary_key=True)
    budget = db.Column(db.Integer)
    adv_scale = db.Column(db.Integer)
    #a_o = alone or with others
    a_o = db.Column(db.Boolean)
    name = db.Column(db.String)
    desc = db.Column(db.String)
    
    vacations = relationship('Vacation', back_populates='activity', cascade ="all, delete-orphan")


class Vacation(db.Model, SerializerMixin):
    __tablename__ = 'vacations'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    activity_id = db.Column(db.Integer, db.ForeignKey('activities.id'))
    trip_id = db.Column(db.Integer, db.ForeignKey('trips.id'))
    user = relationship('User', back_populates = 'vacations', cascade ="all")
    activity = relationship('Activity', back_populates = 'vacations', cascade ="all")
    trip = relationship('Trip', back_populates= 'vacations', cascade ="all")

class User(db.Model, SerializerMixin):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    budget = db.Column(db.Float)
    a_o = db.Column(db.Boolean)
    password = db.Column(db.String)
    email = db.Column(db.String)

    luggages = relationship('Luggage', back_populates = 'user', cascade ="all, delete-orphan")
    vacations = relationship('Vacation', back_populates = 'user', cascade ="all, delete-orphan")


class Luggage(db.Model, SerializerMixin):
    __tablename__ = 'luggages'

    id = db.Column(db.Integer, primary_key=True)
    style_shirt = db.Column(db.Boolean)
    style_pants = db.Column(db.Boolean)
    style_accessories = db.Column(db.Boolean)
    is_summer = db.Column(db.Boolean)

    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    user = relationship('User', back_populates = 'luggages')

class Trip(db.Model, SerializerMixin):
    __tablename__ = 'trips'

    id = db.Column(db.Integer, primary_key=True)
    location  = db.Column(db.String)
    season = db.Column(db.String)
    is_winter = db.Column(db.Boolean)
    price = db.Column(db.Float)
    is_flying = db.Column(db.Boolean)
    weight_limit = db.Column(db.Integer)
    vacations = relationship('Vacation', back_populates = 'trip', cascade ="all, delete-orphan")