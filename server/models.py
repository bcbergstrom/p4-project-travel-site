from sqlalchemy_serializer import SerializerMixin
from sqlalchemy.orm import validates, relationship
from sqlalchemy.ext.associationproxy import association_proxy
from config import db

class Activity(db.Model, SerializerMixin):
    __tablename__ = 'activities'
    
    id = db.Column(db.Integer, primary_key=True)
    budget = db.Column(db.Integer, nullable=False)
    adv_scale = db.Column(db.Integer , nullable=False)
    is_alone = db.Column(db.Boolean)
    name = db.Column(db.String)
    desc = db.Column(db.String)
    
    vacations = relationship('Vacation', back_populates='activity', cascade ="all, delete-orphan")

    @validates('budget')
    def check_bank(self, key, value):
        if 0<= value => 350 and type(value) is str:
            return value
        else:
            raise ValueError('Get more money brokey')

    @validates('adv_scale')
    def check_adv(self, key, value):
        if type(value) is str and 1=> value <= 10:####
            return value
        else:
            raise ValueError('Input a number between 1-10')

    @validates('name', 'desc')
    def check_two(self, key, value):
        if type(value) is str:
            return value
        else:
            raise ValueError('Oops, something was spelled wrong or the wrong type was inputed')

class Vacation(db.Model, SerializerMixin):
    __tablename__ = 'vacations'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    activity_id = db.Column(db.Integer, db.ForeignKey('activity.id'))
    trip_id = db.Column(db.Integer, db.ForeignKey('trip.id'))
    user = relationship('User', back_populates = 'vacations', cascade ="all, delete-orphan")
    activity = relationship('Activity', back_populates = 'vacations', cascade ="all, delete-orphan")
    trip = relationship('Trip', back_populates= 'vacations', cascade ="all, delete-orphan")

class User(db.Model, SerializerMixin):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String , nullable=False)
    budget = db.Column(db.Float, nullable=False)
    is_alone = db.Column(db.Boolean)
    password = db.Column(db.String, nullable=False)
    email = db.Column(db.String, nullable=False, unique = True)

    luggages = relationship('Luggage', back_populates = 'user', cascade ="all, delete-orphan")
    vacations = relationship('Vacation', back_populates = 'user', cascade ="all, delete-orphan")

    @validates('password')
    def check_password(self,key, value):
        if type(value) is str and 1 => value <= 8: ####
            return value
        else:
            raise ValueError('Make your passowrd 8 letters')
    @validates('username')
    def check_username(self, key, value):
        if type(value) is str:
            return value
        else:
            raise ValueError('Not a vaild username')
    @validates('budget')
    def check_budget(self,key, value):
        if type(value) is float:
            return value 
        else:
            raise ValueError('You are too broke :(')

class Luggage(db.Model, SerializerMixin):
    __tablename__ = 'luggages'

    id = db.Column(db.Integer, primary_key=True)
    style_shirt = db.Column(db.Boolean)
    style_pants = db.Column(db.Boolean)
    style_accessories = db.Column(db.Boolean)
    is_summer = db.Column(db.Boolean)
    pants = db.Column(db.Integer)
    shirts = db.Column(db.Integer)
    other_clothes = db.Column(db.Integer)

    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    user = relationship('User', back_populates = 'luggages')

    @validates('other_clothes')
    def check_others(self,key,value):
        if type(value) is int:
            return value
        else:
            raise ValueError('Not enough clothes')
    @validates('shirts')
    def check_shirts(self,key,value):
        if type(value) is int:
            return value
        else:
            raise ValueError('You need more shirts')
    @validates('pants')
    def check_pants(self,key,value):
        if type(value) is int:
            return value
        else:
            raise ValueError('You didnt pack the right amount')

class Trip(db.Model, SerializerMixin):
    __tablename__ = 'trips'

    id = db.Column(db.Integer, primary_key=True)
    location  = db.Column(db.String, nullable=False)
    season = db.Column(db.String, nullable=False)
    is_winter = db.Column(db.Boolean)
    price = db.Column(db.Float, nullable=False)
    is_flying = db.Column(db.Boolean)
    weight_limit = db.Column(db.Integer, nullable=False)
    
    @validates('weight_limit')
    def check_limit(self, key, value):
        if type(value) is int and 25<=value=<50:
            return value
        else:
            raise ValueError('You packed too much!')
    @validates('price')
    def check_price(self, key, value):
        if type(value) is float:
            return value
        else:
            raise ValueError('You need to spend more money')
    @validates('location')
    def check_location(self, key, value):
        if type(value) is str:
            return value
        else:
            raise ValueError('Not a vaild username')
    @validates('season')
    def check_season(self, key, value):
        valid_season=["Summer","Spring", "Winter", "Fall"]
        if type(value) is str and in valid_season:
            return value
        elif letter not in valid_season:
                raise ValueError("Not a season on earth")