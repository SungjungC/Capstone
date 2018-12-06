from PyQt5 import QtCore, QtGui, QtWidgets
from database_user_id import Db2
from database import  Db #importing database.py


class Pro_Dialog(object):
    def setupPro(self, Dialog):
        Dialog.setObjectName("Profile")
        Dialog.setFixedSize(700, 500)

        font = QtGui.QFont()
        font.setFamily("BM DoHyeon")
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

        self.txtSexF= QtWidgets.QRadioButton(Dialog)
        self.txtSexF.setGeometry(QtCore.QRect(320, 120, 221, 35))
        self.txtSexF.setObjectName("txtSexF")

        self.label_F = QtWidgets.QLabel(Dialog)
        self.label_F.setGeometry(QtCore.QRect(340, 120, 161, 40))
        self.label_F.setObjectName("label_F")
        self.label_F.setFont(font)

        self.txtSexM = QtWidgets.QRadioButton(Dialog)
        self.txtSexM.setGeometry(QtCore.QRect(400, 120, 221, 35))
        self.txtSexM.setObjectName("txtSexM")

        self.label_M = QtWidgets.QLabel(Dialog)
        self.label_M.setGeometry(QtCore.QRect(420, 120, 161, 40))
        self.label_M.setObjectName("label_M")
        self.label_M.setFont(font)



        self.txtHeight = QtWidgets.QLineEdit(Dialog)
        self.txtHeight.setGeometry(QtCore.QRect(320, 160, 221, 35))
        self.txtHeight.setObjectName("txtHeight")

        self.txtWeight = QtWidgets.QLineEdit(Dialog)
        self.txtWeight.setGeometry(QtCore.QRect(320, 200, 221, 35))
        self.txtWeight.setObjectName("txtWeight")

        self.txtGoalWeight = QtWidgets.QLineEdit(Dialog)
        self.txtGoalWeight.setGeometry(QtCore.QRect(320, 240, 221, 35))
        self.txtGoalWeight.setObjectName("txtGoalWeight")



        self.btnRegister = QtWidgets.QPushButton(Dialog)
        self.btnRegister.setGeometry(QtCore.QRect(140, 330, 400, 50))
        self.btnRegister.setObjectName("btnRegister")
        self.btnRegister.setStyleSheet("background-color: rgb(0, 0, 0);\n"
                                       "color: rgb(255, 255, 255);\n"
                                       "font: 13pt \"BM DoHyeon\";")
        self.btnRegister.clicked.connect(self.registerProfileButton)


        font.setPointSize(12)
        self.label_Heading = QtWidgets.QLabel(Dialog)
        self.label_Heading.setGeometry(QtCore.QRect(120, 30, 135, 61))
        self.label_Heading.setObjectName("label_Heading")
        self.label_Heading.setStyleSheet(
                                         "color: rgb(51, 0, 51);\n"
                                         "font: 20pt \"BM DoHyeon\";")


        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)


    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "사용자 정보"))
        self.label.setText(_translate("Dialog", "성별:"))
        self.label_F.setText(_translate("Dialog", " 여"))
        self.label_M.setText(_translate("Dialog", " 남"))
        self.label_2.setText(_translate("Dialog", "키:"))
        self.label_3.setText(_translate("Dialog", "몸무게:"))
        self.label_4.setText(_translate("Dialog", "목표 몸무게:"))
        self.btnRegister.setText(_translate("Dialog", "등록"))
        self.label_Heading.setText(_translate("Dialog", self.nickname+"님의정보"))


    def setnickname(self, param_nickname):
        self.nickname = param_nickname
        getDb = Db()
        getDb.nicknameCheck(self.nickname)



    def registerProfileButton(self):  # 등록버튼
        if self.txtSexF.isChecked():
            sex = "여"
        elif self.txtSexM.isChecked():
            sex = "남"
        else:
            sex =""

        height = self.txtHeight.text()
        weight = self.txtWeight.text()
        goalweight = self.txtGoalWeight.text()
        getuserid = Db().nicknameCheck(self.nickname)

        #print(sex, height, weight, goalweight)

        if self.checkFields(sex, height, weight, goalweight):
            self.showMessage("Error", "빈칸 없이 모두 채워주세요")
        else:
            if (Db2().profileCheck(getuserid)):
                Db2().updateTable(getuserid, sex, height, weight, goalweight)
                self.showMessage("Success", "프로필 수정이 완료되었습니다")
                self.clearField()
            else:
                Db2().insertTable(getuserid, sex, height, weight, goalweight)
                self.showMessage("Success", "프로필 입력이 완료되었습니다")
                self.clearField()


    def checkFields(self, sex, height, weight, goalweight):
        if (sex == "" or height == "" or weight == ""or goalweight == ""):
            return True

    def showMessage(self, title, msg):  # 메세지 출력창
            msgBox = QtWidgets.QMessageBox()
            msgBox.setIcon(QtWidgets.QMessageBox.Information)
            # msgBox.setTitle(title)
            msgBox.setText(msg)
            msgBox.setStandardButtons(QtWidgets.QMessageBox.Ok)
            msgBox.exec_()

    def clearField(self):
        self.txtHeight.setText(None)
        self.txtWeight.setText(None)
        self.txtGoalWeight.setText(None)



if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Pro_Dialog()
    ui.setupPro(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
