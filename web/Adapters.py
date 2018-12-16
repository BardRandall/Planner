import json
import hashlib
import random
import datetime


salt = 'saltforpasswords'
error_base = {
    1: 'Server Error',
    2: 'Required args empty',
    3: 'Such user already exists',
    4: 'No such user',
    5: 'Incorrect password',
    6: 'No such token'
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


def query(db, sql, is_return=False):
    cursor = db.cursor()
    cursor.execute(sql)
    if is_return:
        return cursor.fetchall()
    cursor.execute('COMMIT;')


def myhash(data):
    return hashlib.md5((data + salt).encode('utf-8')).hexdigest()


def get_token(db, login):
    token = hashlib.md5((login + str(random.randint(0, 255)) + str(datetime.datetime.now()) + salt).encode('utf-8')).hexdigest()
    user_id = query(db, 'SELECT `id` FROM users WHERE `login`="{}"'.format(login), True)[0][0]
    query(db, 'INSERT INTO sessions (`token`, `user_id`) VALUES ("{}", "{}")'.format(token, user_id))
    return token
