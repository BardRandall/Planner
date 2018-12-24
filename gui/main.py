import sys
import os.path
from Planner.gui.API import API
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow
from Planner.gui.login import init as login_init
from Planner.gui.tasks import init as tasks_init
from Planner.gui.register import init as register_init
from Planner.gui.creator import init as creator_init
class MainWindow(QMainWindow):


    def __init__(self):
        super().__init__()
        res = ''
        if os.path.exists('token.data'):
            with open('token.data', mode='r+') as f:
                res = f.read()
        if res:
            if api.set_token(res):
                tasks_init(self, api)
                return
        login_init(self, api)

    def closeEvent(self, QCloseEvent):
        res = ''
        if os.path.exists('token.data'):
            with open('token.data', mode='r+') as f:
                res = f.read()
        if not res:
            api.logout()
        login_init(self, api)

    def change_scene(self, name):
        eval('{}_init(self, api)'.format(name))


if __name__ == '__main__':
    api = API()
    app = QApplication(sys.argv)
    ex = MainWindow()
    ex.show()
    sys.exit(app.exec_())
