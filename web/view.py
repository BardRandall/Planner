from web.app import app
from flask import request
from web.Adapters import check_args, generate_answer, query, myhash
#from web.MySQL import db

'''
class Database:

    def __init__(self):
        pass

    def cursor(self):
        return self

    def execute(self):
        return None

    def fetchall(self):
        return []


db = Database()
'''
# database class for testing offline

@app.route('/')
def index():
    return 'Main page project'


@app.route('/api/register', methods=['GET'])
def register():
    if check_args(request.args, 'login', 'password'):
        login = request.args['login']
        password = request.args['login']
        if query(db, 'SELECT * FROM users WHERE `login`="{}"'.format(login), True):
            return generate_answer(False, error_code=3)
        query(db, 'INSERT INTO users (`login`, `password`) VALUES ("{}", "{}")'.format(login, myhash(password)))
        return generate_answer(True, {})
    return generate_answer(False, error_code=2)


@app.route('/api/login', methods=['GET'])
def log_in():
    if 'login' in request.args and \
            'password' in request.args:
        return 'Login with login {} and password {}'.format(request.args['login'], request.args['password'])
    return 'Incorrect'


@app.route('/api/logout', methods=['GET'])
def logout():
    if 'token' in request.args:
        return 'Removing token {}'.format(request.args['token'])
    return 'Incorrect'


@app.route('/api/tasks/create', methods=['GET'])
def create():
    if 'token' in request.args and \
            'name' in request.args:
        return 'Created {} task'.format(request.args['name'])
    return 'Incorrect'


@app.route('/api/tasks/get_by_user', methods=['GET'])
def get_by_user():
    if 'token' in request.args:
        return 'Got tasks for token ' + request.args['token']
    return 'Incorrect'


@app.errorhandler(404)
def page_not_found():
    return 'Page not found - my own page'
