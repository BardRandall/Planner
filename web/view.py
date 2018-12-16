from web.app import app
from flask import request
from web.Adapters import check_args, generate_answer, query, myhash, get_token
from web.MySQL import db


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
        return generate_answer(True, {'token': get_token(db, login)})
    return generate_answer(False, error_code=2)


@app.route('/api/login', methods=['GET'])
def log_in():
    if check_args(request.args, 'login', 'password'):
        login = request.args['login']
        password = request.args['password']
        res = query(db, 'SELECT * FROM users WHERE `login`="{}"'.format(login), True)
        if not res:
            return generate_answer(False, error_code=4)
        user_pass = res[0][2]
        if myhash(password) != user_pass:
            return generate_answer(False, error_code=5)
        return generate_answer(True, {'token': get_token(db, login)})
    return generate_answer(False, error_code=2)


@app.route('/api/logout', methods=['GET'])
def logout():
    if check_args(request.args, 'token'):
        token = request.args['token']
        res = query(db, 'SELECT * FROM sessions WHERE `token`="{}"'.format(token), True)
        if not res:
            return generate_answer(False, error_code=6)
        query(db, 'DELETE FROM sessions WHERE `token`="{}"'.format(token))
        return generate_answer(True, {})
    return generate_answer(False, error_code=2)


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


@app.route('/api/tasks/get_related', methods=['GET'])
def get_related():
    pass


@app.route('/api/tasks/update', methods=['GET'])
def update():
    pass


@app.errorhandler(404)
def page_not_found(e):
    return 'Page not found - my own page'
