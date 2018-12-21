from web.main import app
from flask import request
from web.Adapters import check_args, generate_answer, \
    query, myhash, get_token, check_token, process_task_list, get_update_sql


required_task_fields = '`id`, `name`, `parent_id`, `progress`, `description`, `priority`'


@app.route('/')
def index():
    return 'Main page project'


@app.route('/api/register', methods=['GET'])
def register():
    if check_args(request.args, 'login', 'password'):
        login = request.args['login']
        password = request.args['password']
        if query('SELECT * FROM users WHERE `login`="{}"'.format(login), True):
            return generate_answer(False, error_code=3)
        if len(password) < 6:
            return generate_answer(False, error_code=9)
        query('INSERT INTO users (`login`, `password`) VALUES ("{}", "{}")'.format(login, myhash(password)))
        return generate_answer(True, {'token': get_token(login)})
    return generate_answer(False, error_code=2)


@app.route('/api/login', methods=['GET'])  # create from one to four different tokens of different users
def log_in():  # but return is correct
    if check_args(request.args, 'login', 'password'):  # just a magic
        login = request.args['login']
        password = request.args['password']
        res = query('SELECT * FROM users WHERE `login`="{}"'.format(login), True)
        if not res:
            return generate_answer(False, error_code=4)
        user_pass = res[0][2]
        if myhash(password) != user_pass:
            return generate_answer(False, error_code=5)
        return generate_answer(True, {'token': get_token(login)})
    return generate_answer(False, error_code=2)


@app.route('/api/logout', methods=['GET'])
def logout():
    if check_args(request.args, 'token'):
        token = request.args['token']
        res = query('SELECT * FROM sessions WHERE `token`="{}"'.format(token), True)
        if not res:
            return generate_answer(False, error_code=6)
        query('DELETE FROM sessions WHERE `token`="{}"'.format(token))
        return generate_answer(True, {})
    return generate_answer(False, error_code=2)


@app.route('/api/tasks/create', methods=['GET'])  # TODO support of deadlines
def create():
    if not check_args(request.args, 'token', 'name'):
        return generate_answer(False, error_code=2)
    token = request.args['token']
    name = request.args['name']
    description = ''
    parent_id = 'NULL'
    # deadline = 'NULL'
    priority = 3
    user_id = check_token(token)
    if not user_id:
        return generate_answer(False, error_code=6)
    if check_args(request.args, 'description'):
        description = request.args['description']
    if check_args(request.args, 'parent_id'):
        parent_id = request.args['parent_id']
        res = query('SELECT * FROM tasks WHERE `id`="{}"'.format(parent_id), True)
        if not res:
            return generate_answer(False, error_code=7)
        if res[0][1] != user_id:
            return generate_answer(False, error_code=8)
    if check_args(request.args, 'priority'):
        priority = request.args['priority']
    query('INSERT INTO tasks (`user_id`, `name`, `parent_id`, `description`, `priority`) VALUES ({}, "{}", {}, "{}", {})'
          .format(user_id, name, parent_id, description, priority))
    return generate_answer(True, {})


@app.route('/api/tasks/get_by_user', methods=['GET'])  # TODO deadline
def get_by_user():
    if not check_args(request.args, 'token'):
        return generate_answer(False, error_code=2)
    user_id = check_token(request.args['token'])
    if not user_id:
        return generate_answer(False, error_code=6)
    res = query('SELECT {} FROM tasks WHERE `user_id`={}'.format(required_task_fields, user_id),
                True)
    return generate_answer(True, process_task_list(res))


@app.route('/api/tasks/get_related', methods=['GET'])
def get_related():
    if not check_args(request.args, 'token', 'id'):
        return generate_answer(False, error_code=2)
    user_id = check_token(request.args['token'])
    if not user_id:
        return generate_answer(False, error_code=6)
    try:
        task_id = int(request.args['id'])
    except ValueError:
        return generate_answer(False, error_code=12)
    res = query('SELECT {} FROM tasks WHERE `user_id`={} AND `parent_id`={}'
                .format(required_task_fields, user_id, task_id), True)
    return generate_answer(True, process_task_list(res))


@app.route('/api/tasks/update', methods=['GET'])  # check type
def update():
    if not check_args(request.args, 'id', 'token'):
        return generate_answer(False, error_code=2)
    try:
        task_id = int(request.args['id'])
    except ValueError:
        return generate_answer(False, error_code=12)
    user_id = check_token(request.args['token'])
    if not user_id:
        return generate_answer(False, error_code=6)
    res = query('SELECT * FROM tasks WHERE `id`={} AND `user_id`="{}"'.format(task_id, user_id), True)
    if not res:
        return generate_answer(False, error_code=13)
    name, description, priority = None, None, None
    if check_args(request.args, 'name'):
        name = request.args['name']
    if check_args(request.args, 'description'):
        description = request.args['description']
    if check_args(request.args, 'priority'):
        priority = request.args['priority']
        try:
            priority = int(priority)
        except ValueError:
            return generate_answer(False, error_code=12)
        if priority > 5 or priority < 1:
            return generate_answer(False, error_code=11)
    if name is None and description is None and priority is None:
        return generate_answer(False, error_code=2)
    query(get_update_sql(task_id, name, description, priority))
    return generate_answer(True, {})


@app.route('/api/tasks/delete', methods=['GET'])
def delete():
    if not check_args(request.args, 'token', 'id'):
        return generate_answer(False, error_code=2)
    try:
        task_id = int(request.args['id'])
    except ValueError:
        return generate_answer(False, error_code=12)
    user_id = check_token(request.args['token'])
    if not user_id:
        return generate_answer(False, error_code=6)
    res = query('SELECT * FROM tasks WHERE `id`={} AND `user_id`={}'.format(task_id, user_id), True)
    if not res:
        return generate_answer(False, error_code=13)
    query('DELETE FROM tasks WHERE `id`={0} OR `parent_id`={0}'.format(task_id))
    return generate_answer(True, {})


@app.errorhandler(404)
def page_not_found(e):
    return 'Page not found - my own page'
