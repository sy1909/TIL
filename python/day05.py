# [실습]
# 1. Account class 작성 : 인스턴스 변수 - account, balance, interestRate
# 2. accountInfo() - 계좌의 정보를 출력한다(account, balance, interestRate)
# 3. deposit(amount) - 계좌 잔액에 매개변수로 들어온 amount를 누적한다.
# 4. printInterestRate() - 현재 잔액에 이자율을 계산하여 소수점 자리 2자리까지 출력한다.
# 5. withDraw(amount) - 매개변수로 들어온 금액만큼을 출금하여 잔액을 변경한다.
# 단) 잔고가 부족할 경우 '잔액이 부족하여 출금할 수 없습니다' 출력한다.

class Account:
    def __init__(self , account , balance , interestRate):
        self.account = account
        self.balance = balance
        self.interestRate = interestRate

    def accountInfo(self):
        print(self.account , self.balance , self.interestRate)

    def deposit(self , amount):
        self.balance += amount

    def printInterestRate(self):
        self.balance += (self.balance * self.interestRate)
        #self.balance = self.balance * self.interestRate
        print(round(self.balance , 2))

    def withDraw(self , amount):
        if amount > self.balance:
            print('잔액이 부족하여 출금할 수 없습니다.')
        else:
            self.balance -= amount

# caller 쪽에서 객체생성후
account = Account('441-2919-1234' , 500000, 0.073)
account.accountInfo()
account.withDraw(600000)
account.deposit(200000)
account.accountInfo()
account.withDraw(600000)
account.accountInfo()
print("현재 잔액의 이자를 포함한 금액")
account.printInterestRate()