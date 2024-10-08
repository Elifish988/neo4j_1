from  flask import Blueprint, request, jsonify

import servis



bp_crud = Blueprint('crud', __name__)
@bp_crud.route('/insert', methods=['POST'])
def insert():
    data = request.get_json()
    return  servis.insert(data)



@bp_crud.route('/get', methods=['GET'])
def get():
    return servis.get()


@bp_crud.route('/get/<note_id>', methods=['GET'])
def get_note_by_id(note_id):
    return servis.get_note_by_id(note_id)

