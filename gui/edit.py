from PyQt5 import uic
from gui.API import Error
from functools import partial


def save_edit(obj, api, id):
    name = obj.nameEdit.text()
    desc = obj.descEdit.toPlainText()
    priority = obj.priorityBox.currentText()
    res = api.update(id, name, description=desc, priority=priority)
    if type(res) == Error:
        obj.errorLabel.setText(res.desc)
    else:
        obj.change_scene('tasks')


def go_back(obj):
    obj.change_scene('tasks')


def init(obj, api, id=None, name='', desc='', priority=3):
    uic.loadUi('change.ui', obj)
    obj.nameEdit.setText(name)
    obj.descEdit.setPlainText(desc)
    obj.priorityBox.setCurrentIndex(priority - 1)
    obj.editButton.clicked.connect(partial(save_edit, obj, api, id))
    obj.cancelButton.clicked.connect(partial(go_back, obj))
