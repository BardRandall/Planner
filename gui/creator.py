from PyQt5 import uic
from gui.API import Error
from functools import partial
def save_create(obj, api):
        name = obj.title_row.text()
        plan = obj.plans.text()
        a = api.create_task(name, parent_id=None, description=plan)

        if type(a) == Error:
            obj.title_error.setText(a.desc)

        else:
            obj.change_scene('tasks')

def init(obj, api):
    uic.loadUi('newone.ui', obj)
    obj.okey.clicked.connect(partial(save_create, obj, api))

