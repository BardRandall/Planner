from PyQt5 import uic
from Planner.gui.API import Error
from functools import partial
from PyQt5.QtCore import QCoreApplication


def run_reg(obj, api):
    login = obj.login_input.text()
    password = obj.password_input.text()
    res = api.login(login, password)
    if type(res) == Error:
        pass
    else:
        obj.login_input.setText('Login successful')
        obj.change_scence('user_window')


def change(obj, api):
    obj.change_scene('registr')


def init(obj, api):
    uic.loadUi('login.ui', obj)
    obj.bpass.clicked.connect(partial(run_reg, obj, api))
    obj.help.clicked.connect(partial(change, obj, api))
    obj.lostpw.clicked.connect(QCoreApplication.instance().quit)
