"""
    Micro Server For AITA
"""
import json, os, datetime, time
from pymongo import MongoClient
from flask import request, Flask
from werkzeug.utils import secure_filename

client = MongoClient()
DB = client['aita']
MEMEBER = DB['member']
COURSE = DB['course']
COLLECTION = DB['collection']
app = Flask(__name__)

# -------------------- FOR USR -----------------------
@app.route('/signup', methods=['POST'])
def sign_up():
    """
        Accept the sign up post request
    """
    document = {
        'usr': request.form['usr'],
        'pwd': request.form['pwd'],
        'role': request.form['role'],
        'date': str(datetime.date.today())
    }
    result = MEMEBER.find_one({'usr': request.form['usr']})
    if result:
        return 'Taken'
    else:
        MEMEBER.insert_one(document)
        return 'True'

@app.route('/signin', methods=['POST'])
def sign_in():
    """
        Accept the sign in post request
    """
    result_filter = {
        'usr': request.form['usr'],
        'pwd': request.form['pwd']
    }
    result = MEMEBER.find_one(result_filter)
    json_body = {}
    if result:
        json_body['status'] = 'True'
        json_body['role'] = result['role']
        return json.dumps(json_body, indent=2)
    else:
        json_body['status'] = 'Fasle'
        return json.dumps(json_body, indent=2)

@app.route('/getusrinfo', methods=['GET'])
def get_usr_info():
    result = MEMEBER.find_one({'usr': request.args.get('usr')})
    result.pop('_id')
    return json.dumps(result, indent=2)

# -------------------- FOR COURSE -----------------------
@app.route('/upload', methods=['POST'])
def upload():
    """
        存数据库留给submit_class做
    """
    file = request.files['file']
    filename = secure_filename(file.filename)
    file.save(os.path.join('/Users/ludanxer/Programs/AITA/uploads', filename))
    return 'True'

@app.route('/submitclass', methods=['GET'])
def submit_class():
    """
        还需要把filename保存入数据库，以避免重复之类的事情
    """
    document = {
        'genre': request.args.get('genre'),
        'title': request.args.get('title'),
        'exam': request.args.get('exam'),
        'time': request.args.get('time'),
        'teacher': request.args.get('teacher'),
        'video': request.args.get('video'),
        'article': request.args.get('article'),
        'date': str(datetime.date.today()),
        'id': str(time.time()),
        'view': 0
    }
    COURSE.insert_one(document)
    return 'True'

@app.route('/getclass', methods=['GET'])
def get_class():
    json_body = result_filter = {}
    if 'teacher' in request.args:
        result_filter = {'teacher': request.args.get('teacher')}
    elif 'student' in request.args: # TODO: This is not right
        result_filter = {'student': request.args.get('student')}
    result = COURSE.find(result_filter)
    i = 0
    for document in result:
        json_body[i] = document
        json_body[i].pop('_id')
        i += 1
    return json.dumps(json_body, indent=2)

@app.route('/deleteclass', methods=['GET'])
def delete_class():
    COURSE.delete_one({'id': request.args.get('id')})
    return 'True'

# -------------------- FOR COLLECTION -----------------------
@app.route('/addcollection', methods=['GET'])
def add_collection():
    document = {
        'id': request.args.get('id'),
        'usr': request.args.get('usr')
    }
    COLLECTION.insert_one(document)
    return 'True'


@app.route('/getcollection', methods=['GET'])
def get_collection():
    courses = COLLECTION.find({'usr': request.args.get('usr')})
    json_body = {}
    i = 0
    for course in courses:
        course_id = course['id']
        course_content = COURSE.find_one({'id': course_id})
        json_body[i] = course_content
        json_body[i].pop('_id')
        i += 1
    return json.dumps(json_body, indent=2)

@app.route('/deletecollection', methods=['GET'])
def delete_collection():
    COLLECTION.delete_one({'id': request.args.get('id')})
    return 'True'

if __name__ == "__main__":
    app.run(host='127.0.0.1', port='5000', debug='true')
