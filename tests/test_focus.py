# Black Box Testing with Equivalence Class Partitioning
import pytest


@pytest.mark.parametrize(('emotion', 'vector', 'position', 'course_id','message'), (
    ('-10', '0', '0', '123', b'Invalid Emotion Input'),
    ('10', '0', '0', '123', b'Success'),
    ('110', '0', '0', '123', b'Invalid Emotion Input'),
    ('10', '-30', '0', '123', b'Invalid Gaze Input'),
    ('10', '30', '0', '123', b'Invalid Gaze Input'),
    ('10', '0', '-30', '123', b'Invalid Gaze Input'),
    ('10', '0', '30', '123', b'Invalid Gaze Input'),
    ('10', '10', '10', '111', b'Success')
))
def test_add_focus(app, auth, client, emotion, vector, position, course_id, message):
    data = {'anger': emotion,
            'disgust': emotion,
            'fear': emotion,
            'happiness': emotion,
            'neutral': emotion,
            'sadness': emotion,
            'surprise': emotion,
            'vector_x': vector,
            'vector_y': vector,
            'vector_z': vector,
            'position_x': position,
            'position_y': position,
            'course_id': course_id,
            'time': '123'
    }
    with app.app_context(): # to prevent droping database
        auth.login()
        response = client.get('/focus/add', query_string=data)
        assert message in response.data

@pytest.mark.parametrize(('course_id', 'message'), (
    ('111', b'111'),
    ('234', b'None'),
))
def test_get_focus(app, auth, client, course_id, message):
    with app.app_context():
        auth.login()
        response = client.get('/focus/get', query_string={'course_id': course_id})
        assert message in response.data


@pytest.mark.parametrize(('course_id', 'message'), (
    ('111', b'111'),
    ('234', b'None'),
))
def test_get_avg_focus(app, auth, client, course_id, message):
    with app.app_context():
        auth.login()
        response = client.get('/focus/getavg', query_string={'course_id': course_id})
        assert message in response.data

def test_invalid_usr(app, client):
    with app.app_context():
        response = client.get('focus/getavg', query_string={'course_id': '111'})
        assert b'Invalid User' in response.data


@pytest.mark.parametrize(('course_id', 'rate', 'message'), (
    ('111', -3, b'Invalid Rating'),
    ('111', 3, b'Success'),
    ('111', 8, b'Invalid Rating'),
    ('234', 3, b'None')
))
def test_rate(app, auth, client, course_id, rate, message):
    with app.app_context():
        auth.login()
        response = client.get('/focus/rate', query_string={'course_id': course_id, 'rate': rate})
        assert message in response.data
        