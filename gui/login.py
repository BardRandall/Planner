from PyQt5 import uic
from gui.API import Error
from functools import partial


def run_login(obj, api):
    login = obj.loginEdit.text()
    password = obj.passEdit.text()
    res = api.login(login, password)
    if type(res) == Error:
        if res.code == 2:
            obj.errorLabel.setText('Логин или пароль пустые')
        elif res.code == 4:
            obj.errorLabel.setText('Такого пользователя не существует')
        elif res.code == 5:
            obj.errorLabel.setText('Логин или пароль не верный')
        else:
            obj.errorLabel.setText('Неизвестная ошибка')
    else:
        obj.loginEdit.setText('Login successful')


def run_reg(obj):
    obj.change_scene('register')


def init(obj, api):
    uic.loadUi('login.ui', obj)
    obj.loginButton.clicked.connect(partial(run_login, obj, api))
    obj.regButton.clicked.connect(partial(run_reg, obj))
