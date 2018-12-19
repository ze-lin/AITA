"""
    Micro Server For AITA
"""
import json
from pymongo import MongoClient
from flask import request, Flask

client = MongoClient()
db = client['aita']
member = db['member']

app = Flask(__name__)

@app.route('/signup', methods=['POST'])
def sign_up():
    document = {
        'usr': request.form['usr'],
        'pwd': request.form['pwd']
    }
    member.insert_one(document)
    return 'True'

@app.route('/signin', methods=['POST'])
def sign_in():
    result_filter = {
        'usr': request.form['usr'],
        'pwd': request.form['pwd']
    }
    result = member.find_one(result_filter)
    if result:
        return 'True'
    else:
        return 'False'
