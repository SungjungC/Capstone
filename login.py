from PyQt5 import QtCore, QtGui, QtWidgets
from database import Db #importing database.py
from home import Ui_MainWindow
from signup import Ui_Dialog


class Ui_Dialog2(object):

    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.setFixedSize(1280, 720)

        Dialog.setStyleSheet("background-color:rgb(255,255,255)\n")


        #"background-color:rgb(255,255,255)\n"
        #"background-image:url(background.jpeg);\n"
        #"background-repeat: no-repeat;")

        font = QtGui.QFont()
        font.setFamily("BM DoHyeon")

        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(400, 250, 150, 30))
        self.label.setObjectName("label")
        self.label.setFont(font)
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(400, 330, 150, 30))
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.txtNickName = QtWidgets.QLineEdit(Dialog)
        self.txtNickName.setGeometry(QtCore.QRect(570, 245, 200, 40))
        self.txtNickName.setObjectName("txtNickname")
        self.txtPassword = QtWidgets.QLineEdit(Dialog)
        ################## make the password invisible ###########
        self.txtPassword.setEchoMode(QtWidgets.QLineEdit.Password)
        ###########################################################
        self.txtPassword.setGeometry(QtCore.QRect(570, 325, 200, 40))
        self.txtPassword.setObjectName("txtPassword")
        self.btnLogin = QtWidgets.QPushButton(Dialog)
        self.btnLogin.setGeometry(QtCore.QRect(440, 400, 150, 50))
        self.btnLogin.setObjectName("btnLogin")
        self.btnLogin.setStyleSheet("background-color: rgb(0, 0, 0);\n"
                                    "color: rgb(255, 255, 255);\n"
                                    "font: 13pt \"BM DoHyeon\";")
        #################### Login Button funtion #######################
        self.btnLogin.clicked.connect(self.loginCheck)
        #################################################################
        self.btnSignup = QtWidgets.QPushButton(Dialog)
        self.btnSignup.setGeometry(QtCore.QRect(600, 400, 150, 50))
        self.btnSignup.setObjectName("btnSignup")
        self.btnSignup.setStyleSheet("background-color: rgb(0, 0, 0);\n"
                                     "color: rgb(255, 255, 255);\n"
                                     "font: 13pt \"BM DoHyeon\";")


        self.btnSignup.clicked.connect(self.signupButton)
        ################################################################
        self.label_Heading = QtWidgets.QLabel(Dialog)
        self.label_Heading.setGeometry(QtCore.QRect(150, 90, 381, 51))
        self.label_Heading.setObjectName("label_Heading")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "LOGIN"))
        self.label.setText(_translate("Dialog", "<h2>닉네임</h2>"))
        self.label_2.setText(_translate("Dialog", "<h2>비밀번호</h2>"))
        self.btnLogin.setText(_translate("Dialog", "로그인"))
        self.btnSignup.setText(_translate("Dialog", "회원가입"))
        
    def loginCheck(self): #     로그인 데베랑 확인
        self.nickname = self.txtNickName.text()
        password = self.txtPassword.text()
        getDb = Db()
        result = getDb.loginCheck(self.nickname,password)
        if(result):
            self.welcomePage()
            self.clearField()

        else:
            print("비밀번호가 틀렸습니다")
            self.showMessage("경고 : ","잘못된 닉네임 혹은 비밀번호를 입력하셨습니다")
            self.clearField()
            
    def showMessage(self,title,msg): # 잘못입력시 메세지
        msgBox = QtWidgets.QMessageBox()
        msgBox.setIcon(QtWidgets.QMessageBox.Warning)
        #msgBox.setTitle(title)
        msgBox.setText(msg)
        msgBox.setStandardButtons(QtWidgets.QMessageBox.Ok)
        msgBox.exec_()

    def welcomePage(self):  # 첫화면 연결
            self.homWindow = QtWidgets.QDialog()
            self.ui = Ui_MainWindow()
            self.ui.setupUi(self.homWindow)
            self.homWindow.show()
            self.ui.setnickname(self.nickname)
            Dialog.hide()

    def signupButton(self):   # 회원가입 버튼
        self.signDialog = QtWidgets.QDialog()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self.signDialog)
        self.signDialog.show()

                
    def clearField(self):   # 입력후 clear 없애기
        self.txtNickName.setText(None)
        self.txtPassword.setText(None)
        

        
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)

    Dialog = QtWidgets.QDialog()

    ui = Ui_Dialog2()
    ui.setupUi(Dialog)

    Dialog.show()
    sys.exit(app.exec_())

