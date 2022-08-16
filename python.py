import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic


UI_class = uic.loadUiType("pythongui.ui")[0]


class MyWindow(QDialog, UI_class) :
    def __init__(self) :
        super().__init__()
        self.setupUi(self)

app = QApplication(sys.argv)

Window = MyWindow()

Window.show()

app.exec_()