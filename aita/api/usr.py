from flask import Blueprint, g, jsonify, make_response
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


@bp.route('/getpic', methods=['GET'])
@login_required
def get_usr_pic():
    MEMBER = get_collection('member')

    result = MEMBER.find_one({'usr': g.usr['usr']})
    response = make_response(result['pic'])
    response.headers.set('Content-Type', 'image/png')
    return response


@bp.route('/getpicstr', methods=['GET'])
def get_usr_picstr():
    """
        为人脸对比返回用户上传的图片
    """
    MEMBER = get_collection('member')

    result = MEMBER.find_one({'usr': g.usr['usr']})
    return result['pic']
