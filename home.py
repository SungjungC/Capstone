from explain import ExExplain
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QScrollArea
from profile import Pro_Dialog
from database_user_id import Db2
from record import Rec_Dialog
from database import Db
from exercise import Example
from database_exercise import Db3
from PyQt5.QtCore import QCoreApplication

class Ui_MainWindow(object):
    def setupUi(self, Dialog):

        Dialog.setObjectName("Dialog")
        Dialog.setFixedSize(1280, 720)
        Dialog.setStyleSheet("background-color:rgb(255,255,255)\n")
        font = QtGui.QFont()
        font.setFamily("BM DoHyeon")
        self.centralwidget = QtWidgets.QWidget(Dialog)
        self.centralwidget.setObjectName("centralwidget")
        # self.calendarWidget = QtWidgets.QCalendarWidget(self.centralwidget)
        # self.calendarWidget.setGeometry(QtCore.QRect(30, 300, 400, 400))
        # self.calendarWidget.setObjectName("calendarWidget")

        self.pattern = QtWidgets.QLabel(Dialog)
        self.pattern.setGeometry(QtCore.QRect(0, 0, 1280, 60))
        self.pattern.setObjectName("pattern")
        self.pattern.setFont(font)
        self.pattern.setStyleSheet("background-color:rgb(0,0,0);\n"
                                   "color:rgb(255,255,255);")

        self.profile = QtWidgets.QPushButton(Dialog)
        self.profile.setObjectName("profile")
        self.profile.setGeometry(QtCore.QRect(5, 5, 100, 50))
        self.profile.setFont(font)
        self.profile.clicked.connect(self.profileButton)

        self.record = QtWidgets.QPushButton(Dialog)
        self.record.setObjectName("record")
        self.record.setGeometry(QtCore.QRect(120, 5, 100, 50))
        self.record.setFont(font)
        self.record.clicked.connect(self.RecordButton)

        self.logout = QtWidgets.QPushButton(Dialog)
        self.logout.setObjectName("logout")
        self.logout.setFont(font)
        self.logout.setGeometry(QtCore.QRect(1175, 5, 100, 50))
        self.logout.clicked.connect(QCoreApplication.instance().quit)

        self.logo = QtWidgets.QLabel(Dialog)
        self.logo.setGeometry(QtCore.QRect(570, 5, 300, 50))
        self.logo.setObjectName("logo")
        self.logo.setFont(font)
        self.logo.setStyleSheet("background:transparent;\n"
                                "color: rgb(255,255,255);\n"
                                "font: 25pt \"BM DoHyeon\";")

        self.ex1 = QtWidgets.QPushButton(Dialog)
        self.ex1.setObjectName("ex1")
        self.ex1.setGeometry(QtCore.QRect(10, 70, 500, 120))
        self.ex1.setFont(font)
        self.ex1.setStyleSheet("background-image:url(image/01.png)")

        self.ex2 = QtWidgets.QPushButton(Dialog)
        self.ex2.setObjectName("ex2")
        self.ex2.setGeometry(QtCore.QRect(10, 200, 500, 120))
        self.ex2.setFont(font)
        self.ex2.setStyleSheet("background-image:url(image/02.png)")

        self.ex3 = QtWidgets.QPushButton(Dialog)
        self.ex3.setObjectName("ex3")
        self.ex3.setGeometry(QtCore.QRect(10, 330, 500, 120))
        self.ex3.setFont(font)
        self.ex3.setStyleSheet("background-image:url(image/03.png)")

        self.ex4 = QtWidgets.QPushButton(Dialog)
        self.ex4.setObjectName("ex4")
        self.ex4.setGeometry(QtCore.QRect(10, 460, 500, 120))
        self.ex4.setFont(font)
        self.ex4.setStyleSheet("background-image:url(image/04.png)")

        self.ex5 = QtWidgets.QPushButton(Dialog)
        self.ex5.setObjectName("ex5")
        self.ex5.setGeometry(QtCore.QRect(10, 590, 500, 120))
        self.ex5.setFont(font)
        self.ex5.setStyleSheet("background-image:url(image/05.png)")

        self.ex6 = QtWidgets.QPushButton(Dialog)
        self.ex6.setObjectName("ex6")
        self.ex6.setGeometry(QtCore.QRect(520, 70, 500, 120))
        self.ex6.setFont(font)
        self.ex6.setStyleSheet("background-image:url(image/06.png)")

        self.ex7 = QtWidgets.QPushButton(Dialog)
        self.ex7.setObjectName("ex7")
        self.ex7.setGeometry(QtCore.QRect(520, 200, 500, 120))
        self.ex7.setFont(font)
        self.ex7.setStyleSheet("background-image:url(image/07.png)")

        self.ex8 = QtWidgets.QPushButton(Dialog)
        self.ex8.setObjectName("ex8")
        self.ex8.setGeometry(QtCore.QRect(520, 330, 500, 120))
        self.ex8.setFont(font)
        self.ex8.setStyleSheet("background-image:url(image/08.png)")

        # self.ex9 = QtWidgets.QPushButton(Dialog)
        # self.ex9.setObjectName("ex9")
        # self.ex9.setGeometry(QtCore.QRect(520, 460, 500, 120))
        # self.ex9.setFont(font)

        # self.ex10 = QtWidgets.QPushButton(Dialog)
        # self.ex10.setObjectName("ex10")
        # self.ex10.setGeometry(QtCore.QRect(520, 590, 500, 120))
        # self.ex10.setFont(font)

        self.ex1.clicked.connect(self.startExercise1)
        self.ex2.clicked.connect(self.startExercise2)
        self.ex3.clicked.connect(self.startExercise3)
        self.ex4.clicked.connect(self.startExercise4)
        self.ex5.clicked.connect(self.startExercise5)
        self.ex6.clicked.connect(self.startExercise6)
        self.ex7.clicked.connect(self.startExercise7)
        self.ex8.clicked.connect(self.startExercise8)
        # self.ex9.clicked.connect(self.startExercise)
        # self.ex10.clicked.connect(self.startExercise)

        self.filter = QtWidgets.QLabel(Dialog)
        self.filter.setGeometry(QtCore.QRect(1030, 70, 240, 640))
        self.filter.setObjectName("filter")
        self.filter.setFont(font)
        self.filter.setStyleSheet("background-color:rgb(234,234,234);\n")

        # 난이도
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(1100, 80, 120, 70))
        self.label.setObjectName("label")
        self.label.setFont(font)
        self.label.setStyleSheet("background-color:rgb(234,234,234);\n"
                                 "color: rgb(80,80,80);\n"
                                 "font: 15pt \"BM DoHyeon\";")

        # 부위
        self.label2 = QtWidgets.QLabel(Dialog)
        self.label2.setGeometry(QtCore.QRect(1110, 230, 120, 70))
        self.label2.setObjectName("label")
        self.label2.setFont(font)
        self.label2.setStyleSheet("background-color:rgb(234,234,234);\n"
                                  "color: rgb(80,80,80);\n"
                                  "font: 15pt \"BM DoHyeon\";")

        # 덤벨
        self.label3 = QtWidgets.QLabel(Dialog)
        self.label3.setGeometry(QtCore.QRect(1110, 380, 120, 70))
        self.label3.setObjectName("label")
        self.label3.setFont(font)
        self.label3.setStyleSheet("background-color:rgb(234,234,234);\n"
                                  "color: rgb(80,80,80);\n"
                                  "font: 15pt \"BM DoHyeon\";")

        self.level3 = QtWidgets.QRadioButton(Dialog)
        self.level3.setGeometry(QtCore.QRect(1040, 160, 20, 20))
        self.level3.setObjectName("level3")
        self.level3.setStyleSheet("background-color :rgb(234,234,234);\n")
        self.txtlevel3 = QtWidgets.QLabel(Dialog)
        self.txtlevel3.setGeometry(QtCore.QRect(1070, 160, 20, 30))
        self.txtlevel3.setObjectName("txtlevel3")
        self.txtlevel3.setFont(font)
        self.txtlevel3.setStyleSheet("background-color:rgb(234,234,234);\n"
                                     "font: 12pt \"BM DoHyeon\";")

        self.buttonGroup_1 = QtWidgets.QButtonGroup(Dialog)
        self.buttonGroup_1.setObjectName("buttonGroup_1")
        self.buttonGroup_1.addButton(self.level3)

        self.level2 = QtWidgets.QRadioButton(Dialog)
        self.level2.setGeometry(QtCore.QRect(1120, 160, 20, 20))
        self.level2.setObjectName("level2")
        self.level2.setStyleSheet("background-color :rgb(234,234,234);\n")
        self.txtlevel2 = QtWidgets.QLabel(Dialog)
        self.txtlevel2.setGeometry(QtCore.QRect(1150, 160, 20, 30))
        self.txtlevel2.setObjectName("txtlevel2")
        self.txtlevel2.setFont(font)
        self.txtlevel2.setStyleSheet("background-color:rgb(234,234,234);\n"
                                     "font: 12pt \"BM DoHyeon\";")

        self.buttonGroup_1.addButton(self.level2)

        self.level1 = QtWidgets.QRadioButton(Dialog)
        self.level1.setGeometry(QtCore.QRect(1200, 160, 20, 20))
        self.level1.setObjectName("level1")
        self.level1.setStyleSheet("background-color :rgb(234,234,234);\n")
        self.txtlevel1 = QtWidgets.QLabel(Dialog)
        self.txtlevel1.setGeometry(QtCore.QRect(1230, 160, 20, 30))
        self.txtlevel1.setObjectName("txtlevel1")
        self.txtlevel1.setFont(font)
        self.txtlevel1.setStyleSheet("background-color:rgb(234,234,234);\n"
                                     "font: 12pt \"BM DoHyeon\";")

        self.buttonGroup_1.addButton(self.level1)

        self.part3 = QtWidgets.QRadioButton(Dialog)
        self.part3.setGeometry(QtCore.QRect(1040, 310, 20, 20))
        self.part3.setObjectName("part3")
        self.part3.setStyleSheet("background-color :rgb(234,234,234);\n")
        self.txtpart3 = QtWidgets.QLabel(Dialog)
        self.txtpart3.setGeometry(QtCore.QRect(1060, 310, 40, 30))
        self.txtpart3.setObjectName("txtpart3")
        self.txtpart3.setFont(font)
        self.txtpart3.setStyleSheet("background-color:rgb(234,234,234);\n"
                                    "font: 12pt \"BM DoHyeon\";")

        self.buttonGroup_2 = QtWidgets.QButtonGroup(Dialog)
        self.buttonGroup_2.setObjectName("buttonGroup_2")
        self.buttonGroup_2.addButton(self.part3)

        self.part2 = QtWidgets.QRadioButton(Dialog)
        self.part2.setGeometry(QtCore.QRect(1120, 310, 20, 20))
        self.part2.setObjectName("part2")
        self.part2.setStyleSheet("background-color :rgb(234,234,234);\n")
        self.txtpart2 = QtWidgets.QLabel(Dialog)
        self.txtpart2.setGeometry(QtCore.QRect(1140, 310, 40, 30))
        self.txtpart2.setObjectName("txtpart2")
        self.txtpart2.setFont(font)
        self.txtpart2.setStyleSheet("background-color:rgb(234,234,234);\n"
                                    "font: 12pt \"BM DoHyeon\";")

        self.buttonGroup_2.addButton(self.part2)

        self.part1 = QtWidgets.QRadioButton(Dialog)
        self.part1.setGeometry(QtCore.QRect(1200, 310, 20, 30))
        self.part1.setObjectName("part1")
        self.part1.setStyleSheet("background-color :rgb(234,234,234);\n")
        self.txtpart1 = QtWidgets.QLabel(Dialog)
        self.txtpart1.setGeometry(QtCore.QRect(1220, 310, 40, 30))
        self.txtpart1.setObjectName("txtpart1")
        self.txtpart1.setFont(font)
        self.txtpart1.setStyleSheet("background-color:rgb(234,234,234);\n"
                                    "font: 12pt \"BM DoHyeon\";")

        self.buttonGroup_2.addButton(self.part1)

        self.buttonGroup_3 = QtWidgets.QButtonGroup(Dialog)
        self.buttonGroup_3.setObjectName("buttonGroup_3")

        self.tool1 = QtWidgets.QRadioButton(Dialog)
        self.tool1.setGeometry(QtCore.QRect(1040, 450, 20, 20))
        self.tool1.setObjectName("tool1")
        self.tool1.setStyleSheet("background-color:rgb(234,234,234);\n")
        self.txttool1 = QtWidgets.QLabel(Dialog)
        self.txttool1.setGeometry(QtCore.QRect(1070, 450, 120, 30))
        self.txttool1.setObjectName("txttool1")
        self.txttool1.setFont(font)
        self.txttool1.setStyleSheet("background-color:rgb(234,234,234);\n"
                                    "font: 12pt \"BM DoHyeon\";")
        self.buttonGroup_3.addButton(self.tool1)

        self.tool2 = QtWidgets.QRadioButton(Dialog)
        self.tool2.setGeometry(QtCore.QRect(1140, 450, 20, 20))
        self.tool2.setObjectName("tool2")
        self.tool2.setStyleSheet("background-color:rgb(234,234,234);\n")
        self.txttool2 = QtWidgets.QLabel(Dialog)
        self.txttool2.setGeometry(QtCore.QRect(1165, 450, 100, 30))
        self.txttool2.setObjectName("txttool2")
        self.txttool2.setFont(font)
        self.txttool2.setStyleSheet("background-color:rgb(234,234,234);\n"
                                    "font: 12pt \"BM DoHyeon\";")
        self.buttonGroup_3.addButton(self.tool2)

        self.search = QtWidgets.QPushButton(Dialog)
        self.search.setGeometry(QtCore.QRect(1050, 610, 205, 70))
        self.search.setObjectName("search")
        self.search.setFont(font)
        self.search.clicked.connect(self.searchExercise)
        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

        # Dialog.setWindowFlags(QtCore.Qt.CustomizeWindowHint)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "HOME"))
        self.profile.setText(_translate("Dialog", "프로필"))
        self.record.setText(_translate("Dialog", "운동기록"))
        self.label.setText(_translate("Dialog", "난이도"))
        self.label2.setText(_translate("Dialog", "부위"))
        self.logout.setText(_translate("Dialog", "종료"))
        self.txtlevel1.setText(_translate("Dialog", "하"))
        self.txtlevel2.setText(_translate("Dialog", "중"))
        self.txtlevel3.setText(_translate("Dialog", "상"))
        self.txtpart1.setText(_translate("Dialog", "전신"))
        self.txtpart2.setText(_translate("Dialog", "하체"))
        self.txtpart3.setText(_translate("Dialog", "상체"))
        self.search.setText(_translate("Dialog", "검색하기"))
        self.txttool1.setText(_translate("Dialog", "사용"))
        self.txttool2.setText(_translate("Dialog", "사용 X"))
        self.label3.setText(_translate("Dialog", "덤벨"))
        self.logo.setText(_translate("Dialog", "HOME FIT"))


    def searchExercise(self):
        if self.level1.isChecked():
            level = 1
        elif self.level2.isChecked():
            level = 2
        elif self.level3.isChecked():
            level = 3
        else:
            level = ""

        if self.part1.isChecked():
            part = 1
        elif self.part2.isChecked():
            part = 2
        elif self.part3.isChecked():
            part = 3
        else:
            part = ""

        if self.tool1.isChecked():
            tool = 1
        elif self.tool2.isChecked():
            tool = 2
        else:
            tool = ""

        ex_num = Db3().searchEx(level, part, tool)
        print("home:", ex_num)

        if(ex_num!=0):
            self.exWindow = QtWidgets.QDialog()
            self.ui = Example()
            self.ui.setupUi(self.exWindow,ex_num)
            self.exWindow.show()
            self.ui.start()
            self.ui.nextFrameSlot()

    def startExercise1(self):
        self.exWindow = QtWidgets.QDialog()
        self.ui = ExExplain()
        self.ui.getnumber(1)
        self.ui.setupUi(self.exWindow)
        self.exWindow.show()

    def startExercise2(self):
        self.exWindow = QtWidgets.QDialog()
        self.ui = ExExplain()
        self.ui.getnumber(2)
        self.ui.setupUi(self.exWindow)
        self.exWindow.show()

    def startExercise3(self):
        self.exWindow = QtWidgets.QDialog()
        self.ui = ExExplain()
        self.ui.getnumber(3)
        self.ui.setupUi(self.exWindow)
        self.exWindow.show()

    def startExercise4(self):
        self.exWindow = QtWidgets.QDialog()
        self.ui = ExExplain()
        self.ui.getnumber(4)
        self.ui.setupUi(self.exWindow)
        self.exWindow.show()

    def startExercise5(self):
        self.exWindow = QtWidgets.QDialog()
        self.ui = ExExplain()
        self.ui.getnumber(5)
        self.ui.setupUi(self.exWindow)
        self.exWindow.show()

    def startExercise6(self):
        self.exWindow = QtWidgets.QDialog()
        self.ui = ExExplain()
        self.ui.getnumber(6)
        self.ui.setupUi(self.exWindow)
        self.exWindow.show()

    def startExercise7(self):
        self.exWindow = QtWidgets.QDialog()
        self.ui = ExExplain()
        self.ui.getnumber(7)
        self.ui.setupUi(self.exWindow)
        self.exWindow.show()

    def startExercise8(self):
        self.exWindow = QtWidgets.QDialog()
        self.ui = ExExplain()
        self.ui.getnumber(8)
        self.ui.setupUi(self.exWindow)
        self.exWindow.show()

    def setnickname(self, param_nickname):
        self.nickname = param_nickname

    def profileButton(self):
        self.proDialog = QtWidgets.QDialog()
        self.ui = Pro_Dialog()
        self.ui.setnickname(self.nickname)
        self.ui.setupPro(self.proDialog)
        self.proDialog.show()

    def RecordButton(self):
        getuserid = Db().nicknameCheck(self.nickname)

        if (Db2().profileCheck(getuserid)):
            self.RecDialog = QtWidgets.QDialog()
            self.ui = Rec_Dialog()
            self.ui.setnickname(self.nickname)
            self.ui.setupUi(self.RecDialog)
            self.RecDialog.show()


        else:
            self.showMessage("Error", "프로필 입력을 해주세요!")

    def showMessage(self, title, msg):  # 메세지
        msgBox = QtWidgets.QMessageBox()
        msgBox.setIcon(QtWidgets.QMessageBox.Warning)
        # msgBox.setTitle(title)
        msgBox.setText(msg)
        msgBox.setStandardButtons(QtWidgets.QMessageBox.Ok)
        msgBox.exec_()



if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_MainWindow()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

    # def startExercise0(self):
    #     self.exWindow = QtWidgets.QDialog()
    #     self.ui = Example()
    #     self.ui.setupUi(self.exWindow,0)
    #     self.exWindow.show()
    #     self.ui.start()
    #     self.ui.nextFrameSlot()
    #
    # def startExercise1(self):
    #     self.exWindow = QtWidgets.QDialog()
    #     self.ui = Example()
    #     self.ui.setupUi(self.exWindow,1)
    #     self.exWindow.show()
    #     self.ui.start()
    #     self.ui.nextFrameSlot()
    #     #Dialog.hide()
    #
    # def startExercise2(self):
    #     self.exWindow = QtWidgets.QDialog()
    #     self.ui = Example()
    #     self.ui.setupUi(self.exWindow,2)
    #     self.exWindow.show()
    #     self.ui.start()
    #     self.ui.nextFrameSlot()
    #
    # def startExercise3(self):
    #     self.exWindow = QtWidgets.QDialog()
    #     self.ui = Example()
    #     self.ui.setupUi(self.exWindow,3)
    #     self.exWindow.show()
    #     self.ui.start()
    #     self.ui.nextFrameSlot()
    #
    # def startExercise4(self):
    #     self.exWindow = QtWidgets.QDialog()
    #     self.ui = Example()
    #     self.ui.setupUi(self.exWindow,4)
    #     self.exWindow.show()
    #     self.ui.start()
    #     self.ui.nextFrameSlot()
    #
    # def startExercise5(self):
    #     self.exWindow = QtWidgets.QDialog()
    #     self.ui = Example()
    #     self.ui.setupUi(self.exWindow,5)
    #     self.exWindow.show()
    #     self.ui.start()
    #     self.ui.nextFrameSlot()
    #
    # def startExercise6(self):
    #     self.exWindow = QtWidgets.QDialog()
    #     self.ui = Example()
    #     self.ui.setupUi(self.exWindow,6)
    #     self.exWindow.show()
    #     self.ui.start()
    #     self.ui.nextFrameSlot()
    #
    # def startExercise7(self):
    #     self.exWindow = QtWidgets.QDialog()
    #     self.ui = Example()
    #     self.ui.setupUi(self.exWindow,7)
    #     self.exWindow.show()
    #     self.ui.start()
    #     self.ui.nextFrameSlot()
    #
    # def startExercise8(self):
    #     self.exWindow = QtWidgets.QDialog()
    #     self.ui = Example()
    #     self.ui.setupUi(self.exWindow,8)
    #     self.exWindow.show()
    #     self.ui.start()
    #     self.ui.nextFrameSlot()
    #
    # def startExercise9(self):
    #     self.exWindow = QtWidgets.QDialog()
    #     self.ui = Example()
    #     self.ui.setupUi(self.exWindow,9)
    #     self.exWindow.show()
    #     self.ui.start()
    #     self.ui.nextFrameSlot()
