import sys
from Planner.gui.API import API
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow
from Planner.gui.login import init as login_init
from Planner.gui.registr import init as registr_init


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        login_init(self, api)



    def closeEvent(self, QCloseEvent):
        api.logout()

    def change_scene(self, name):
        eval('{}_init(self, api)'.format(name))


if __name__ == '__main__':
    api = API()
    app = QApplication(sys.argv)
    ex = MainWindow()
    ex.show()
    sys.exit(app.exec_())
