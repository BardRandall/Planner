from PyQt5 import uic
from gui.API import Error
from functools import partial


def run_reg(obj, api):
    login = obj.lineEdit.text()
    password = obj.lineEdit_2.text()
    res = api.login(login, password)
    if type(res) == Error:
        pass
    else:
        obj.lineEdit.setText('Login successful')


def init(obj, api):
    uic.loadUi('login.ui', obj)
    obj.pushButton.clicked.connect(partial(run_reg, obj, api))
