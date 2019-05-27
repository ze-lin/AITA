from flask import Blueprint, jsonify, request
from app.auth import login_required
from app.db import get_db

bp = Blueprint('comment', __name__, url_prefix='/comment')

@bp.route('/add', methods=['GET'])
@login_required
def add_comment():
    DB = get_db()
    COMMENT = DB['comment']

    document = {
        'id': request.args.get('id'),
        'startTime': request.args.get('startTime'),
        'endTime': request.args.get('endTime'),
        'content': request.args.get('content')
    }
    COMMENT.insert_one(document)
    return 'Success!'


@bp.route('/get', methods=['GET'])
@login_required
def get_comment():
    DB = get_db()
    COMMENT = DB['comment']

    result = COMMENT.find({'id': request.args.get('id')})
    json_body = {}
    for i, comment in enumerate(result):
        json_body[i] = comment
        json_body[i].pop('_id')
    return jsonify(json_body)
