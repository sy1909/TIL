
from bigdata.inheritance.oop_inheritance02 import *

# tmpObj = Tmp('객체생성을 통한 인스턴스변수 바인딩')
# print( tmpObj.sayPrint() )
# tmpObj.callSayPrint()

# unit = Unit(100 , 100)
# status = unit.status()
# print(help(Unit))
# print('unit - status , ' , status)
# print('*** marine info ***')
# marine01 = Marine(100, 100, 50, 50)
# print('marine01 - status , ' , marine01.status())
# marine01.attack()
# marine01.stimPack()
# print('after stimPack marine01 - status , ' , marine01.status())
# print('*** medic info ***')
# medic01  = Medic(0 , 100 , 0)
# print('medic01 - status , ' ,  medic01.status())
# medic01.attack()

# marine01 = Marine(100, 100, 50, 50)
# marine02 = Marine(100, 100, 50, 50)
# marine03 = Marine(100, 100, 50, 50)
#
# medic01  = Medic(0 , 100 , 0)
# medic02  = Medic(0 , 100 , 0)
#
# ship = DropShip(0, 100)
# ship.board(marine01)
# ship.board(medic01)
# ship.board(marine02)
# ship.board(marine03)
# ship.board(medic02)

# unitList = [marine01 , marine02, marine03, medic01, medic02]
# ship.board(unitList)
# ship.attack()
# ship.drop()


# [실습]
# 1. Account class 작성 - account, balance, interestRate, type(계좌 종류 S|F)
# 1-1. SavingAccount , FundAccount 추가
# 1-2.  |                       |
# 1.3.  -- printInterestRate()  -- printInterestRate()
# 1.4  SavingAccount - printInterestRate()
#      기본 이자율에 만기시 이자율을(0.1) 복리로 계산
# 1.5  FundAccount - printInterestRate()
#      기본 이자율에 잔액 10만원 이상이며 10%
#      기본 이자율에 잔액 50만원 이상이며 15%
#      기본 이자율에 잔액 100만원 이상이며 20%

# 2. accountInfo() - 계좌의 정보를 출력한다(account, balance, interestRate)
# 3. deposit(amount) - 계좌 잔액에 매개변수로 들어온 amount를 누적한다.
# 4. printInterestRate() - 현재 잔액에 이자율을 계산하여 소수점 자리 2자리까지 출력한다.
# 5. withDraw(amount) - 매개변수로 들어온 금액만큼을 출금하여 잔액을 변경한다.
# 단) 잔고가 부족할 경우 '잔액이 부족하여 출금할 수 없습니다' 출력한다.

# class Account :
#     def __init__(self, account, balance, interestRate):
#         self.account = account
#         self.balance = balance
#         self.interestRate = interestRate
#     def accountInfo(self):
#         print("계좌번호 : {0} , 현재 잔액 : {1}".format(self.account, self.balance))
#     def deposit(self, amount):
#         self.balance += amount
#     def printInterestRate(self):
#         interest  = (self.balance) + self.balance * self.interestRate
#         print( "%.2f" % (interest) )
#     def withDraw(self, amount):
#         if (self.balance < amount) :
#             print("잔액이 부족하여 출금할 수 없습니다.")
#         else:
#             self.balance -= amount
#


# 다중상속 및 추상화
# print()
# print()
# liger = Liger()
# liger.play()
# liger.bite()
# liger.jump()
# liger.cry()
# liger.nonAbstractFunc()
# 추상클래스는 객체생성이 안된다.
# animal = Animal()
# tiger = Tiger()
# lion  = Lion()

# first-class function
# 실제적으로 모든 데이터 타입 및 함수를 -> 객체 취급한다

# def myFunc(x, y) :
#     return x + y
#
# print('call myFunc - ' , myFunc(10, 20))
# print('function address - ' , myFunc)
#
# myAddress = myFunc
# print(id(myAddress) , id(myFunc))
# print('call myAddress - ' , myAddress(10, 20))
#
# def myAdd(x, y) :
#     return x + y
#
# def myMul(x, y) :
#     return x * y
#
# def myFirstFunc(func , args) :
#     result = []
#     for (tmp01 , tmp02) in args :
#         result.append(func(tmp01, tmp02))
#     return result
#
# result = myFirstFunc(myMul , [(1,2) , (3,4) , (5,6)])
# print('result - ' , result )
# result = myFirstFunc(myAdd , [(1,2) , (3,4) , (5,6)])
# print('result - ' , result )
#


'''
예외
- SyntaxError
- NameError
- ZeroDivisionError
- IndexError
'''
# print('error)
# a = 10
# b = 20
# print(c)
# print( 100/ 0 )
# x = [1,2,3]
# print( x[3] )
# try :
#     names = ['jslim' , 'parksu' , 'admin']
#     searchName = 'park'
#     idx = names.index(searchName)
#     print('{} Found It!! {} in names'.format(searchName , idx))
# except Exception as e :
#     print('except block -  ' , str(e))
# else :
#     print('예외가 발생하지 않을 경우 수행되는 블럭')
# finally :
#     print('예외발생 여부와 상관없이 실행되는 블럭')

# userInput()

# myList = [10, 20, 25, 'num', 40, 50]
# listExcepFunc(myList)
try :
    result = positiveDivide(10, -3)
    print('call positiveDivide func - ' , result )
except UserNegativeDivisionError as e :
    print(e.msg)
except ZeroDivisionError as e :
    print('Error - ' , e.args[0])

print('process kill')












