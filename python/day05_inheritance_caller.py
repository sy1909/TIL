
from bigdata.inheritance.oop_inheritance import *

# private vs public
obj = MyDate()
obj.setYear(-2021)
print( obj.getYear() )

sub = Sub()
echo = sub.sayEcho('jslim')
print('caller - ' , echo)

child = Child01('jslim' , 'instructor' , 32)
print( child.display() )

# PersonVO , StudentVO , TeacherVO
perList = []
perList.append(StudentVO('한한한' , 30 , '경기도' , '1992'))
perList.append(StudentVO('조조조' , 25 , '서울'   , '2016'))
perList.append(TeacherVO('임임임' , 31 , '광주'   , 'python'))
# 출력
for obj in perList :
    if isinstance(obj, StudentVO) :
        print( obj.stuInfo() )
    else :
        print(obj.teaInfo())




