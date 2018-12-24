from PyQt5 import uic
from gui.API import Error
from functools import partial


def initialization(obj, api):
    new_login = obj.log.text()
    new_password = obj.pasw.text()
    res = api.register(new_login, new_password)
    if type(res) == Error:
        pass
    else:
        obj.login_input.setText('Registaration successful')


def change2(obj, api):
    obj.change_scene('login')


def init(obj, api):
    uic.loadUi('registration.ui', obj)
    obj.saver.clicked.connect(partial(initialization, obj, api))
    obj.saver.clicked.connect(partial(change2, obj, api))


