from db.mongo_db import get_db
from models.Note import Note
from  flask import jsonify
from bson import ObjectId



def insert(data):
    new_note = Note(title=data['title'], content=data['content'], due_date=data['due_date'], priority=data['priority'])
    collection = get_db().nots
    collection.insert_one(new_note.to_dict())
    return jsonify({"message": "created successfully"}, new_note.to_dict())

def get():
    db = get_db()
    my_list = list(db.nots.find())
    for note in my_list:
        note['_id'] = str(note['_id'])

    return jsonify({"notes": my_list})

def get_note_by_id(note_id):
    db = get_db()
    note = db.nots.find_one({"_id": ObjectId(note_id)})
    if note:
        note['_id'] = str(note['_id'])
        return jsonify({"note": note})
    else:
        return jsonify({"message": "Note not found"}), 404