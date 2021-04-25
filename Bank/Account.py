class Account:
    def __init__(self,userid=None,username=None,userbalance=None):
        self.__userid = userid
        self.__username = username
        self.__userbalance = userbalance

    def getUserid(self):                                      
        return self.__userid

    def getUserName(self):
        return self.__username

    def getUserbalance(self):
        return self.__userbalance   

    def deposit(self,money):       #예금       
        self.__userbalance = self.__userbalance+money 

    def withdraw(self,money):      #출금
        if self.__userbalance<money:
            print("출금할 금액이 잔여 금액",self.__userbalance,"보다 많습니다.")
        else:
            self.__userbalance = self.__userbalance-money
            
class BankManager:
    def __init__(self):
        self.accountlist = []

    def makeAccount(self): #계좌개설을 담당할 메서드
        userid = int(input("계좌번호: "))
        if self.idcheck(userid):
            username = input("이름: ")
            userbalance =int(input("예금: "))  
            self.accountlist.append(Account(userid,username,userbalance))
            print("##계좌개설을 완료하였습니다##")
        else:
            print("생성할 수 없습니다.")

    def idcheck(self,userid):
        for i in range(len(self.accountlist)):
            if self.accountlist[i].getUserid() == userid:
                print("중복된 계좌번호가 존재합니다.")
                return False
        return True

    def deposit(self):   #입금처리 담당
        userid=input("입금하실 계좌번호를 입력해주세요: ")
        for i in range(len(self.accountlist)):
            if self.accountlist[i].getUserid() == userid:
                print("계좌번호: ", self.accountlist[i].getUserid(), " / 이름: ", self.accountlist[i].getUserName(), " / 잔액: ", self.accountlist[i].getUserbalance())
                self.accountlist[i].deposit(int(input("입금하실 금액을 입력해주세요: ")))
                print("계좌번호: ", self.accountlist[i].getUserid(), " / 이름: ", self.accountlist[i].getUserName(), " / 잔액: ", self.accountlist[i].getUserbalance())
                break 
            else:
                print("존재하지 않는 계좌번호입니다.")

    def withdraw(self): #출금처리 담당
        userid=input("출금하실 계좌번호를 입력해주세요: ")   
        for i in range(len(self.accountlist)):
            if self.accountlist[i].getUserid() == userid:
                print("계좌번호: ", self.accountlist[i].getUserid(), " / 이름: ", self.accountlist[i].getUserName(), " / 잔액: ", self.accountlist[i].getUserbalance())
                self.accountlist[i].withdraw(int(input("출금하실 금액을 입력해주세요: ")))
                print("계좌번호: ", self.accountlist[i].getUserid(), " / 이름: ", self.accountlist[i].getUserName(), " / 잔액: ", self.accountlist[i].getUserbalance())
                break
            else:
                print("존재하지 않는 계좌번호입니다.")        

    def showAccount(self): # 전체고객의 계좌정보 출력
        for i in range(len(self.accountlist)):
            print("계좌번호: ",self.accountlist[i].getUserid()," / 이름: ",
                  self.accountlist[i].getUserName()," / 잔액: ",self.accountlist[i].getUserbalance())

class BankingSystem:
        a=BankManager()
        while True:
            num=input("======== Bank Menu ========\n1.계좌개설\n2.입금하기\n3.출금하기 \n4.전체조회 \n5.이체하기 \n6.종료하기 \n===============================\n")
            if num=="1":
                print("===========계좌개설=============")                
                a.makeAccount()         
            elif num=="2":
                print("===========입금하기=============")
                a.deposit()
            elif num=="3":
                print("===========출금하기=============")               
                a.withdraw()             
            elif num=="4":
                print("===========전체조회=============")             
                a.showAccount()      
            elif num=="5":
                print("============================")
                print("    프로그램이 종료됩니다   \n")
                print("============================\n")
                break
            else:
                print("잘못 입력하셨습니다")