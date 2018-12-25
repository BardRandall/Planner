from PyQt5 import uic
from Planner.gui.API import Error
from functools import partial


def save_create(obj, api, id):
    name = obj.nameEdit.text()
    desc = obj.descEdit.toPlainText()
    priority = obj.priorityBox.currentText()
    res = api.create_task(name, parent_id=id, description=desc, priority=priority)
    if type(res) == Error:
        obj.errorLabel.setText(res.desc)
    else:
        obj.change_scene('tasks')


def go_back(obj):
    obj.change_scene('tasks')


def init(obj, api, id=None):
    uic.loadUi('newone.ui', obj)
    obj.createButton.clicked.connect(partial(save_create, obj, api, id))
    obj.cancelButton.clicked.connect(partial(go_back, obj))
