import json
import hashlib
import random
import datetime
import pymysql
import pymysql.cursors
from Planner.web.config import db_host, db_user, db_pass, db_name


db = pymysql.connect(db_host, db_user, db_pass, db_name)
salt = 'saltforpasswords'


def init_db():
    global db
    db.close()
    db = pymysql.connect(db_host, db_user, db_pass, db_name)


error_base = {
    1: 'Server Error',
    2: 'Required args empty',
    3: 'Such user already exists',
    4: 'No such user',
    5: 'Incorrect password',
    6: 'No such token',
    7: 'Parent task don\'t exists',
    8: 'You can\'t inherit from someone else\'s task',
    9: 'Short password',
    10: 'No related tasks',  # useless
    11: 'Bad priority',
    12: 'Incorrect input type',
    13: 'Access error'
}


def check_args(request, *args):
    for arg in args:
        if arg not in request:
            return False
        if request[arg] == '':
            return False
    return True


def generate_answer(success, obj=None, error_code=1):
    if success:
        res = {'ok': success, 'object': obj}
    else:
        res = {'ok': success, 'error': {'code': error_code, 'desc': error_base[error_code]}}
    return json.dumps(res)


def base_query(sql, is_return):
    cursor = db.cursor()
    cursor.execute(sql)
    if is_return:
        res = cursor.fetchall()
        cursor.close()
        print('Success return: ' + sql)
        return res
    cursor.execute('COMMIT;')
    cursor.close()
    print('Success: ' + sql)


def query(sql, is_return=False):
    try:
        return base_query(sql, is_return)
    except Exception:
        print('Trying to reconnect...')
        init_db()
        return base_query(sql, is_return)


def myhash(data):
    return hashlib.md5((data + salt).encode('utf-8')).hexdigest()


def get_token(login):
    token = hashlib.md5((login + str(random.randint(0, 255)) + str(datetime.datetime.now()) + salt).encode('utf-8')).hexdigest()
    user_id = query('SELECT `id` FROM users WHERE `login`="{}"'.format(login), True)[0][0]
    query('INSERT INTO sessions (`token`, `user_id`) VALUES ("{}", {})'.format(token, user_id))
    return token


def check_token(token):
    res = query('SELECT * FROM sessions WHERE `token`="{}"'.format(token), True)
    if not res:
        return False
    return res[0][2]


def process_task(task):
    return {
        'id': task[0],
        'name': task[1],
        'parent_id': task[2],
        'progress': task[3],
        'description': task[4],
        'priority': task[5],
        'has_related': bool(task[6])
    }


def process_task_list(task_list):
    res = []
    for task in task_list:
        t = list(task) + [query('SELECT * FROM tasks WHERE `parent_id`={}'.format(task[0]), True)]
        res.append(process_task(t))
    return res


def get_update_sql(task_id, name, description, priority, progress):
    sql = 'UPDATE `tasks` SET '
    sql_data = []
    if name is not None:
        sql_data.append('`name`="{}"'.format(name))
    if description is not None:
        sql_data.append('`description`="{}"'.format(description))
    if priority is not None:
        sql_data.append('`priority`={}'.format(priority))
    if progress is not None:
        sql_data.append('`progress`={}'.format(progress))
    sql += ', '.join(sql_data) + ' '
    sql += 'WHERE `id`={}'.format(task_id)
    return sql
