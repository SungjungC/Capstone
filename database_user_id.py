
import sqlite3

class Db2:
    def __init__(self):
        self.connection = sqlite3.connect("HOME_FIT.db")

    def insertTable(self, userid, sex, height, weight, goalweight):

        self.connection.execute("INSERT INTO EX_USER VALUES(?,?,?,?,?)", (userid, sex, height, weight, goalweight))
        self.connection.commit()

    def updateTable(self, userid, sex, height, weight, goalweight):



        self.connection.execute("UPDATE EX_USER SET USER_SEX=?, USER_HEIGHT=?, USER_WEIGHT=?, USER_GOALWEIGHT=? WHERE USER_ID=?",
                                    (sex,height,weight,goalweight,userid))

        self.connection.commit()



    def profileCheck(self, userid): #중복확인
        check = self.connection.execute("SELECT * FROM EX_USER WHERE USER_ID = ?", [userid])
        checkC = len(check.fetchall())

        print(checkC)

        if(checkC>0):
            return True
        else:
            return False