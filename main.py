from PyQt5 import QtCore, QtGui, QtWidgets
from program import Ui_Dialog2


class Ui_DialogM(object):

    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.setFixedSize(1280, 720)

        Dialog.setStyleSheet("background-image:url(image/background.jpeg);\n"
                             "background-repeat: no-repeat;")


        self.btnLogin = QtWidgets.QPushButton(Dialog)
        self.btnLogin.setGeometry(QtCore.QRect(0, 0, 1280, 720))
        self.btnLogin.setObjectName("btnLogin")
        self.btnLogin.setStyleSheet("background-color: transparent;\n"
                                    "color: rgb(0, 0, 0);\n"
                                    "font: 13pt \"Noto Sans\";")
        #################### Login Button funtion #######################
        self.btnLogin.clicked.connect(self.MainPage)


        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Main"))
       # self.btnLogin.setText(_translate("Dialog", "Login"))


    def MainPage(self):  # 첫화면 연결
        self.homWindow = QtWidgets.QDialog()
        self.ui = Ui_Dialog2()
        self.ui.setupUi(self.homWindow)
        self.homWindow.show()
        Dialog.deleteLater()


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)

    Dialog = QtWidgets.QDialog()

    ui = Ui_DialogM()
    ui.setupUi(Dialog)

    Dialog.show()
    sys.exit(app.exec_())

