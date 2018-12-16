import json
import hashlib


salt = 'saltforpasswords'
error_base = {
    1: 'Server Error',
    2: 'Required args empty',
    3: 'Such user already exists'
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
    #cursor.execute(sql)
    cursor.execute('SELECT * FROM users')
    if is_return:
        return cursor.fetchall()


def myhash(data):
    return hashlib.md5((data + salt).encode('utf-8')).hexdigest()
