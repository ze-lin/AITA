import datetime, base64, functools
from flask import Blueprint, g, request, session, jsonify, render_template
from aita.db import get_collection

bp = Blueprint('auth', __name__, url_prefix='/auth')


@bp.route('/signup', methods=['POST'])
def sign_up():
    MEMBER = get_collection('member')

    result = MEMBER.find_one({'usr': request.form['usr']})
    if request.form['usr'] == '':
        return 'require username'
    elif request.form['pwd'] == '':
        return 'require password'

    if result:
        return 'Taken!'
    else:
        image = request.files['file']
        document = {
            'usr': request.form['usr'],
            'pwd': request.form['pwd'],
            'role': request.form['role'],
            'date': str(datetime.date.today()),
            'pic': base64.encodebytes(image.read())
        }
        MEMBER.insert_one(document)
        return 'Success!'


@bp.route('/signin', methods=['POST'])
def sign_in():
    result_filter = {
        'usr': request.form['usr'],
        'pwd': request.form['pwd']
    }
    MEMBER = get_collection('member')

    result = MEMBER.find_one(result_filter)
    if result:
        session.clear() # What is a session? And how does cookie work in this?
        session['usr'] = result['usr']
        return jsonify(status=True, role=result['role'])
    else:
        return jsonify(status=False)


@bp.before_app_request
def load_logged_in_user():
    usr_id = session.get('usr')

    if usr_id is None:
        g.usr = None
    else:
        MEMBER = get_collection('member')

        result = MEMBER.find_one({'usr': usr_id})
        result.pop('pwd')
        g.usr = result


@bp.route('/logout', methods=['GET'])
def logout():
    session.clear()
    return 'Success!'


def login_required(view):
    @functools.wraps(view)
    def wrapped_view(**kwargs):
        if g.usr is None:
            return 'Invalid User'

        return view(**kwargs)
    return wrapped_view
