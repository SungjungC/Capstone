import sqlite3

class Db:
    def __init__(self):
                self.connection = sqlite3.connect("HOME_FIT.db")
                self.curs = self.connection.cursor()

    def insertTable(self,email,nickname,password): # 가입할때 정보 삽입

        self.connection.execute("INSERT INTO EX_MEMBER (`MEM_EMAIL`, `MEM_NICKNAME`, `MEM_PASSWORD`) VALUES(?,?,?)", (email, nickname, password))
        self.connection.commit()


    def signupCheck(self,email):    # 가입할때 email 중복체크
        check =self.connection.execute("SELECT * FROM EX_MEMBER WHERE MEM_NICKNAME = ?",[email])
        checkC = len(check.fetchall())

        for data in check:
            print("email : ", data[1])

        if(checkC > 0):
            print("이미 있는 사용자 입니다")
            return True

        else:
            return False

    def signupNickCheck(self, nickname):  # 가입할때 닉네임 중복체크
        checkn = self.connection.execute("SELECT * FROM EX_MEMBER WHERE MEM_NICKNAME = ?", [nickname])
        checknC = len(checkn.fetchall())

        if (checknC > 0):
            return True
        else:
            return False



    def nicknameCheck(self,nickname):   # 닉네임 가져와서 넘기기
        userid = self.connection.execute("SELECT USER_ID FROM EX_MEMBER WHERE MEM_NICKNAME = ? ",[nickname])

        for data in userid:
            usersendid=data[0]
        return usersendid

    def forBMI(self,nickname):
        userid = self.connection.execute("SELECT USER_ID FROM EX_MEMBER WHERE MEM_NICKNAME = ? ", [nickname])

        for data in userid:
            useridforbmi=data[0]

        weight = self.connection.execute("SELECT USER_WEIGHT FROM EX_USER WHERE USER_ID = ? ", [useridforbmi])
        height = self.connection.execute("SELECT USER_HEIGHT FROM EX_USER WHERE USER_ID = ? ", [useridforbmi])

        for data in weight:
            usersendw =data[0]

        for data in height:
            usersendh = data[0]


        result = usersendw / (usersendh * usersendh) * 10000

        return result

    def forGoal(self, nickname):
        userid = self.connection.execute("SELECT USER_ID FROM EX_MEMBER WHERE MEM_NICKNAME = ? ", [nickname])

        for data in userid:
            useridforgoal = data[0]

        weight = self.connection.execute("SELECT USER_WEIGHT FROM EX_USER WHERE USER_ID = ? ", [useridforgoal])
        goalweight = self.connection.execute("SELECT USER_GOALWEIGHT FROM EX_USER WHERE USER_ID = ? ", [useridforgoal])

        for data in weight:
            usersendw = data[0]

        for data in goalweight:
            usersendg = data[0]

        result = 100*usersendg / usersendw

        return result

    def loginCheck(self,nickname,password): # 로그인할 때 확인
        result = self.connection.execute("SELECT * FROM EX_MEMBER WHERE MEM_NICKNAME = ? AND MEM_PASSWORD = ?",(nickname,password))
        count = len(result.fetchall())
        
        if(count > 0):
            print("로그인 성공")
            return True
                
        else:
            print("로그인 실패")
            return False


    def forrecord(self,nickname):
        userid = self.connection.execute("SELECT USER_ID FROM EX_MEMBER WHERE MEM_NICKNAME = ? ", [nickname])

        for data in userid:
            useridforrec = data[0]

        self.curs.execute("SELECT * FROM EX_REC WHERE USER_ID = ? ",[useridforrec])

        rows = self.curs.fetchall()
        checkC = len(rows)

        c = 0

        list = [[0] * 5 for i in range(checkC)]

        if(checkC == 0):
            print("ERROR")
        else:
            while(True):
                if(c==checkC):
                    break
                id = rows[c][0]
                name =rows[c][1]
                date =rows[c][2]
                time =rows[c][3]
                count =rows[c][4]



                list[c][0] = id
                list[c][1] = name
                list[c][2] = date
                list[c][3] = time
                list[c][4] = count

                c = c+1
        print(list)
        return list






        
