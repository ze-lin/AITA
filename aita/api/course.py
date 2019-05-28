import datetime, time, os
from flask import Blueprint, jsonify, request, g
from aita.auth import login_required
from aita.db import get_collection
from werkzeug.utils import secure_filename


bp = Blueprint('course', __name__, url_prefix='/course')


@bp.route('/getall', methods=['GET'])
def get_all_course():
    COURSE = get_collection('course')

    result = COURSE.find()
    json_body = {}
    for i, document in enumerate(result):
        json_body[i] = document
        json_body[i].pop('_id')
    return jsonify(json_body)


@bp.route('/getall-teacher', methods=['GET'])
@login_required
def get_all_course_teacher():
    COURSE = get_collection('course')
    if g.usr['role'] == 'student':
        return 'student'

    result = COURSE.find({ 'teacher': g.usr['usr'] })
    json_body = {}
    for i, document in enumerate(result):
        json_body[i] = document
        json_body[i].pop('_id')
    return jsonify(json_body)


@bp.route('/create', methods=['GET'])
@login_required
def create_course():
    COURSE = get_collection('course')

    document = {
        'genre': request.args.get('genre'),
        'title': request.args.get('title'),
        'exam': request.args.get('exam'),
        'time': request.args.get('time'),
        'teacher': g.usr['usr'],
        'video': secure_filename(request.args.get('video')),
        'article': secure_filename(request.args.get('article')),
        'date': str(datetime.date.today()),
        'id': str(time.time()),
        'view': 0
    }
    COURSE.insert_one(document)
    return 'Success!'


@bp.route('/delete', methods=['GET'])
@login_required
def delete_course():
    # 级联删除
    COURSE = get_collection('course')
    COLLECTION = get_collection('collection') # delete all
    course_id = request.args.get('id')

    COLLECTION.delete_many({ 'id': course_id })
    COURSE.delete_one({'id': course_id})
    return 'Success!'


@bp.route('/uploadfile', methods=['POST'])
@login_required
def upload():
    """
        存数据库留给submit_class做
    """
    file = request.files['file']
    file_name = secure_filename(file.filename)
    if not os.path.exists(os.path.join('aita/static', file_name)):
        file.save(os.path.join('aita/static', file_name))

    return 'Success!'


@bp.route('/getreading', methods=['GET'])
@login_required
def get_reading():
    COURSE = get_collection('course')

    result = COURSE.find_one({'id': request.args.get('id')})
    file_name = result['article']
    file_path = os.path.join('aita/static', file_name)
    content = ''

    with open(file_path, 'r') as f:
        for line in f:
            content += line
    return content

@bp.route('/getvideo', methods=['GET'])
@login_required
def get_video():
    COURSE = get_collection('course')

    result = COURSE.find_one({'id': request.args.get('id')})
    file_name = result['video']
    return file_name

@bp.route('/getexam', methods=['GET'])
@login_required
def get_exam():
    COURSE = get_collection('course')

    result = COURSE.find_one({'id': request.args.get('id')})
    return result['exam']


@bp.route('/view', methods=['GET'])
@login_required
def view():
    COURSE = get_collection('course')
    course_id = request.args.get('id')
    result = COURSE.find_one({'id': course_id })
    result['view'] += 1
    COURSE.replace_one({'id': course_id }, result)

    COLLECTION = get_collection('collection')
    document = {
        'id': course_id,
        'usr': g.usr['usr']
    }
    result = COLLECTION.find_one(document)
    if not result:
        COLLECTION.insert_one(document)
    return 'Success!'
