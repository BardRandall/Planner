from PyQt5 import uic, QtCore
import os.path
from Planner.gui.API import Error
from functools import partial
from PyQt5.QtWidgets import QHBoxLayout, QLineEdit, QProgressBar, QPushButton, QLabel, QGridLayout
from PyQt5 import QtCore


def run_logout(obj, api):
    api.logout()
    with open('token.data', mode='w+') as f:
        f.write('')
    obj.change_scene('login')


def create(obj, api):
    obj.change_scene('creator')


def add_task(obj, api):
    a = api.get_user_tasks()
    for i in range(len(a)):
        name_n = QLabel(a[i]['name'])
        progress = QProgressBar[a[i]['progress']]
        obj.gridLayout.addWidget(name_n, i, 0)
        obj.gridLayout.addWidget(name_n, i, 1)
        obj.gridLayout.addWidget('{}_'.format(QPushButton('')), i, 0)





def init(obj, api):
    uic.loadUi('tasks.ui', obj)
    obj.logoutButton.clicked.connect(partial(run_logout, obj, api))
    obj.creator.clicked.connect(partial(create, obj, api))
    add_task(obj, api)
