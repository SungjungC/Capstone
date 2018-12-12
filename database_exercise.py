import sqlite3
from PyQt5 import QtCore, QtGui, QtWidgets
import easygui

class Db3:
    def __init__(self):
        self.connection = sqlite3.connect("HOME_FIT.db")
        self.curs = self.connection.cursor()

    def searchEx(self, level, part, tool):
        r = self.curs.execute("SELECT INFO_NAME FROM EX_INFO WHERE INFO_DIFF = ? AND INFO_PART = ? AND INFO_TOOL = ?",
                                          (level, part, tool))
        rows = self.curs.fetchall()

        checkC = len(rows)
        print(checkC)
        c =0
        list = []

        if(checkC == 0):
            easygui.msgbox("조건에 맞는 운동이 없습니다.", "운동목록")
            idcData=0
        else:
            while(True):
                if(c==checkC):
                    break
                name = rows[c][0]
                list.append(name)
                c = c+1

            #self.showMessage(list)
            msg = "선택 된 조건에 맞는 운동 목록입니다\n\n운동을 시작하려면 ok버튼을 눌러주세요"
            title = "운동목록"
            select= easygui.choicebox(msg, title, list)
            print(select)

            idc = self.connection.execute(
                "SELECT INFO_ID FROM EX_INFO WHERE INFO_NAME = ?",[select])
            if(select==None):
                idcData=0
            for data in idc:
                idcData = data[0]
            print(idcData)
        self.connection.commit()
        return idcData
