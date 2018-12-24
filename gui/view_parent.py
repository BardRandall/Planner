from PyQt5 import uic, QtCore
import os.path
from gui.API import Error
from functools import partial
from PyQt5.QtWidgets import QHBoxLayout, QLineEdit, QProgressBar, QPushButton, QLabel, QGridLayout
from PyQt5 import QtCore
from gui.creator import init as creator_init
from gui.edit import init as edit_init


def run_logout(obj, api):
    api.logout()
    with open('token.data', mode='w+') as f:
        f.write('')
    obj.change_scene('login')


def create(obj, api, id):
    creator_init(obj, api, id)


def delete(obj, api, id):
    api.delete(id)
    init(obj, api)


def create_linked(obj, api, id):
    creator_init(obj, api, id)


def edit(obj, api, id, name, desc, priority):
    edit_init(obj, api, id, name, desc, priority)


def view_parent(obj, api, id, name):
    init(obj, api, id, name)


def load_tasks(obj, api, id):
    res = api.get_user_tasks()
    if not res:
        obj.noTasksLabel.setText('У вас нет подзадач')
    else:
        obj.noTasksLabel.setText('')
    deny = 0
    for i in range(len(res)):
        if res[i]['parent_id'] != id:
            deny += 1
            continue
        if res[i]['progress'] is None:
            res[i]['progress'] = 0
        name_obj = QLabel(res[i]['name'])
        progress_object = QProgressBar()
        progress_object.setValue(res[i]['progress'])
        btn_show = QPushButton('Смотреть подзадачи')
        btn_show.clicked.connect(partial(view_parent, obj, api, res[i]['id'], res[i]['name']))
        btn_edit = QPushButton('Редактировать')
        btn_edit.clicked.connect(partial(edit, obj, api, res[i]['id'], res[i]['name'], res[i]['description'], res[i]['priority']))
        btn_delete = QPushButton('Удалить')
        btn_delete.clicked.connect(partial(delete, obj, api, res[i]['id']))
        obj.gridLayout.addWidget(name_obj, i, 0)
        obj.gridLayout.addWidget(progress_object, i, 1)
        obj.gridLayout.addWidget(btn_show, i, 2)
        obj.gridLayout.addWidget(btn_edit, i, 3)
        obj.gridLayout.addWidget(btn_delete, i, 4)
    if deny == len(res):
        obj.noTasksLabel.setText('У вас нет подзадач')


def to_tasks(obj):
    obj.change_scene('tasks')


def init(obj, api, id=None, name=''):
    uic.loadUi('tasks.ui', obj)
    obj.logoutButton.clicked.connect(partial(run_logout, obj, api))
    obj.creator.clicked.connect(partial(create, obj, api, id))
    obj.backButton.setEnabled(True)
    obj.backButton.clicked.connect(partial(to_tasks, obj))
    obj.titleLabel.setText('Подзадания для {}'.format(name))
    load_tasks(obj, api, id)
