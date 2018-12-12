
from PyQt5 import QtCore, QtGui, QtWidgets
from database import  Db
from PyQt5.QtWidgets import  QTableWidget,QTableWidgetItem,QTreeView
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QStandardItemModel


class Rec_Dialog(object):
    DATE, EXNAME, HOURS, EXNUM  = range(4)

    def setupUi(self, Dialog):

        Dialog.setObjectName("Dialog")
        Dialog.setFixedSize(640, 360)
        Dialog.setStyleSheet("background-color:rgb(255,255,255)\n")

        font = QtGui.QFont()
        font.setFamily("BM DoHyeon")

        #목표몸무게달성
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(20, 20, 220, 60))
        self.label.setObjectName("label")
        self.label.setFont(font)

        #달성 %
        # self.label_1 = QtWidgets.QLabel(Dialog)
        # self.label_1.setGeometry(QtCore.QRect(140, 65, 50, 30))
        # self.label_1.setObjectName("label1")
        # self.label_1.setFont(font)

        # 목표몸무게 멘트
        self.label_1_1 = QtWidgets.QLabel(Dialog)
        self.label_1_1.setGeometry(QtCore.QRect(20, 100, 170, 20))
        self.label_1_1.setObjectName("label1_1")
        self.label_1_1.setStyleSheet("font: 8pt \"BM DoHyeon\";")

        #progressBar
        self.progressBar = QtWidgets.QProgressBar(Dialog)
        self.progressBar.setGeometry(QtCore.QRect(20, 70, 130, 20))
        self.progressBar.setProperty("value", self.goal)
        self.progressBar.setObjectName("progressBar")

        #BMI 지수
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(20, 150, 200, 30))
        self.label_2.setObjectName("label2")
        self.label_2.setFont(font)

        # BMI 지수멘트
        self.label_2_2 = QtWidgets.QLabel(Dialog)
        self.label_2_2.setGeometry(QtCore.QRect(20, 180, 200, 30))
        self.label_2_2.setObjectName("label2_2")
        self.label_2_2.setFont(font)


        self.dataView =QtWidgets.QTreeView(Dialog)
        self.dataView.setGeometry(QtCore.QRect(220, 30, 400, 300))
        self.dataView.setObjectName("운동기록")
        self.dataView.setRootIsDecorated(True)
        self.dataView.setAlternatingRowColors(True)
        self.dataView.setEditTriggers(QTreeView.NoEditTriggers)


        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "운동기록"))
        self.label.setText(_translate("Dialog", "<h2>목표몸무게 달성</h2>"))
        # self.label_1.setText(_translate("Dialog", str(self.goal)+"%"))

        if(self.goal < 50):
            self.label_1_1.setText(_translate("Dialog", "조금 더 분발하세요!"))

        elif(50  <= self.goal < 80):
            self.label_1_1.setText(_translate("Dialog", "반이나 왔어요 조금만 힘내요!"))


        elif (80 <= self.goal < 100):
            self.label_1_1.setText(_translate("Dialog", "목표 곧 달성이예요!"))

        else:
            self.label_1_1.setText(_translate("Dialog", "축하해요! 목표를 달성했어요!"))



        self.label_2.setText(_translate("Dialog", "<h2>BMI 지수 : " + self.bmist+"</h2>"))



        if(self.bmi <=18.5):
            self.label_2_2.setText(_translate("Dialog", "저체중 입니다"))

        elif (18.5 < self.bmi <=24.9):
            self.label_2_2.setText(_translate("Dialog", "정상 입니다"))

        elif (25.0 < self.bmi <= 29.9):
            self.label_2_2.setText(_translate("Dialog", "과체중 입니다"))

        else:
            self.label_2_2.setText(_translate("Dialog", "비만 입니다"))

        model = self.createRecordModel()

        self.dataView.setModel(model)

        list = Db().forrecord(self.nickname)
        checkC =len(list)

        c = 0

        if (checkC == 0):
            print("운동기록없음")
        else:
            while (True):
                if (c == checkC):
                    break
                #id = list[c][0]
                name = list[c][1]
                date = list[c][2]
                time = list[c][3]
                count = list[c][4]

                c = c + 1

                self.addRec(model, date, name, time, count)


    def setnickname(self, param_nickname):
        self.nickname = param_nickname
        self.bmi = round(Db().forBMI(self.nickname),1)
        self.bmist = str(self.bmi)
        self.goal =round(Db().forGoal(self.nickname),1)
        #Db.forrecord(self.nickname)


    def createTable(self):
    # Create table
        self.tableWidget = QTableWidget()
        self.tableWidget.setRowCount(4)
        self.tableWidget.setColumnCount(2)
        self.tableWidget.setItem(0, 0, QTableWidgetItem("Cell (1,1)"))
        self.tableWidget.setItem(0, 1, QTableWidgetItem("Cell (1,2)"))
        self.tableWidget.setItem(1, 0, QTableWidgetItem("Cell (2,1)"))
        self.tableWidget.setItem(1, 1, QTableWidgetItem("Cell (2,2)"))
        self.tableWidget.setItem(2, 0, QTableWidgetItem("Cell (3,1)"))
        self.tableWidget.setItem(2, 1, QTableWidgetItem("Cell (3,2)"))
        self.tableWidget.setItem(3, 0, QTableWidgetItem("Cell (4,1)"))
        self.tableWidget.setItem(3, 1, QTableWidgetItem("Cell (4,2)"))
        self.tableWidget.move(0, 0)

    def createRecordModel(self):
        model = QStandardItemModel(0, 4)
        model.setHeaderData(self.DATE, Qt.Horizontal, "날짜")
        model.setHeaderData(self.EXNAME, Qt.Horizontal, "운동이름")
        model.setHeaderData(self.HOURS, Qt.Horizontal, "시간")
        model.setHeaderData(self.EXNUM, Qt.Horizontal, "운동횟수")

        return model


    def addRec(self, model, date , exname, time, num ):
        model.insertRow(0)
        model.setData(model.index(0, self.HOURS), time)
        model.setData(model.index(0, self.EXNAME), exname)
        model.setData(model.index(0,self.EXNUM), num)
        model.setData(model.index(0, self.DATE), date)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QMainWindow()
    ui = Rec_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

