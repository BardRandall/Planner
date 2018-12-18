import requests
import json

server = 'http://yandexplanner.pythonanywhere.com/api/'


class Error:

    def __init__(self, code, desc):
        self.code = code
        self.desc = desc

    def code(self):
        return self.code

    def desc(self):
        return self.desc

    def __repr__(self):
        return 'Error {}: {}'.format(self.code, self.desc)


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
            res = self._get_answer('tasks/create', name=name, parent_id=parent_id,
                                   description=description, priority=priority)
        if type(res) != Error:
            return True
        return res

    def get_user_tasks(self):
        return self._get_answer('tasks/get_by_user', token=self.token)

    def get_related(self, task_id):
        return self._get_answer('tasks/get_related', token=self.token, id=task_id)
