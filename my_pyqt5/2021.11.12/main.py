import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
from MyExcel import MyExcel

form_class = uic.loadUiType("assignment.ui")[0]


class WindowClass(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.mex = MyExcel()

        self.savebtn.clicked.connect(self.savefn)
        self.loadbtn.clicked.connect(self.loadfn)
        self.createbtn.clicked.connect(self.createfn)

    def savefn(self):
        try:
            kor = self.koredit.text()
            eng = self.engedit.text()
            math = self.mathedit.text()
            tot = int(kor) + int(eng) + int(math)
            avg = tot / 3

            print('tot = ', tot)
            print('avg = ', avg)
            self.mex.savefn(kor,eng,math,tot,avg)
        except Exception as e:
            print(e)

    def loadfn(self):
        self.mex.loadfn()

    def createfn(self):
        try:
            self.mex.createfn()
        except Exception as e:
            print(e)


if __name__ == "__main__":
    app = QApplication(sys.argv)

    myWindow = WindowClass()

    myWindow.show()

    app.exec_()
