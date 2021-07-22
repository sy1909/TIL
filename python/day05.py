
# 학습목표 : 객체지향(oop)
# class vs instance
# 함수기반의 객체지향 - 클래스의 개념 또한 포함
# 함수 < 클래스(변수, 함수) < 모듈(xxx.py) < package
# 클래스 ?
'''
- 함수의 모음
- 역할 : 여러개의 함수와 공유 자료(변수)를 묶어서 관리하는 템플릿
- 구성 : 멤버 = 변수 + 함수(메서드) + 생성자
'''

from bigdata.oop.oop_day05 import *

# 인스턴스 생성
# instance = Person()
# instance.변수
# instance.함수()

# perName = '임임임'
# perAge  = 27
# perGender = 'M'
#
# def doing() :
#     print('{} 는 나이가 {} 이며 성별은 {} 이고 일하고 있다'.format(perName, perAge, perGender))
#
# doing()

# perObj = Person('임임임' , 49 , 'M')
# perObj.doing()
# print(perObj.name)
# print(perObj.age)
# print(perObj.gender)
#
# perObj02 = Person('섭섭해' , 29 , 'F')
# perObj02.doing()
# print(perObj02.name)
# print(perObj02.age)
# print(perObj02.gender)

# perList = []
# perList.append(Person('임임임' , 49 , 'M'))
# perList.append(Person('섭섭해' , 29 , 'F'))
#
# for obj in perList :
#     # print(dir(obj))
#     print(obj.perInfo())

# obj01 = Person('임임임' , 49 , 'M')
# obj01.printClsVar()
# Person.cls_var = 4.5
# obj01.printClsVar()
# 클래스 이름으로 인스턴스 소유의 함수 접근 불가
# Person.perInfo()
# Person.classFunc()


# empObj01 = Employee('jslim' , 1000 )
# print( empObj01.getSalary() )
#
# empObj02 = Employee('조조조' , 1200 )
# print( empObj02.getSalary() )
#
# # 급여 인상
# empObj01.incrementSalary()
# empObj02.incrementSalary()
# print( empObj01.getSalary() )
# print( empObj02.getSalary() )
#
# # 인상률 변경
# Employee.changeRate(1.5)
#
# # 급여 인상
# empObj01.incrementSalary()
# empObj02.incrementSalary()
# print( empObj01.getSalary() )
# print( empObj02.getSalary() )

# empObj01 = Employee('jslim' , 1000 )
# print( empObj01.getSalary() )
# empObj01.incrementSalary()
# print( empObj01.getSalary() )
# empObj01.instanceRate(1.5)
# empObj01.incrementSalary()
# print( empObj01.getSalary() )
#
# print('empObj02')
# empObj02 = Employee('조조조' , 1200 )
# print( empObj02.getSalary() )
# empObj02.incrementSalary()
# print( empObj02.getSalary() )

myDreamCar = Car('티코' , 4 , 4000)
myDreamCar.carInfo()

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
















