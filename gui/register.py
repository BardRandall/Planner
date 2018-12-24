from PyQt5 import uic
from gui.API import Error
from functools import partial


def run_reg(obj, api):
    login = obj.loginEdit.text()
    password = obj.passEdit.text()
    rpassword = obj.pass2Edit.text()
    if password != rpassword:
        obj.errorLabel.setText('Пароли разные')
        return
    res = api.register(login, password)
    if type(res) == Error:
        obj.errorLabel.setText(res.desc)
    else:
        obj.errorLabel.setText('')
        obj.change_scene('tasks')


def run_login(obj):
    obj.change_scene('login')


def init(obj, api):
    uic.loadUi('register.ui', obj)
    obj.loginButton.clicked.connect(partial(run_login, obj))
    obj.regButton.clicked.connect(partial(run_reg, obj, api))
