import sys
from Planner.gui.API import API
from Planner.gui.registration import Registration
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow


class Door(Registration):

    def __init__(self):
        global ex
        super().__init__()
        Registration().__init__()
        self.initUI()
        self.login_sr = None
        self.password_sr = None


    def initUI(self):
        uic.loadUi('login.ui', self)
        self.bpass.clicked.connect(self.run_pass)
        self.help.clicked.connect(self.reg_run)





    def run_pass(self):
        self.login_sr = self.login_input.text()
        self.password_sr = self.password_input.text()
        res = api.login(self.login_sr, self.password_sr)
        if type(res) not in self.errors:
            pass

    def reg_run(self):
        uic.loadUi('registration.ui', self)




    def save_initialization(self):
        api.register(Registration.log.text(), Registration.pasw.text())



if __name__ == '__main__':
    api = API()
    app = QApplication(sys.argv)
    ex = Door()
    ex.show()
    sys.exit(app.exec_())
