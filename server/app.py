from flask import request
from flask_restful import Resource, Api
from config import app, db, api
from models import Luggage, User, Trip, Activity, Luggage, Vacation
class All_Luggage(Resource):
    def get(self, id):
        ll = Luggage.query.all()
        return [lug.to_dict() for lug in ll],200
    def post(self):
        try:
            data = request.get_json()
            lugg = Luggage(
                pants = data['pants'], 
                shirts = data['shirts'], 
                other_clothes = data['other_clothes']
            )
            db.session.add(lugg)
            db.session.commit()
            return lugg.to_dict(), 200
        except Exception as e:
            raise ValueError('Pack more clothes')
class Editing(Resource):
    def get(self, id):
        lug = Luggage.query.filter(Luggage.id == id).first()
        if lug:
            return lug.to_dict(), 200
        else:
            raise ValueError('This luggage does not exist')
    def patch(self,id):
        ages = Luggage.query.filter(Luggage.id == id).first()
        if ages is not None:
            try:
                data = request.get_json()
                for key in data:
                    setattr(ages, key, data[key])
                db.session.add(ages)
                db.session.commit()
                return ages.to_dict(),202
            except Exception as e:
                raise ValueError({
                    'Error' : 'Validation errors'
                }), 400
        else:
            raise ValueError({
                'Error' : 'Luggage not found '
            })
    def delete(self, id):
        age = Luggage.query.filter(Luggage.id == id).first()
        if age:
            db.session.delete(age)
            db.session.commit()
            return {}, 204
        else:
            raise ValueError({
                'Error': 'Could not find luggage'
            }),404
api.add_resource(All_Luggage,'/Luggages')
api.add_resource(Editing,'/ChangeLuggages/<int:id>')


class All_Activity(Resource):
    def get(self, id):
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
            raise ValueError('This activity is already present')
api.add_resource(All_Activity,'/Activity')
class One_Activity(Resource):
    def get(self, id):
        act = Activity.query.filter(Activity.id == id).first()
        if act:
            return act.to_dict()
        else:
            raise ValueError('This activity does not exist')
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
                raise ValueError('You can not change this aspect')
        else:
            raise ValueError('This activity does not exist')
    def delete(self, id):
        vity = Activity.query.filter(Activity.id == id).first()
        if vity:
            db.session.delete(vity)
            db.session.commit()
            return {}, 204
        else:
            raise ValueError({
                'Error': 'Could not find Activity'
            }),404
api.add_resource(One_Activity,'/Activity/<int:id>')

if __name__ == '__main__':
    app.run(port=5555, debug=True)