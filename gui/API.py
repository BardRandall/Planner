import requests
import json

server = 'http://yandexplanner.pythonanywhere.com/api/'

error_base = {
    1: 'Ошибка сервера',
    2: 'Пустые данные',
    3: 'Пользователь с таким логином уже существует',
    4: 'Нет пользователя с таким логином',
    5: 'Неверный логин или пароль',
    6: 'Токена не существует',
    7: 'Родительский таск не существует',
    8: 'Ошибка доступа',
    9: 'Короткий пароль',
    10: 'Нет родительских тасков',  # useless
    11: 'Неверный приоритет',
    12: 'Некорректные входные данные',
    13: 'Ошибка доступа'
}


class Error:

    def __init__(self, code, desc):
        self.code = code
        self.native_desc = desc
        if code in error_base:
            self.desc = error_base[code]
        else:
            self.desc = 'Неизвестная ошибка'

    def __repr__(self):
        return 'Error {}: {}'.format(self.code, self.native_desc)

    def __bool__(self):
        return False


class API:

    @staticmethod
    def _get_answer(method, **args):
        req = requests.get(server + method, params=args).content
        res = json.loads(req)
        if res['ok']:
            return res['object']
        return Error(res['error']['code'], res['error']['desc'])

    def __init__(self):
        self.token = None

    def is_logged_in(self):
        return self.token is not None

    def logout(self):
        if self.is_logged_in():
            self._get_answer('logout', token=self.token)
            self.token = None

    def register(self, login, password):
        res = self._get_answer('register', login=login, password=password)
        if type(res) != Error:
            if self.is_logged_in():
                self.logout()
            self.token = res['token']
            return True
        return res

    def login(self, login, password):
        res = self._get_answer('login', login=login, password=password)
        if type(res) != Error:
            if self.is_logged_in():
                self.logout()
            self.token = res['token']
            return True
        return res

    def create_task(self, name, parent_id=None, description='', priority=3):
        if parent_id is None:
            res = self._get_answer('tasks/create', token=self.token, name=name, description=description,
                                   priority=priority)
        else:
            res = self._get_answer('tasks/create', token=self.token, name=name, parent_id=parent_id,
                                   description=description, priority=priority)
        if type(res) != Error:
            return True
        return res

    def get_user_tasks(self):
        return self._get_answer('tasks/get_by_user', token=self.token)

    def get_related(self, task_id):
        return self._get_answer('tasks/get_related', token=self.token, id=task_id)

    def update(self, task_id, name=None, description=None, priority=None):
        query_data = {}
        if name is not None:
            query_data['name'] = name
        if description is not None:
            query_data['description'] = description
        if priority is not None:
            query_data['priority'] = priority
        return self._get_answer('tasks/update', token=self.token, id=task_id, **query_data)

    def delete(self, task_id):
        return self._get_answer('tasks/delete', token=self.token, id=task_id)

    def set_token(self, token):
        res = self._get_answer('check_token', token=token)
        if type(res) != Error:
            self.token = token
            return True
        return False
