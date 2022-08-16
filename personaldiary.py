import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
import os
import cx_Oracle as oracle
from tkinter import messagebox


UI_class = uic.loadUiType("pythongui5.ui")[0]


class MyWindow(QMainWindow, UI_class) :
    def __init__(self) :
        super().__init__()
        self.setupUi(self)

        self.pushButton.clicked.connect(self.executebtn)
        self.pushButton_2.clicked.connect(self.closebtn)

    def executebtn(self):
        location = self.lineEdit.text()
        address = self.lineEdit_2.text()
        dbid = self.lineEdit_3.text()
        password = self.lineEdit_4.text()
        try:
            os.environ["PATH"] = location + ";" + os.environ["PATH"]
            conn = oracle.connect(dbid, password, address)
            cur = conn.cursor()
            self.label_7.setText("STATUS: Success Connected.")
            title = self.lineEdit_5.text()
            content = self.textEdit.toPlainText().replace(" ", "\n")
            sql = "insert into diary values (:1, :2, sysdate, null)"
            val = (title, content)
            cur.execute(sql, val)
            messagebox.showinfo("PersonalDiary Python", "Successfully Written.")
            cur.close()
            conn.commit()
            conn.close()
        except Exception as e:
            print(e)
            self.label_7.setText("STATUS: " + str(e))
            messagebox.showerror("PersonalDiary Python", str(e))
    def closebtn(self):
        sys.exit()

app = QApplication(sys.argv)

Window = MyWindow()

Window.show()

app.exec_()