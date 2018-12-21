import sys

from PyQt5.QtWidgets import QApplication

current_scene = ''

app = QApplication(sys.argv)
ex = None


def change_scene_to(scene_name, obj):
    global current_scene, ex
    current_scene = scene_name
    if ex is not None:
        ex.close()
    ex = obj()
    ex.show()


if __name__ == '__main__':
    from gui.main import MyWidget
    change_scene_to('login', MyWidget)
    sys.exit(app.exec_())
