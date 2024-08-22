from flask import request, make_response, session
from flask_restful import Resource, Api
from config import app, db, api
from models import Luggage, User, Trip, Activity, Luggage, Vacation


@app.before_request
def check_if_logged_in():
    print(request.endpoint)
    if  session.get('user_id') or request.endpoint in ('login','register','session'):
        pass
    else:
        return make_response({'error':'Please log in first'}, 403)
        



class All_Luggage(Resource):
    def get(self):
        ll = Luggage.query.all()
        return [lug.to_dict(rules=('-user',)) for lug in ll],200
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
                other_clothes = data['other_clothes'],
                user_id=data['user_id']
                )
            db.session.add(lugg)
            db.session.commit()
            return lugg.to_dict(rules=('-user',)), 200
        except Exception as e:
            return make_response({'error': str(e)},404)
#this get one, patch, and delete are for luggage 
class Editing(Resource):
    def get(self, id):
        lug = Luggage.query.filter(Luggage.id == id).first()
        if lug:
            return lug.to_dict(rules=('-user.vacations',)), 200
        else:
            return make_response('This luggage does not exist')
    def patch(self,id):
        ages = Luggage.query.filter(Luggage.id == id).first()
        if ages is not None:
            try:
                data = request.get_json()
                for key in data:
                    print("key",key)
                    setattr(ages, key, data[key])
                db.session.add(ages)
                db.session.commit()
                return ages.to_dict(rules=('-user.vacations',)),200
            except Exception as e:
                return make_response({
                    'Error' : str(e)
                },404)
        else:
            return make_response({
                'Error' : 'Luggage not found '
            },404)
    def delete(self, id):
        age = Luggage.query.filter(Luggage.id == id).first()
        if age:
            db.session.delete(age)
            db.session.commit()
            return {}, 200
        else:
            return make_response({
                'Error': 'Could not find luggage'
            },404)
api.add_resource(All_Luggage,'/api/luggages')
api.add_resource(Editing,'/api/luggages/<int:id>')


class All_Activity(Resource):
    def get(self):
        aa = Activity.query.all()
        return [act.to_dict(rules=('-vacations',)) for act in aa],200
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
            return vity.to_dict(rules=('-vacations',)), 200
        except Exception as e:
            return make_response({'error': str(e)},404)
class One_Activity(Resource):
    def get(self, id):
        act = Activity.query.filter(Activity.id == id).first()
        if act:
            return act.to_dict(rules=('-vacations',)),200
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
                return one.to_dict(rules=('-vacations',)),202
            except Exception as e:
                return make_response({'error': str(e)}), 404
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
            },404)
api.add_resource(All_Activity,'/activity')
api.add_resource(One_Activity,'/activity/<int:id>')


class All_User(Resource):
    def get(self):
        au = User.query.all()
        return [us.to_dict(rules=('-vacations',)) for us in au],200
    def post(self):
        try:
            data = request.get_json()
            new_user = User(
                username = data['username'], 
                budget = data['budget'], 
                is_alone = data['is_alone'], 
                password = data['password'],
                email = data['email']
            )
            db.session.add(new_user)
            db.session.commit()
            return new_user.to_dict(rules=('-vacations',)),200
        except Exception as e:
            return make_response({'errors': str(e)},404)
class One_User(Resource):
    def get(self, id):
        act = User.query.filter(User.id == id).first()
        if act:
            return act.to_dict(rules=('-vacations',)),200
        else:
            return make_response({'error':'This user does not exist'},400)
    def patch(self, id):
        one = User.query.filter(User.id == id).first()
        if one:
            try:
                data = request.get_json()
                for key in data:
                    setattr(one,key,data[key])
                db.session.add(one)
                db.session.commit()
                return one.to_dict(rules=('-vacations',)),202
            except Exception as e:
                return make_response({"error": str(e)},404) 
        else:
            return make_response('This user does not exist',404)
    def delete(self, id):
        one = User.query.filter(User.id == id).first()
        if one:
            db.session.delete(one)
            db.session.commit()
            return {}, 204
        else:
            return make_response({
                'error': 'Could not find user'
            },404)
api.add_resource(All_User,'/users', endpoint='register')
api.add_resource(One_User,'/users/<int:id>')


class All_Trip(Resource):
    def get(self):
        at = Trip.query.all()
        return [faire.to_dict(rules=('-vacations',)) for faire in at],200
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
            return make_response({'error': str(e)},404)
class One_Trip(Resource):
    def get(self, id):
        rip = Trip.query.filter(Trip.id == id).first()
        if rip:
            return rip.to_dict(rules=('-vacations',)),200
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
                return make_response({"error": str(e)},404)
        else:
            return make_response({
                'Error': 'Could not find Trip'},404)
    def delete(self, id):
        one = Trip.query.filter(Trip.id == id).first()
        if one:
            db.session.delete(one)
            db.session.commit()
            return {}, 204
        else:
            return make_response({
                'Error': 'Could not find Trip'
            },404)
api.add_resource(All_Trip,'/trip')
api.add_resource(One_Trip,'/trip/<int:id>')

class One_Vacation(Resource):
    def get(self, id):
        vity = Vacation.query.filter(Vacation.id == id).first()
        if vity:
            return vity.to_dict(),200
        else:
            return make_response('This vacation does not exist',400)
    def delete(self, id):
        one = Vacation.query.filter(Vacation.id == id).first()
        if one:
            db.session.delete(one)
            db.session.commit()
            return {}, 204
        else:
            return make_response({
                'Error': 'Could not find vacation'
            },404)
        
class All_Vacation(Resource):
    def get(self):
        at = Vacation.query.all()
        return [faire.to_dict() for faire in at],200
    def post(self):
        try:
            data = request.get_json()
            sure = Vacation(
                start_date = data['start_date'],
                end_date = data['end_date'],
                trip_id = data['trip_id']
            )
            db.session.add(sure)
            db.session.commit()
            return sure.to_dict(), 200
        except Exception as e:
            return make_response({'error': str(e)},404)

api.add_resource(One_Vacation,'/vacation/<int:id>')
api.add_resource(All_Vacation,'/vacation')



class Login(Resource):
    def post(self):
        email = request.get_json()['email']
        user = User.query.filter(User.email == email).first()
        password = request.get_json()['password']
        if user.authenticate(password) and user:
            session['user_id'] = user.id
            return user.to_dict(), 200
        return make_response({'error':'Invalid username or password'}, 401)
    


class CheckSession(Resource):
    def get(self):
        user = User.query.filter(User.id == session.get('user_id')).first()
        if user:
            return user.to_dict()
        else:
            return {'message': '401: Not Authorized'}, 401
        
class Logout(Resource):
    def delete(self):
        session['user_id'] = None
        return {'message': '204: No Content'}, 200


class SaveSession(Resource):
    def get(self):
        print(session)
        return {}
    
    def post(self):
        data = request.get_json()
        session['data'] = data['data']
        print(data)
        return {}

api.add_resource(SaveSession,'/session/save')
api.add_resource(Logout,'/logout')
api.add_resource(CheckSession,'/session', endpoint='session')
api.add_resource(Login,'/login')

if __name__ == '__main__':
    app.run(port=5555, debug=True)