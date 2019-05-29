import pytest
from aita import create_app
from pymongo import MongoClient
from flask import current_app
from aita.db import get_collection


@pytest.fixture
def app():
    app = create_app('Testing')

    with app.app_context():
        get_collection('member').insert_one({'usr': 'init', 'pwd': 'rightpwd', \
            'role': 'teacher', 'data': '2019', 'pic': 'image'})
    app.teardown_appcontext(drop_db)
    yield app


@pytest.fixture
def client(app):
    return app.test_client()


def drop_db(e=None):
    db = MongoClient(current_app.config['DATABASE'])
    db.drop_database('test')

# class AuthActions(object):
#     def __init__(self, client):
#         self._client = client

#     def login(self, username='test', password='test'):
#         return self._client.post(
#             '/auth/login',
#             data={'username': username, 'password': password}
#         )

#     def logout(self):
#         return self._client.get('/auth/logout')


# @pytest.fixture
# def auth(client):
#     return AuthActions(client)


