from flask import Blueprint, jsonify, g
from aita.auth import login_required
from aita.db import get_collection
from aita.api.focus import calcu_focus

bp = Blueprint('completeness', __name__, url_prefix='/completeness')

def calcu_focus_completeness(focus_data):
    if focus_data:
        ans = 100
        for minute in range(0, 10): # 每分钟至少 3000 分 才能得 10 分
            score = 0
            for secend in range(minute*60, (minute+1)*60):
                if str(secend) in focus_data['emotion']:
                    score += calcu_focus(focus_data['emotion'][str(secend)])
            # print(score)
            if score < 3000:
                ans -= 10
        return ans
    else: # 没参加这个课程
        return 0

@bp.route('/get', methods=['GET'])
@login_required
def get_completeness():
    COURSE = get_collection('course')
    COLLECTION = get_collection('collection')
    FOCUS = get_collection('focus')

    result = COLLECTION.find({ 'usr': g.usr['usr'] })
    json_body = {}
    for i, course in enumerate(result):
        course_id = course['id']
        course_focus = FOCUS.find_one({ 'id': course_id, 'usr': g.usr['usr'] })
        course_content = COURSE.find_one({ 'id': course_id })
        json_body[i] = course_content
        json_body[i]['complete'] = calcu_focus_completeness(course_focus)
        json_body[i].pop('_id')
    return jsonify(json_body)
