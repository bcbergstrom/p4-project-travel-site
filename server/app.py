from flask import Flask, request, make_response, jsonify
from flask_migrate import Migrate
from flask_restful import Resource, Api
from models import Activity, Luggage, Vacation, User, Trip
from config import app, db, api


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.json.compact = False

migrate = Migrate(app, db)

db.init_app(app)

api = Api(app)

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
            raise ValueError('New bag as your carry on')
api.add_resource(All_Luggage,'/Luggages')

class One_Lugg(Resource):
    def get(self, id):
        lug = Luggage.query.filter(Luggage.id == id).first()
        if lug:
            return lug.to_dict(), 200

api.add_resource(All_Signups,'/signups')


if __name__ == '__main__':
    app.run(port=5555, debug=True)