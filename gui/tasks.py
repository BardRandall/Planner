from PyQt5 import uic, QtCore
import os.path
from gui.API import Error
from functools import partial
from PyQt5.QtWidgets import QHBoxLayout, QLineEdit, QProgressBar, QPushButton, QLabel, QGridLayout
from PyQt5 import QtCore
from gui.creator import init as creator_init
from gui.edit import init as edit_init
from gui.view_parent import init as view_parent_init


def run_logout(obj, api):
    api.logout()
    with open('token.data', mode='w+') as f:
        f.write('')
    obj.change_scene('login')


def create(obj, api):
    obj.change_scene('creator')


def delete(obj, api, id):
    api.delete(id)
    init(obj, api)


def create_linked(obj, api, id):
    creator_init(obj, api, id)


def edit(obj, api, id, name, desc, priority):
    edit_init(obj, api, id, name, desc, priority)


def view_parent(obj, api, id, name):
    view_parent_init(obj, api, id, name)


def load_tasks(obj, api):
    a = api.get_user_tasks()
    if not a:
        obj.noTasksLabel.setText('У вас нет заданий')
    else:
        obj.noTasksLabel.setText('')
    for i in range(len(a)):
        if a[i]['parent_id'] is not None:
            continue
        if a[i]['progress'] is None:
            a[i]['progress'] = 0
        name_obj = QLabel(a[i]['name'])
        progress_object = QProgressBar()
        progress_object.setValue(a[i]['progress'])
        btn_show = QPushButton('Смотреть подзадачи')
        btn_show.clicked.connect(partial(view_parent, obj, api, a[i]['id'], a[i]['name']))
        btn_edit = QPushButton('Редактировать')
        btn_edit.clicked.connect(partial(edit, obj, api, a[i]['id'], a[i]['name'], a[i]['description'], a[i]['priority']))
        btn_delete = QPushButton('Удалить')
        btn_delete.clicked.connect(partial(delete, obj, api, a[i]['id']))
        obj.gridLayout.addWidget(name_obj, i, 0)
        obj.gridLayout.addWidget(progress_object, i, 1)
        obj.gridLayout.addWidget(btn_show, i, 2)
        obj.gridLayout.addWidget(btn_edit, i, 3)
        obj.gridLayout.addWidget(btn_delete, i, 4)


def init(obj, api):
    uic.loadUi('tasks.ui', obj)
    obj.logoutButton.clicked.connect(partial(run_logout, obj, api))
    obj.creator.clicked.connect(partial(create, obj, api))
    load_tasks(obj, api)
