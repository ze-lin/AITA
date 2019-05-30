# White Box Testing
import pytest
from flask import g, session
from aita.db import get_collection
from io import BytesIO


def test_get_usr_info(app, auth, client):
    with app.app_context():
        with client:
            auth.login()
            assert session['usr'] == 'init'

            MEMBER = get_collection('member')
            result = MEMBER.find_one({'usr': 'init'})
            assert result
            assert '_id' in result
            assert 'pic' in result

            response = client.get('/usr/getinfo')
            assert b'init' in response.data

def test_update_usr_info(app, auth, client):
    with app.app_context():
        with client:
            auth.login()
            assert session['usr'] == 'init'

            MEMBER = get_collection('member')
            result = MEMBER.find_one({'usr': 'init'})
            assert result
            assert result['pwd'] == 'rightpwd'

            data = { 'pwd': 'newpwd' }
            data['file'] = (BytesIO(b'test'), 'image.png')

            response = client.post('/usr/updateinfo', data=data,  content_type='multipart/form-data')
            assert b'Success' in response.data

            result = MEMBER.find_one({'usr': 'init'})
            assert result['pwd'] == 'newpwd'



def test_update_usr_pwd(app, auth, client):
    with app.app_context():
        with client:
            auth.login()
            assert session['usr'] == 'init'

            MEMBER = get_collection('member')
            result = MEMBER.find_one({'usr': 'init'})
            assert result
            assert result['pwd'] == 'rightpwd'

            response = client.get('/usr/updatepwd', query_string={ 'pwd': 'newpwd' })
            assert b'Success' in response.data

            result = MEMBER.find_one({'usr': 'init'})
            assert result['pwd'] == 'newpwd'


def test_get_usr_pic(app, auth, client):
    with app.app_context():
        with client:
            auth.login()
            assert session['usr'] == 'init'

            MEMBER = get_collection('member')
            result = MEMBER.find_one({'usr': 'init'})
            assert result
            assert 'pic' in result

            response = client.get('/usr/getpic')
            assert response.status_code == 200
            assert b'image' in response.data