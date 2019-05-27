import math
from flask import Blueprint, jsonify, request, g
from aita.auth import login_required
from aita.db import get_collection

bp = Blueprint('focus', __name__, url_prefix='/focus')


def calcu_focus(focus_dict):
    result = 100 - focus_dict['anger'] - focus_dict['disgust'] - focus_dict['fear'] - \
        focus_dict['sadness']/2 - focus_dict['surprise']/2 - focus_dict['vector_x']*30 - focus_dict['vector_y']*30
    if result < 0:
        result = 0
    return result


@bp.route('/add', methods=['GET'])
@login_required
def add_focus():
    FOCUS = get_collection('focus')

    result_filter = {
        'usr': g.usr['usr'],
        'id': request.args.get('course_id') # course_id
    }
    c_time = str(math.floor(float(request.args.get('time'))))
    document = result_filter.copy()
    document['rate'] = 1.0
    document['emotion'] = {}
    document['emotion'][c_time] = {
        'anger': float(request.args.get('anger')),
        'disgust': float(request.args.get('disgust')),
        'fear': float(request.args.get('fear')),
        'happiness': float(request.args.get('happiness')),
        'neutral': float(request.args.get('neutral')),
        'sadness': float(request.args.get('sadness')),
        'surprise': float(request.args.get('surprise')),
        'vector_x': abs(float(request.args.get('vector_x'))),
        'vector_y': abs(float(request.args.get('vector_y'))),
        'vector_z': float(request.args.get('vector_z')),
        'position_x': float(request.args.get('position_x')),
        'position_y': float(request.args.get('position_y'))
    }
    result = FOCUS.find_one(result_filter)
    if result: # 已经有了
        result['emotion'][c_time] = document['emotion'][c_time]
        FOCUS.replace_one(result_filter, result)
    else:
        FOCUS.insert_one(document)
    return 'Success!'


@bp.route('/get', methods=['GET'])
@login_required
def get_focus():
    """
        每个学生获取自己的专注度
    """
    FOCUS = get_collection('focus')

    result_filter = {
        'usr': g.usr['usr'],
        'id': request.args.get('course_id')
    }
    result = FOCUS.find_one(result_filter)
    if result:
        json_body = {}
        for i in range(0, 600):
            if str(i) in result['emotion']:
                json_body[str(i)] = calcu_focus(result['emotion'][str(i)])
        return jsonify(json_body)
    else:
        return 'None'


@bp.route('/getavg', methods=['GET'])
@login_required
def get_avg_focus():
    """
        每个老师获取特定课程的平均专注度
    """
    FOCUS = get_collection('focus')

    result = FOCUS.find({'id': request.args.get('course_id')})
    if result:
        json_body = {}
        all_weight = 0.0
        for focus in result:
            weight = focus['rate']
            all_weight += weight
            for i in range(0, 600):
                if str(i) in focus['emotion']:
                    if str(i) in json_body:
                        json_body[str(i)] += calcu_focus(focus['emotion'][str(i)]) * weight
                    else:
                        json_body[str(i)] = calcu_focus(focus['emotion'][str(i)]) * weight

        for i in range(0, 600):
            if str(i) in json_body:
                json_body[str(i)] /= all_weight

        return jsonify(json_body)
    else:
        return 'None'


@bp.route('/rate', methods=['GET'])
@login_required
def rate():
    FOCUS = get_collection('focus')

    result_filter = {
        'usr': g.usr['usr'],
        'id': request.args.get('course_id')
    }
    result = FOCUS.find_one(result_filter)
    if result:
        result['rate'] = int(request.args.get('rate'))/5
        FOCUS.replace_one(result_filter, result)

    return 'Success!'
