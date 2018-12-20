import sys
from Planner.gui.API import API
from PyQt5 import uic
from PyQt5.QtWidgets import QWidget, QHBoxLayout, QApplication, QPushButton, \
    QLabel, \
    QLCDNumber, QLineEdit, QMainWindow


class Example(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.login_sr = ''
        self.password_sr = ''

    def initUI(self):
        uic.loadUi('The Imperor planner.ui', self)
        self.bpass.clicked.connect(self.run_pass)




    def run_pass(self):
        self.login_sr = self.login.text()
        self.password_sr = self.password.text()


if __name__ == '__main__':
    api = API()
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec_())
