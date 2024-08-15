from sqlalchemy_serializer import SerializerMixin
from sqlalchemy.orm import validates, relationship
from sqlalchemy.ext.associationproxy import association_proxy
from config import db

class Activity(db.Model, SerializerMixin):
    __tablename__ = 'activities'
    
    id = db.Column(db.Integer, primary_key=True)
    budget = db.Column(db.Integer, nullable=False)
    adv_scale = db.Column(db.Integer , nullable=False)
    is_alone = db.Column(db.Boolean, nullable=False)
    name = db.Column(db.String, nullable=False)
    desc = db.Column(db.String, nullable=False)
    
    serialize_rules = ('-vacations.activity',)    
    vacations = db.relationship('Vacation', back_populates='activity', cascade ="all, delete-orphan")

    @validates('budget')
    def check_bank(self, key, value):
        if type(value) is int and 1 <= value <= 350:
            return value
        else:
            raise ValueError('Get more money brokey')

    @validates('adv_scale')
    def check_adv(self, key, value):
        if type(value) is int and 1 <= value <= 10:####
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
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    activity_id = db.Column(db.Integer, db.ForeignKey('activities.id'))
    trip_id = db.Column(db.Integer, db.ForeignKey('trips.id'))
    user = db.relationship('User', back_populates = 'vacations', cascade ="all")
    activity = db.relationship('Activity', back_populates = 'vacations', cascade ="all")
    trip = db.relationship('Trip', back_populates= 'vacations', cascade ="all")
    serialize_rules = ('-user.vacations', '-activity.vacations', '-trip.vacations')    
class User(db.Model, SerializerMixin):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String , nullable=False)
    budget = db.Column(db.Float, nullable=False)
    is_alone = db.Column(db.Boolean)
    password = db.Column(db.String, nullable=False)
    email = db.Column(db.String, nullable=False, unique = True)


    serialize_rules = ('-luggages.user', '-vacations.user' )
    
    
    luggages = db.relationship('Luggage', back_populates = 'user', cascade ="all, delete-orphan")
    vacations = db.relationship('Vacation', back_populates = 'user', cascade ="all, delete-orphan")

    @validates('password')
    def check_password(self,key, value):
        if type(value) is str and 8 <= len(value) <= 16: ####
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
        if type(value) is int:
            return value 
        else:
            raise ValueError('You are too broke :(')

class Luggage(db.Model, SerializerMixin):
    __tablename__ = 'luggages'

    id = db.Column(db.Integer, primary_key=True)
    style_shirt = db.Column(db.Boolean, nullable=False)
    style_pants = db.Column(db.Boolean, nullable=False)
    style_accessories = db.Column(db.Boolean, nullable=False)
    is_summer = db.Column(db.Boolean, nullable=False)
    pants = db.Column(db.Integer, nullable=False)
    shirts = db.Column(db.Integer, nullable=False)  
    other_clothes = db.Column(db.Integer, nullable=False)
    
    serialize_rules = ('-user.luggages',)

    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    user = db.relationship('User', back_populates = 'luggages')

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
    is_winter = db.Column(db.Boolean )
    price = db.Column(db.Float, nullable=False)
    is_flying = db.Column(db.Boolean)
    weight_limit = db.Column(db.Integer, nullable=False)
    serialize_rules = ('-vacations.trip',)
    vacations = db.relationship('Vacation', back_populates = 'trip', cascade ="all, delete-orphan")
    
    @validates('weight_limit')
    def check_limit(self, key, value):
        if type(value) is int and 25<=value<=50:
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
        valid_season=["summer","spring", "winter", "fall"]
        if type(value) is str and value in valid_season:
            return value
        else:
                raise ValueError("Not a season on earth")