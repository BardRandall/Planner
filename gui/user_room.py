from PyQt5 import uic
from gui.API import Error
from functools import partial

def create(obj, api):
   obj.change_scene('newone')

def init(obj, api):
    uic.loadUi('user_window.ui', obj)
    obj.creator.clicked.connect(partial(create, obj, api))
