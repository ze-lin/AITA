import base64
from flask import Blueprint, g, jsonify, make_response, request
from aita.auth import login_required
from aita.db import get_collection

bp = Blueprint('usr', __name__, url_prefix='/usr')


@bp.route('/getinfo', methods=['GET'])
@login_required
def get_usr_info():
    MEMBER = get_collection('member')

    result = MEMBER.find_one({'usr': g.usr['usr']})
    result.pop('_id')
    result.pop('pic')
    return jsonify(result)


@bp.route('/updateinfo', methods=['POST'])
@login_required
def update_usr_info():
    MEMBER = get_collection('member')

    result = MEMBER.find_one({'usr': g.usr['usr']})
    pwd = request.form['pwd']
    if pwd != '':
        result['pwd'] = pwd
    image = request.files['file']
    result['pic'] = base64.encodebytes(image.read())
    MEMBER.replace_one({'usr': g.usr['usr']}, result)

    return 'Success!'


@bp.route('/updatepwd', methods=['GET'])
@login_required
def update_usr_pwd():
    MEMBER = get_collection('member')

    result = MEMBER.find_one({ 'usr': g.usr['usr'] })
    pwd = request.args.get('pwd')
    if pwd != '':
        result['pwd'] = pwd

    MEMBER.replace_one({'usr': g.usr['usr']}, result)

    return 'Success!'


@bp.route('/getpic', methods=['GET'])
@login_required
def get_usr_pic():
    MEMBER = get_collection('member')

    result = MEMBER.find_one({'usr': g.usr['usr']})
    response = make_response(result['pic'])
    response.headers.set('Content-Type', 'image/png')
    return response
