from PyQt5 import uic, QtCore
import os.path
from gui.API import Error
from functools import partial


def run_logout(obj, api):
    api.logout()
    with open('token.data', mode='w+') as f:
        f.write('')
    obj.change_scene('login')


def init(obj, api):
    uic.loadUi('tasks.ui', obj)
    obj.logoutButton.clicked.connect(partial(run_logout, obj, api))
