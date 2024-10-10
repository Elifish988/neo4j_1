from bson import ObjectId

from database.connect import cars, drivers, taxi_db


class MongoDBRepository:
    def __init__(self, collection):
        self.collection = collection


    def add(self, item):
        item_id = self.collection.insert_one(item).inserted_id
        return item_id


    def get_all(self):
        return self.collection.find()


    def get_by_id(self, id):
        return self.collection.find_one({"_id": ObjectId(id)})


    def update(self ,object_id, item):
        self.collection.update_one({"_id": ObjectId(object_id)}, {"$set": item})


    def delete(self, object_id):
        self.collection.delete_one({"_id": ObjectId(object_id)})












