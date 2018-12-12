from PyQt5 import QtCore, QtGui, QtWidgets
from database import Db
from home import Ui_MainWindow

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.setFixedSize(700, 500)

        font = QtGui.QFont()
        font.setFamily("배달의민족 도현")
        font.setPointSize(12)
        Dialog.setStyleSheet("background-color:rgb(255,255,255)\n")

        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(150, 120, 151, 40))
        self.label.setObjectName("label")
        self.label.setFont(font)

        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(150, 160, 151, 40))
        self.label_2.setObjectName("label_2")
        self.label_2.setFont(font)

        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(150, 200, 171, 40))
        self.label_3.setObjectName("label_3")
        self.label_3.setFont(font)

        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(150, 240, 161, 40))
        self.label_4.setObjectName("label_4")
        self.label_4.setFont(font)

        self.txtEmail = QtWidgets.QLineEdit(Dialog)
        self.txtEmail.setGeometry(QtCore.QRect(320, 120, 221, 35))
        self.txtEmail.setObjectName("txtEmail")

        self.txtNickName = QtWidgets.QLineEdit(Dialog)
        self.txtNickName.setGeometry(QtCore.QRect(320, 160, 221, 35))
        self.txtNickName.setObjectName("txtNickName")

        self.txtPassword = QtWidgets.QLineEdit(Dialog)
        ################## make the password invisible ############
        self.txtPassword.setEchoMode(QtWidgets.QLineEdit.Password)
        ###########################################################
        self.txtPassword.setGeometry(QtCore.QRect(320, 200, 221, 35))

        self.txtPassword.setObjectName("txtPassword")
        self.txtPassword2 = QtWidgets.QLineEdit(Dialog)
        ################## make the password2 invisible ############
        self.txtPassword2.setEchoMode(QtWidgets.QLineEdit.Password)
        ###########################################################
        self.txtPassword2.setGeometry(QtCore.QRect(320, 240, 221, 35))
        self.txtPassword2.setObjectName("txtPassword2")

        self.btnCheck = QtWidgets.QPushButton(Dialog)
        self.btnCheck.setGeometry(QtCore.QRect(550, 120, 100, 35))
        self.btnCheck.setObjectName("btnCheck")
        self.btnCheck.setStyleSheet("background-color: rgb(224, 224, 224);\n"
                                    "color: rgb(100, 100, 100);\n"
                                    "font: 10pt \"BM DoHyeon\";")
        ################## register button#########################
        self.btnCheck.clicked.connect(self.signupCheck2)

        self.btnCheckn = QtWidgets.QPushButton(Dialog)
        self.btnCheckn.setGeometry(QtCore.QRect(550, 160, 100, 35))
        self.btnCheckn.setObjectName("btnCheckn")
        self.btnCheckn.setStyleSheet("background-color: rgb(224, 224, 224);\n"
                                     "color: rgb(100, 100, 100);\n"
                                     "font: 10pt \"BM DoHyeon\";")
        ################## register button#########################
        self.btnCheckn.clicked.connect(self.signupNickCheck2)

        self.btnRegister = QtWidgets.QPushButton(Dialog)
        self.btnRegister.setGeometry(QtCore.QRect(140, 330, 400, 50))
        self.btnRegister.setObjectName("btnRegister")
        self.btnRegister.setStyleSheet("background-color: rgb(0, 0, 0);\n"
                                       "color: rgb(255, 255, 255);\n"
                                       "font: 13pt \"BM DoHyeon\";")
        ################## register button#########################
        self.btnRegister.clicked.connect(self.registerButton)
        ###########################################################

        font.setPointSize(12)
        self.label_Heading = QtWidgets.QLabel(Dialog)
        self.label_Heading.setGeometry(QtCore.QRect(120, 30, 135, 61))
        self.label_Heading.setObjectName("label_Heading")
        self.label_Heading.setStyleSheet("color: rgb(51, 0, 51);\n"
                                         "font: 13pt \"BM DoHyeon\";")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        self.Dialog =Dialog

    def signupNickCheck2(self):  # 닉네임 체크
        nickname = self.txtNickName.text()
        getDb = Db()
        checkn = getDb.signupNickCheck(nickname)

        if (checkn):
            print("이미 존재하는 닉네임입니다")
            self.showMessage("경고 : ", "이미 존재하는 닉네임입니다")
            self.clearField()
            return False

        else:
            if (nickname == ""):
                self.showMessage("경고 : ", "닉네임을 입력해주세요")
                return False
            print("사용가능한 닉네임입입니다.")
            self.showMessage("확인 : ", "사용가능한 닉네임입니다")
            return True

    def signupCheck2(self):  # 이메일 있는지 체크
        email = self.txtEmail.text()
        getDb = Db()
        check = getDb.signupCheck(email)

        if (check):
            print("이미 존재하는 이메일 입니다")
            self.showMessage("경고 : ", "이미 존재하는 이메일 입니다")
            self.clearField()
            return False

        else:
            if (email == ""):
                self.showMessage("경고 : ", "이메일을 입력해주세요")
                return False
            print("사용가능한 이메일 입니다.")
            self.showMessage("확인 : ", "사용가능한 이메일 입니다")
            return True

    def registerButton(self):
        email = self.txtEmail.text()
        nickname = self.txtNickName.text()
        password = self.txtPassword.text()
        password2 = self.txtPassword2.text()

        if self.checkFields(email, nickname, password):
            self.showMessage("Error", "빈칸 없이 모두 채워주세요")
        else:
            if (self.checkPassword(password, password2)):
                if (self.signupCheck2() & self.signupNickCheck2()):
                    # insertDb = Db()
                    Db().insertTable(email, nickname, password)
                    self.showMessage("Success", "회원가입이 완료되었습니다")
                    self.clearField()
                    self.Dialog.hide()

            else:
                self.showMessage("Error", "비밀번호가 일치하지 않습니다")

    def showMessage(self, title, msg):
        msgBox = QtWidgets.QMessageBox()
        msgBox.setIcon(QtWidgets.QMessageBox.Information)
        # msgBox.setTitle(title)
        msgBox.setText(msg)
        msgBox.setStandardButtons(QtWidgets.QMessageBox.Ok)
        msgBox.exec_()

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "회원가입"))
        self.label.setText(_translate("Dialog", "이메일:"))
        self.label_2.setText(_translate("Dialog", "별명:"))
        self.label_3.setText(_translate("Dialog", "비밀번호:"))
        self.label_4.setText(_translate("Dialog", "비밀번호 확인:"))
        self.btnRegister.setText(_translate("Dialog", "등록"))
        self.btnCheck.setText(_translate("Dialog", "중복확인"))
        self.btnCheckn.setText(_translate("Dialog", "중복확인"))

        self.label_Heading.setText(_translate("Dialog", "계정 만들기"))

    def checkFields(self, email, nickname, password):
        if (nickname == "" or email == "" or password == ""):
            return True

    ############## check if password1 and password2 matches #############
    def checkPassword(self, password1, password2):
        return password1 == password2

    ##################### clear fields ##################
    def clearField(self):
        self.txtPassword.setText(None)
        self.txtNickName.setText(None)
        self.txtEmail.setText(None)
        self.txtPassword2.setText(None)


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

