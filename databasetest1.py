import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic   # ui 파일을 사용하기 위한 모듈 import
import os
import cx_Oracle as oracle
import pandas as pd

#UI파일 연결 코드
UI_class = uic.loadUiType("pythongui4.ui")[0]


class MyWindow(QMainWindow, UI_class) :
    def __init__(self) :
        super().__init__()
        self.setupUi(self)

        self.pushButton.clicked.connect(self.executebtn)
        self.pushButton_2.clicked.connect(self.closebtn)

    def executebtn(self):
        self.textBrowser.clear()
        location = self.lineEdit.text()
        address = self.lineEdit_2.text()
        dbid = self.lineEdit_3.text()
        password = self.lineEdit_4.text()
        try:
            os.environ["PATH"] = location + ";" + os.environ["PATH"]
            conn = oracle.connect(dbid, password, address)
            cur = conn.cursor()
            self.label_7.setText("STATUS: Success Connected.")
            sql = self.textEdit_5.toPlainText()
            cur.execute(sql)
            self.label_7.setText("STATUS: Success Executed.")
            pd.set_option('display.max_columns', None)
            pd.set_option('display.max_rows', None)
            df = pd.read_sql(sql, con=conn)
            self.textBrowser.append(str(df))
            ##for row in cur:
            ##   for x in row:
            ##  self.textBrowser.append(str(x))
        except Exception as e:
            print(e)
            self.label_7.setText("STATUS: " + str(e))
    def closebtn(self):
        sys.exit()

app = QApplication(sys.argv)

Window = MyWindow()

Window.show()

app.exec_()