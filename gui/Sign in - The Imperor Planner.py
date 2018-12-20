import sys
from Planner.gui.API import API
from Planner.gui.registration import Registration
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow


class Door(QMainWindow):

    def __init__(self):
        super().__init__()
        self.initUI()
        self.login_sr = None
        self.password_sr = None
        self.errors = {1: 'Server Error', 2: 'Required args empty',3: 'Such user already exists',4: 'No such user',5: 'Incorrect password',6: 'No such token',
        7: 'Parent task dont exists',
        8: 'You cant inherit from someone elses task',
        9: 'Short password',
        10: 'No related tasks',  # useless
        11: 'Bad priority',
        12: 'Incorrect input type',
        13: 'Access error'
        }
    def initUI(self):
        uic.loadUi('The Imperor planner.ui', self)
        self.bpass.clicked.connect(self.run_pass)
        self.help.clicked.connect(self.reg_run)



    def run_pass(self):
        self.login_sr = self.login_input.text()
        self.password_sr = self.password_input.text()
        res = api.login(self.login_sr, self.password_sr)
        if type(res) not in self.errors:
            pass

    


if __name__ == '__main__':
    api = API()
    app = QApplication(sys.argv)
    ex = Door()
    ex.show()
    sys.exit(app.exec_())
