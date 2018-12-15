import sys
from PyQt5 import uic
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QListWidget, QListWidgetItem, QAbstractItemView


class DragAndDropList(QListWidget):
    itemMoved = pyqtSignal(int, int, QListWidgetItem)

    def __init__(self, parent=None, **args):
        super(DragAndDropList, self).__init__(parent)
        self.setAcceptDrops(True)
        self.setDragEnabled(True)
        self.setDragDropMode(QAbstractItemView.InternalMove)
        self.drag_item = None
        self.drag_row = None

    def startDrag(self, supportedActions):
        self.drag_item = self.currentItem()
        self.drag_row = self.row(self.drag_item)
        super(DragAndDropList, self).startDrag(supportedActions)

    def dragEnterEvent(self, event):
        if event.mimeData().hasUrls():
            event.ignore()
        else:
            event.accept()

    def dragMoveEvent(self, event):
        if event.mimeData().hasUrls():
            event.ignore()
        else:
            event.accept()

    def dropEvent(self, event):
        print(dir(event))
        print(dir(event.mimeData()))
        print(event.mimeData().text())
        self.addItem(event.mimeData().text())

    def dropMimeData(self, index, mimedata, action):
        super(DragAndDropList, self).dropMimeData(index, mimedata, action)
        return True


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('main.ui', self)
        self.list1 = DragAndDropList(self)
        self.list1.move(10, 80)
        self.list1.addItem('item 1')
        self.list2 = DragAndDropList(self)
        self.list2.move(270, 80)
        self.list3 = DragAndDropList(self)
        self.list3.move(530, 80)


app = QApplication(sys.argv)
ex = MyWidget()
ex.show()
sys.exit(app.exec_())
