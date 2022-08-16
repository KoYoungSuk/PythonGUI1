import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic


UI_class = uic.loadUiType("pythongui3.ui")[0]


class MyWindow(QMainWindow, UI_class) :
    def __init__(self) :
        super().__init__()
        self.setupUi(self)

        self.pushButton.clicked.connect(self.pushed)
        self.pushButton_2.clicked.connect(self.pushed2)
        self.pushButton_3.clicked.connect(self.pushed3)

    def pushed(self):
        #self.windowTitle(self.textEdit.toPlainText())
        self.label.setText(self.textEdit.toPlainText())
    def pushed2(self):
        sys.exit()
    def pushed3(self):
        self.label.setText(self.textEdit_2.toPlainText())

app = QApplication(sys.argv)

Window = MyWindow()

Window.show()

app.exec_()