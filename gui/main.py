import sys
from gui.API import API
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow
from gui.login import init as login_init


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        login_init(self, api)


if __name__ == '__main__':
    api = API()
    app = QApplication(sys.argv)
    ex = MainWindow()
    ex.show()
    sys.exit(app.exec_())
