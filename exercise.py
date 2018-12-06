from PyQt5 import QtCore, QtGui, QtWidgets

class Example(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setFixedSize(700, 500)
        MainWindow.setStyleSheet("background-color:rgb(255,255,255)\n")


        font = QtGui.QFont()
        font.setFamily("BM DoHyeon")

        self.label = QtWidgets.QLabel(MainWindow)
        self.label.setGeometry(QtCore.QRect(20, 30, 670, 450))
        self.label.setObjectName("label")
        self.label.setFont(font)

        if(self.num== 1):
         self.label.setStyleSheet("background-image:url(EX01.png);\n"
                                    "background-repeat: no-repeat;")
        elif(self.num== 2):
         self.label.setStyleSheet("background-image:url(EX02.png);\n"
                                    "background-repeat: no-repeat;")
        elif (self.num == 3):
         self.label.setStyleSheet("background-image:url(EX03.png);\n"
                                    "background-repeat: no-repeat;")
        elif (self.num == 4):
         self.label.setStyleSheet("background-image:url(EX04.png);\n"
                                    "background-repeat: no-repeat;")
        elif (self.num == 5):
         self.label.setStyleSheet("background-image:url(EX05.png);\n"
                                    "background-repeat: no-repeat;")
        elif (self.num == 6):
         self.label.setStyleSheet("background-image:url(EX06.png);\n"
                                    "background-repeat: no-repeat;")
        elif (self.num == 7):
         self.label.setStyleSheet("background-image:url(EX07.png);\n"
                                    "background-repeat: no-repeat;")
        elif (self.num == 8):
         self.label.setStyleSheet("background-image:url(EX08.png);\n"
                                    "background-repeat: no-repeat;")




        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))


    def getnumber(self, num):
        self.num =num
        print(num)
        print(self.num)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Example()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())