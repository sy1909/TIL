
def sayPrint() :
    return '모듈에 정의된 일반 함수 입니다'

class Tmp(object) :
    def __init__(self, msg):
        self.msg = msg

    def sayPrint(self):
        return self.msg

    def callSayPrint(self):
        print(sayPrint())
        print(self.sayPrint())


class Unit(object) :
    def __init__(self , damage , life):
        self.__utype  = self.__class__.__name__
        self.__damage = damage
        self.__life   = life

    def setDamage(self , damage):
        self.__damage = damage

    def setLife(self, life):
        self.__life = life

    def getType(self):
        return self.__utype
    def getDamage(self):
        return self.__damage
    def getLife(self):
        return self.__life
    def status(self):
        return '타입 : {}\t공격력 : {}\t생명력 : {}\t'.format(self.__utype , self.__damage , self.__life)

    def attack(self):
        pass


# 다형성
# 부모에 정의된 함수를 자식에서 재정의(overriding)하는 것
# 자식에서 재정의되는 함수는 구현부(body)가 부모와 달라야 된다.

class Marine(Unit) :
    def __init__(self, damage , life , offenseUp , defenseUp):
        self.__utype = self.__class__.__name__
        super().__init__(damage , life)
        self.__offenseUp = offenseUp
        self.__defenseUp = defenseUp
    # setXXX() , getXXX()
    def status(self):
        return super().status() + '공격력 업그레이드 : {}\t방어력 업그레이드 : {}'.format(self.__offenseUp, self.__defenseUp)
    def attack(self):
        print('마린 공격개시~~~ 땅!땅!땅!')

    def stimPack(self):
        if super().getLife() > 40 :
            print('마린이 stimpack 을 사용합니다')
            super().setDamage( super().getDamage() * 1.5 )
            super().setLife( super().getLife() - 10 )
        else :
            print('체력이 낮아 마린이 stimpack 을 사용할 수 없습니다')

class Medic(Unit) :
    def __init__(self, damage, life, defenseUp):
        self.__utype = self.__class__.__name__
        super().__init__(damage, life)
        self.__defenseUp = defenseUp

    def status(self):
        return super().status() + '방어력 업그레이드 : {}'.format(self.__defenseUp)

    def attack(self):
        print('메딕이 마린을 치료합니다~~~ 찌찌찍')


class DropShip(Unit) :
    def __init__(self, damage , life):
        self.__utype = self.__class__.__name__
        super().__init__(damage , life)
        self.unitList = []

    def attack(self):
        print('dropship 이 마린과 메딕을 목표지점으로 수송합니다.~~~~잘 날아갑니다')

    # def board(self , crew):
    #     print('부대원을 태운다.')
    #     self.unitList.append(crew)

    def board(self , unitList):
        self.unitList = unitList

    def drop(self):
        for unit in self.unitList :
            if isinstance(unit , Marine) :
                unit.stimPack()
            unit.attack()


# 다중상속 , 추상화
# 추상클래스 -> 추상메서드
# 인스턴스를 생성 X

from abc import *

class Animal(object , metaclass=ABCMeta) :
    @abstractmethod
    def cry(self):
        pass
    def nonAbstractFunc(self):
        print('나는 추상클래에서 정의된 일반함수 입니다')

class Tiger(Animal) :
    def jump(self):
        print('호랑이가 점프를 한다.')
    def cry(self):
        print('어흥')
class Lion(Animal) :
    def bite(self):
        print('한 입에 꿀꺽한다.')
    def cry(self):
        print('캬오')
class Liger(Lion , Tiger) :
    def play(self):
        print('라이거가 사육사를 데리고 놀다가 꿀꺽했습니다.~')



'''
예외처리구문
try     :
    예외가 발생 할 가능성이 있는 코드 
except  :
    발생한 예외를 잡기위한 객체를 정의하고 처리하는 코드
except  :
    발생한 예외를 잡기위한 객체를 정의하고 처리하는 코드
else    :
    예외가 발생되지 않을 때 실행되는 블럭
finally :
    예외발생 여부와 상관없이 실행되는 블럭
'''
# XXXXXError

def userInput() :
    try :
        age = int(input('나이를 숫자로 입력하세요 : '))
    except ValueError as e :
        # print(str(e))
        userInput()
    else :
        print('your age is ', age, 'years old')
'''
매개변수로 넘겨 받은 각 첨자번지의 값에 제곱한 결과를 출력할려고 한다
예외 발생을 확인하고 예외처리 구문을 추가하여
정상적인 흐름의 함수 호출이 되도록 만들어 본다면?
'''
def listExcepFunc(userList) :
    try :
        for element in userList :
            print('raw - ' , element)
            squared = element ** 2
            print('squared - ' , squared)
    except Exception as e :
        print(str(e))

    print('function end~~')

# 사용자정의 예외 클래스 만들기
class UserNegativeDivisionError(Exception) :
    def __init__(self, msg):
        self.msg = msg

def positiveDivide(x, y) :
    if(y < 0 ) :
        raise UserNegativeDivisionError('음수 값으로 나눌 수 없습니다')
    return x / y




