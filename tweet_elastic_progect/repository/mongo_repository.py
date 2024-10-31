from pymongo import MongoClient


MONGO_URI = 'mongodb://localhost:27017/'
DB_NAME = 'users_db'


def get_db():
    client = MongoClient(MONGO_URI)
    db = client[DB_NAME]
    return db