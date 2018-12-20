import sys
from Planner.gui.API import API
from PyQt5 import uic
from PyQt5.QtWidgets import QWidget, QHBoxLayout, QApplication, QPushButton, \
    QLabel, \
    QLCDNumber, QLineEdit, QMainWindow


class Registration (QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        uic.loadUi('registration.ui', self)
        self.saver.clicked.connect(self.run_save)




    def run_save(self):
        self.login = self.log.text()
        self.password = self.pasw.text()
        print(self.login)
        print(self.password)

if __name__ == '__main__':
    api = API()
    app = QApplication(sys.argv)
    ex = Registration()
    ex.show()
    sys.exit(app.exec_())

