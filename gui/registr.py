from PyQt5 import uic
from Planner.gui.API import Error
from functools import partial
from Planner.gui.login import init as login_init

def initialization(obj, api):
    new_login = obj.log.text()
    new_password = obj.pasw.text()
    res = api.login(new_login, new_password)
    if type(res) == Error:
        pass
    else:
        obj.login_input.setText('Registaration successful')


def change2(obj, api):
    uic.loadUi('The Imperor planner.ui', obj)
    login_init(obj, api)

def init(obj, api):
    uic.loadUi('registration.ui', obj)
    obj.saver.clicked.connect(partial(initialization, obj, api))

