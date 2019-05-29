# Black Box Testing with Boundary Value Analysis method
import pytest
from io import BytesIO

@pytest.mark.parametrize(('usr', 'pwd', 'message'), (
    ('', '', b'Require Username'),
    ('usrname', '', b'Require Password'),
    ('init', 'rightpwd', b'Taken'),
    ('test', 'rightpwd', b'Success'),
))
def test_sign_up(client, usr, pwd, message):
    data={'usr': usr, 'pwd': pwd, 'role': 'teacher'}
    data['file'] = (BytesIO(b'test'), 'image.png')
    response = client.post('/auth/signup', data=data, content_type='multipart/form-data')
    assert message in response.data


@pytest.mark.parametrize(('usr', 'pwd', 'message'), (
    ('', '', b'false'),
    ('usrname', '', b'false'),
    ('init', 'rightpwd', b'true'),
))
def test_sign_in(client, usr, pwd, message):
    response = client.post('/auth/signin', data={'usr': usr, 'pwd': pwd})
    assert message in response.data


def test_logout(client):
    response = client.get('/auth/logout')
    assert response.status_code == 200
    assert b'Success' in response.data
