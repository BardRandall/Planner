from web.app import app
from flask import request


@app.route('/')
def index():
    return 'Main page project'


@app.route('/api/register', methods=['GET'])
def register():
    if 'login' in request.args and \
            'password' in request.args:
        return 'Register with login {} and password {}'.format(request.args['login'], request.args['password'])
    return 'Incorrect'


@app.route('/api/login', methods=['GET'])
def login():
    if 'login' in request.args and \
            'password' in request.args:
        return 'Login with login {} and password {}'.format(request.args['login'], request.args['password'])
    return 'Incorrect'
