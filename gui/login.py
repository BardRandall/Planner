from PyQt5 import uic
from gui.API import Error
from functools import partial


def run_login(obj, api):
    login = obj.lineEdit.text()
    password = obj.lineEdit_2.text()
    res = api.login(login, password)
    if type(res) == Error:
        pass
    else:
        obj.lineEdit.setText('Login successful')


def run_reg(obj):
    obj.change_scene('register')


def init(obj, api):
    uic.loadUi('login.ui', obj)
    obj.loginButton.clicked.connect(partial(run_login, obj, api))
    obj.regButton.clicked.connect(partial(run_reg, obj))
