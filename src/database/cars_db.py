from pymongo import ASCENDING
from src.establish_db_connection import database


collection = database.carsDB
admin = database.adminDB
collection.create_index([("cars_id", ASCENDING)], unique=True)

def add_cars(id, name, price, company, admin_id):
    try:
        collection.insert_one(
            {
                "cars_id": id,
                "cars_name": name,
                "cars_price": price,
                "cars_company": company,
                "admin_id": admin_id,
            }
        )
        return True
    except Exception as e:
        print(f"Something went wrong: {e}")
        return False

def get_all_cars(admin_id):
    try:
        cars = collection.find({"admin_id": admin_id})
        a = []
        for cars in cars:
            del cars["_id"]
            a.append(cars)
        return a
    except Exception as e:
        print(f"Something went wrong: {e}")
        return None

def update_cars(id, name, price, company, admin_id):
    try:
        collection.update_one(
            {"cars_id": id, "admin_id": admin_id},
            {
                "$set": {
                    "cars_name": name,
                    "cars_price": price,
                    "cars_company": company,
                }
            }
        )
    except Exception as e:
        print(f"Something went wrong: {e}")
        return False

def delete_cars(id, admin_id):
    try:
        collection.delete_one({"cars_id": id, "admin_id": admin_id})
    except Exception as e:
        print(f"Something went wrong: {e}")
        return False

def cars_model(id, admin_id):
    try:
        cars = collection.find_one({"cars_id": id, "admin_id": admin_id})
        del cars["_id"]
        return cars
    except Exception as e:
        print(f"Something went wrong: {e}")
        return None
    
def login_admin(admin_id, password):
    try:
        admin = admin.find_one({"admin_id": admin_id})

        if admin is None:
            return False

        if admin["password"] == password:
            return True
        else:
            return False
        
    except Exception as e:
        print(f"Something went wrong: {e}")
        return False
    
def create_admin(admin_id, password):
    try:
        admin.insert_one(
            {
                "admin_id": admin_id,
                "password": password,
            }
        )
        return True
    except Exception as e:
        print(f"Something went wrong: {e}")
        return False