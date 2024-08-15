from random import randint, choice, uniform
from config import app
from faker import Faker
from models import db, User, Trip, Activity, Luggage, Vacation

fake = Faker()

def create_users():
    for _ in range(10):
        user = User(
            username = fake.name(),
            budget = randint(100, 350),
            is_alone = choice([True, False]),
            password = fake.password(),
            email = fake.email()
        )
        db.session.add(user)

def create_trips():
    for _ in range(10):
        trip = Trip(
            location = fake.city(),
            season = choice(["summer", "fall", "winter", "spring"]),
            is_winter = choice([True, False]),
            price = uniform(100, 500),
            is_flying = choice([True, False]),
            weight_limit = randint(25, 50)
        )
        db.session.add(trip)
        
def create_activities():
    for _ in range(10):
        activity = Activity(
            name = fake.catch_phrase(),
            desc = fake.text(),
            budget= randint(1, 350),
            adv_scale = randint(1, 10),
            is_alone = choice([True, False]))
        db.session.add(activity)
        
def create_luggages():
    for _ in range(10):
        luggages = Luggage(
            style_shirt = choice([True, False]),
            style_pants = choice([True, False]),
            style_accessories = choice([True, False]),
            is_summer = choice([True, False]),
            pants = randint(1, 10),
            shirts = randint(1, 10),
            other_clothes = randint(1, 10),
            user_id = randint(1, 10)
        )
        db.session.add(luggages)

def create_vacations():
    for _ in range(10):
        vacation = Vacation(
                user_id = randint(1, 10),
                activity_id = randint(1, 10),
                trip_id = randint(1, 10)
                )
        db.session.add(vacation)


if __name__ == '__main__':
    with app.app_context():
        print("Clearing DB")
        db.drop_all()
        db.create_all()
        print("Seeding DB")
        create_users()
        create_trips()
        create_activities()
        create_luggages()
        create_vacations()
        db.session.commit()
        print("Done!")
