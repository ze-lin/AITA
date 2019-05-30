import pytest
from aita import create_app
from pymongo import MongoClient
from flask import current_app
from aita.db import get_collection


@pytest.fixture
def app():
    # print('new app!')
    app = create_app('Testing')
    with app.app_context():
        get_collection('member').insert_one({'usr': 'init', 'pwd': 'rightpwd', \
            'role': 'teacher', 'data': '2019', 'pic': 'image'})

        document = {
            '_id': 1,
            'rate': 1,
            'emotion': {},
            'usr': 'init',
            'id': '111'
        }
        document['emotion']['111'] = {
            'anger': 100, 'disgust': 100, 'fear': 0, 'happiness': 0,
            'neutral': 0, 'sadness': 0, 'surprise': 0, 'vector_x': 0, 'vector_y': 0,
            'vector_z': 0, 'position_x': 0, 'position_y': 0
        }
        FOCUS = get_collection('focus')
        FOCUS.insert_one(document)
        document['usr'] = 'init2'
        document['_id'] = 2
        FOCUS.insert_one(document)

    app.teardown_appcontext(drop_db)
    yield app


@pytest.fixture
def client(app):
    # print('new client!')
    return app.test_client()


def drop_db(e=None):
    db = MongoClient(current_app.config['DATABASE'])
    db.drop_database('test')


class AuthActions(object):
    def __init__(self, client):
        self._client = client

    def login(self, usr='init', pwd='rightpwd'):
        return self._client.post('/auth/signin', data={'usr': usr, 'pwd': pwd})


@pytest.fixture
def auth(client):
    return AuthActions(client)
