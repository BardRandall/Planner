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

    def initUI(self):
        uic.loadUi('registration.ui', self)
        self.saver.clicked.connect(self.run_save)




    def run_save(self):
        self.log = self.login.text()
        self.pasw = self.password.text()


if __name__ == '__main__':
    api = API()
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec_())
