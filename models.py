import pymongo
from bson import ObjectId
from pymongo import MongoClient
from werkzeug.security import generate_password_hash, check_password_hash


def find_user(email, password):
    client = MongoClient(
        "mongodb+srv://maxs:hwfi%211920@maxmongo-yndfj.mongodb.net/test?retryWrites=true&w=majority"
    )
    db = client.pymongodb
    mycol = db.users
    results = mycol.find_one({"email": email})
    if results:
        if check_password_hash(results['password'], password):
            return results
        else:
            return "user not found"
    return results


def add_user(email, firstname, lastname, password, role):
    try:
        client = MongoClient("mongodb+srv://maxs:hwfi%211920@maxmongo-yndfj.mongodb.net/test?retryWrites=true&w"
                             "=majority")
        print("Connected successfully!!!")
    except:
        print("Could not connect to MongoDB")
    db = client.pymongodb
    collection = db.users
    user_rec = {
        "email": email,
        "firstName": firstname,
        "lastName": lastname,
        "password": generate_password_hash(password),
        "role": role
    }
    results = collection.find_one({"email": email})
    print(results)
    if results:
        return False
    else:
        inc_record = collection.insert_one(user_rec)
        print("Data inserted with record ids", inc_record)
        # Printing the data inserted
        cursor = collection.find()
        for record in cursor:
            print(record)
            return True


def find_user_id(id):
    try:
        client = MongoClient("mongodb+srv://maxs:hwfi%211920@maxmongo-yndfj.mongodb.net/test?retryWrites=true&w"
                             "=majority")
        print("Connected successfully!!!")
    except:
        print("Could not connect to MongoDB")
    db = client.pymongodb
    collection = db.users
    results = collection.find_one({'_id': ObjectId(id)})
    if results:
        return True
    else:
        return False
