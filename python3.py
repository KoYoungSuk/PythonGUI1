import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic


UI_class = uic.loadUiType("pythongui2.ui")[0]


class MyWindow(QMainWindow, UI_class) :
    def __init__(self) :
        super().__init__()
        self.setupUi(self)

        self.pushButton.clicked.connect(self.pushed)
        self.pushButton_2.clicked.connect(self.pushed2)

    def pushed(self):
        self.label_2.setText("This is Python")
    def pushed2(self):
        sys.exit()

app = QApplication(sys.argv)

Window = MyWindow()

Window.show()

app.exec_()