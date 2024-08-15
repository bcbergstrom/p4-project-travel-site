from flask import request, make_response
from flask_restful import Resource, Api
from config import app, db, api
from models import Luggage, User, Trip, Activity, Luggage, Vacation
class All_Luggage(Resource):
    def get(self):
        ll = Luggage.query.all()
        return [lug.to_dict() for lug in ll],200
    def post(self):
        try:
            data = request.get_json()
            lugg = Luggage(
                style_shirt = data['style_shirt'], 
                style_accessories = data['style_accessories'], 
                style_pants = data['style_pants'],
                is_summer = data['is_summer'],
                pants = data['pants'], 
                shirts = data['shirts'], 
                other_clothes = data['other_clothes']
            )
            db.session.add(lugg)
            db.session.commit()
            return lugg.to_dict(), 200
        except Exception as e:
            return make_response('Pack more clothes'),404
class Editing(Resource):
    def get(self, id):
        lug = Luggage.query.filter(Luggage.id == id).first()
        if lug:
            return lug.to_dict(), 200
        else:
            return make_response('This luggage does not exist')
    def patch(self,id):
        ages = Luggage.query.filter(Luggage.id == id).first()
        if ages is not None:
            try:
                data = request.get_json()
                for key in data:
                    setattr(ages, key, data[key])
                db.session.add(ages)
                db.session.commit()
                return ages.to_dict(),200
            except Exception as e:
                return make_response({
                    'Error' : 'Validation errors'
                }), 404
        else:
            return make_response({
                'Error' : 'Luggage not found '
            }),404
    def delete(self, id):
        age = Luggage.query.filter(Luggage.id == id).first()
        if age:
            db.session.delete(age)
            db.session.commit()
            return {}, 200
        else:
            return make_response({
                'Error': 'Could not find luggage'
            }),404
api.add_resource(All_Luggage,'/Luggages')
api.add_resource(Editing,'/ChangeLuggages/<int:id>')


class All_Activity(Resource):
    def get(self):
        aa = Activity.query.all()
        return [act.to_dict() for act in aa],200
    def post(self):
        try:
            data = request.get_json()
            vity = Activity(
                budget = data['budget'], 
                adv_scale = data['adv_scale'], 
                is_alone = data['is_alone'], 
                name = data['name'],
                desc = data['desc']
            )
            db.session.add(vity)
            db.session.commit()
            #check if its already in our database
            return vity.to_dict(), 200
        except Exception as e:
            return make_response('This activity is already present'), 404
class One_Activity(Resource):
    def get(self, id):
        act = Activity.query.filter(Activity.id == id).first()
        if act:
            return act.to_dict(),200
        else:
            return make_response('This activity does not exist'),400
    def patch(self, id):
        one = Activity.query.filter(Activity.id == id).first()
        if one:
            try:
                data = request.get_json()
                for key in data:
                    setattr(one,key,data[key])
                db.session.add(one)
                db.session.commit()
                return one.to_dict(),202
            except Exception as e:
                return make_response('You can not change this aspect'), 404
        else:
            return make_response('This activity does not exist'),404
    def delete(self, id):
        vity = Activity.query.filter(Activity.id == id).first()
        if vity:
            db.session.delete(vity)
            db.session.commit()
            return {}, 204
        else:
            return make_response({
                'Error': 'Could not find Activity'
            }),404
api.add_resource(All_Activity,'/Activity')
api.add_resource(One_Activity,'/Activity/<int:id>')


class All_User(Resource):
    def get(self):
        au = User.query.all()
        return [us.to_dict() for us in au],200
    def post(self):
        try:
            data = request.get_json()
            sure = User(
                username = data['username'], 
                budget = data['budget'], 
                is_alone = data['is_alone'], 
                passowrd = data['passowrd'],
                email = data['email']
            )
            db.session.add(sure)
            db.session.commit()
            #check if its already in our database
            return sure.to_dict(), 200
        except Exception as e:
            return make_response('This User is already present'), 404
class One_User(Resource):
    def get(self, id):
        act = User.query.filter(User.id == id).first()
        if act:
            return act.to_dict(),200
        else:
            return make_response('This User does not exist'),400
    def patch(self, id):
        one = User.query.filter(User.id == id).first()
        if one:
            try:
                data = request.get_json()
                for key in data:
                    setattr(one,key,data[key])
                db.session.add(one)
                db.session.commit()
                return one.to_dict(),202
            except Exception as e:
                return make_response('You can not change this aspect'), 404
        else:
            return make_response('This User does not exist'),404
    def delete(self, id):
        one = User.query.filter(User.id == id).first()
        if one:
            db.session.delete(one)
            db.session.commit()
            return {}, 204
        else:
            return make_response({
                'Error': 'Could not find User'
            }),404
api.add_resource(All_User,'/User')
api.add_resource(One_User,'/User/<int:id>')


class All_Trip(Resource):
    def get(self):
        at = Trip.query.all()
        return [faire.to_dict() for faire in at],200
    def post(self):
        try:
            data = request.get_json()
            sure = Trip(
                location = data['location'], 
                season = data['season'], 
                is_winter = data['is_winter'], 
                price = data['price'],
                is_flying = data['is_flying'], 
                weight_limit = data['weight_limit']
            )
            db.session.add(sure)
            db.session.commit()
            #check if its already in our database
            return sure.to_dict(), 200
        except Exception as e:
            return make_response('This User is already present'), 404
class One_Trip(Resource):
    def get(self, id):
        rip = Trip.query.filter(Trip.id == id).first()
        if rip:
            return rip.to_dict(),200
        else:
            return make_response('This Trip does not exist'),400
    def patch(self, id):
        one = Trip.query.filter(Trip.id == id).first()
        if one:
            try:
                data = request.get_json()
                for key in data:
                    setattr(one,key,data[key])
                db.session.add(one)
                db.session.commit()
                return one.to_dict(),202
            except Exception as e:
                return make_response('You can not change this aspect'), 404
        else:
            return make_response('This Trip does not exist'),404
    def delete(self, id):
        one = Trip.query.filter(Trip.id == id).first()
        if one:
            db.session.delete(one)
            db.session.commit()
            return {}, 204
        else:
            return make_response({
                'Error': 'Could not find Trip'
            }),404
api.add_resource(All_Trip,'/Trip')
api.add_resource(One_Trip,'/Trip/<int:id>')


if __name__ == '__main__':
    app.run(port=5555, debug=True)