from flask import request
from flask_restful import Resource, Api
from config import app, db, api

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
api.add_resource(All_Luggage,'/Luggages')

class Editing(Resource):
    def patch(self,id):
        ages = Luggage.query.filter(Luggage.id == id).first()
        if ages:
            try:
                data = request.get_json()
                for key in data:
                    setattr(ages, key, data[key])
                db.session.add(ages)
                db.session.commit()
                return ages.to_dict(),202
            except Exception as e:
                return{
                    'Error' : 'Validation errors'
                }, 400
        else:
            return{
                'Error' : 'Luggage not found '
            }
    def delete(self, id):
        age = Luggage.query.filter(Luggage.id == id).first()
        if age:
            db.session.delete(age)
            db.session.commit()
            return {}, 204
        else:
            return{
                'Error': 'Could not find luggage'
            },404
        
api.add_resource(Editing,'/ChangeLuggages/<int:id>')

# class One_Lugg(Resource):
#     def get(self, id):
#         lug = Luggage.query.filter(Luggage.id == id).first()
#         if lug:
#             return lug.to_dict(), 200

# api.add_resource(One_Lugg,'/One_thing')
class All_Activity(Resource):
    

if __name__ == '__main__':
    app.run(port=5555, debug=True)