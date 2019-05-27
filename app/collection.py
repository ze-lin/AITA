import math
from flask import Blueprint, jsonify, request, g
from app.auth import login_required
from app.db import get_db

bp = Blueprint('collection', __name__, url_prefix='/collection')


@bp.route('/add', methods=['GET'])
@login_required
def add_collection():
    DB = get_db()
    COLLECTION = DB['collection']

    document = {
        'id': request.args.get('id'),
        'usr': g.usr['usr']
    }
    COLLECTION.insert_one(document)
    return 'Success!'


@bp.route('/get', methods=['GET'])
@login_required
def get_collection():
    DB = get_db()
    COURSE = DB['course']
    COLLECTION = DB['collection']

    courses = COLLECTION.find({'usr': g.usr['usr']})
    json_body = {}
    for i, course in enumerate(courses):
        course_id = course['id']
        course_content = COURSE.find_one({'id': course_id})
        json_body[i] = course_content
        json_body[i].pop('_id')
    return jsonify(json_body)


@bp.route('/delete', methods=['GET'])
@login_required
def delete_collection():
    DB = get_db()
    COLLECTION = DB['collection']

    result_filter = {
        'id': request.args.get('id'),
        'usr': g.usr['usr']
    }
    COLLECTION.delete_one(result_filter)
    return 'Success!'
