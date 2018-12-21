import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow
from gui.run import change_scene_to


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('login.ui',self)
        self.pushButton.clicked.connect(self.run)

    def run(self):
        uic.loadUi('register.ui', self)



if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
