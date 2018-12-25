from PyQt5 import uic, QtCore
from Planner.gui.API import Error
from functools import partial
from PyQt5.QtCore import QCoreApplication


def run_login(obj, api):
    login = obj.loginEdit.text()
    password = obj.passEdit.text()
    res = api.login(login, password)
    if type(res) == Error:
        obj.errorLabel.setText(res.desc)
    else:
        if obj.rememberCheck.isChecked():
            with open('token.data', mode='w+') as f:
                f.write(api.token)
        obj.errorLabel.setText('')
        obj.change_scene('tasks')


def run_reg(obj):
    obj.change_scene('register')


def init(obj, api):
    uic.loadUi('login.ui', obj)
    obj.loginButton.clicked.connect(partial(run_login, obj, api))
    obj.regButton.clicked.connect(partial(run_reg, obj))

