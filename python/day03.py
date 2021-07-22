
# boolean type
# True | False
# 논리연산자(not , and , or)
# 비교연산자(& , | , ~)
# "" , [] , () , {} , 0 , None -> False

# 32 16 8 4 2 1
a = 5 # 0101
b = 0 # 0000

print('boolean - ' , bool(-1) )
print('bitwise - ' , bool( (a&b) ) )
print('bitwise - ' , bool( (a|b) ) )

tmpList = []
tmpStr  = ""
print('list - ' , bool(tmpList)  , bool(tmpStr) , bool( (1,2,3) ))


trueFlag  = True
falseFlag = False

print('True - False '  , int(trueFlag) , int(False) )
print('and - & ' , trueFlag and falseFlag , trueFlag & falseFlag)
print('or  - | ' , trueFlag or  falseFlag , trueFlag | falseFlag)
print('not' , not trueFlag )

# 날짜~
'''
install.packages() = conda install ~~~ , pip install ~~~~~
libraray()
형식) from 패키지명.모듈 import 함수명
형식) from 모듈 import 함수명 또는 클래스 
형식) import 모듈이름
'''
from datetime import date , datetime
print('type' ,  type(date) )

today = date.today()
print('today - ' , type(today) , today)
print('year month day - ' , today.year , today.month , today.day)

user_time = datetime.today()
# print('time - ' , user_time , user_time.year , user_time.month , user_time.day)
print('time - ' , user_time.hour , user_time.minute , user_time.second)

# print('today + 1 - ' , today+1) -- error

from datetime import date , datetime ,  timedelta
from dateutil.relativedelta import      relativedelta

today = date.today()
days = timedelta(days=-1)
print('하루 전 날짜 - ' , (today+days))

days = relativedelta(days=+2)
print('이틀 후 날짜 - ' , (today+days))
months = relativedelta(months=-2)
print('두달 전 날짜 - ' , (today+months))
years = relativedelta(years=+2)
print('이년 후 날짜 - ' , (today+years))

# 특정날짜객체를 생성
from dateutil.parser import parse
userDate = parse('2019-7-16')
print('userDate - ' , userDate , type(userDate))

today = datetime.today()
print('today - ' , today , type(today))

# strftime() , strptime()
print('날자를 문자형태로 변경 - ' , userDate.strftime('%m-%d-%Y') , type(userDate.strftime('%m-%d-%y')) )
str = '19,7,16 , 10:29:12'
print('문자형을 날짜로 변경 - ' ,
      datetime.strptime(str , '%y,%m,%d , %H:%M:%S') ,
      type(datetime.strptime(str , '%y,%m,%d , %H:%M:%S')))


# 제어문
# if 구문
# 들여쓰기(Indent)
# 블럭을 정의할 때 :
tmpList = [1]
if tmpList :
    print('pass')

# score = int( input('점수를 입력하세요 : ') )
# if score >= 60 :
#     print('pass')
# else :
#     print('fail')

# if 조건식 : elif : elif :
# 윤년
# 4의 배수이고 100의 배수가 아니거나 400의 배수일 때
year = 2020
if ( year % 4 == 0 and year % 100 != 0 ) or ( year % 400 == 0 ) :
    print('윤년')
else :
    print('평년')

# input()함수를 이용해서 연도와 월을 입력받아
# 해당년도가 윤년일 경우 2월달의 마지막일은 29 , 평년일경우 2월달의 마지막일은 28
# 출력의 형식은 : xxxx년 x월 마지막일은 xx일 입니다
# if 구문으로 작성 또는 if ~ elif
# year  = int(input('년도 입력 : '))
# month = int(input('달 입력 : '))
# year_month      = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31 ]
# leap_year_month = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31 ]
# if ( year % 4 == 0 and year % 100 != 0 ) :
#     print('{} 년 {} 월 마지막 일은 {} 입니다'.format(year , month , leap_year_month[month - 1]))
# elif ( year % 400 == 0 ) :
#     print('{} 년 {} 월 마지막 일은 {} 입니다'.format(year , month , leap_year_month[month - 1]))
# else :
#     print('{} 년 {} 월 마지막 일은 {} 입니다'.format(year, month, year_month[month - 1]))

# if ~ in 구문
# for ~ in
# fruits = {'봄' : '딸기' , '여름' : '토마토' , '가을' : '사과' , '겨울' : '귤'}
# season = input('계절 입력 : ')
# if season in fruits :
#     print(fruits.get(season))
# else :
#     print('정확한 계절을 입력하세요~')



# if month == 2:
#     if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0) :
#         lastday = 29
#         print('{}년 {}월 마지막일은 {}일 입니다.'.format(year,month,lastday))
#     else:
#         lastday = 28
#         print('{}년 {}월 마지막일은 {}일 입니다.'.format(year,month,lastday))
#
# elif month in [1,3,5,7,8,10,12]:
#     lastday = 31
#     print('{}년 {}월 마지막일은 {}일 입니다.'.format(year,month,lastday))
# else:
#     lastday = 30
#     print('{}년 {}월 마지막일은 {}일 입니다.'.format(year,month,lastday))


# year = int(input('년도 입력'))
# month = int(input('달 입력'))
# list31 = [1,3,5,7,8,10,12]
# if month!=2:
#     if month in list31:
#         print("{}년 {}의 마지막 달은 31일 입니다".format(year,month))
#     else:
#         print("{}년 {}의 마지막 달은 30일 입니다".format(year, month))
# else:
#     if (year%4==0 and year%100 !=0) or year%400 ==0:
#         print("{}년 {}의 마지막 달은 27일 입니다".format(year, month))
#     else:
#         print("{}년 {}의 마지막 달은 28일 입니다".format(year, month))

grade = 'A'
avg   = 91

# 중첩 조건문
if grade == 'A' :
    if avg >= 95 :
        print('장학금 100%')
    elif avg >= 90 :
        print('장학금 90%')

# 3항연산자 : 조건식 , 참, 거짓
# 형식) 변수 =  참 if 조건식 else 거짓
num = 9
if num >= 5 :
    result = num * 2
else :
    result = num + 2

result = num * 2  if num >= 5 else num + 2
print('result - ' , result )

# if ~ in , not in
tmpList = [10, 20, 30]
tmpSet  = {70, 80, 90}
tmpDict = {'name' : 'jslim' , 'city' : 'seoul' , 'gender' : 'M' }
tmpTpl  = (10, 12, 14)

if 'jslim' in tmpDict.values() :
    print('ok')
else :
    print('fail')

# 현재 13:22
# 현재 12:00
# 시간이 정각인지 아닌지를 구분하고 싶다면?
time = '12:01'
result = '정각입니다'  if  time[-2: ] == '00'  else '정각이 아닙니다'
print('time - ' , result )

# 011 SK , 016 KTF, 019 LGU
# 011-1234-1234
phoneNumber = '016-1234-1234'
brand = phoneNumber.split('-')[0]
# print(brand)
if brand == '011' :
    print('SK')
elif brand == '016' :
    print('KTF')
else :
    print('LGU')

# 주민번호 >> 성별 >> xxxxxx-1xxxxxx
# 3항연산자
# 지역코드 00 ~ 08 : 서울지역
ssn = 'xxxxxx-107xxxx'
gender = ssn.split('-')[1]
result = '남자' if gender[0] == '1' or gender[0] == '3' else '여자'
print('gender - ' , result )
# 출생지역 구분
location = 'seoul' if int(ssn[8:10]) in range(0,9) else 'not seoul'
print(location)
print('서울') if int(ssn.split('-')[1][1:3]) > 0 and int(ssn.split('-')[1][1:3]) <= 8 else print('서울아님')

# 1 ~ 10 사이의 난수를 생성하고 숫자를 맞춰보는 Guess Game
# 열고개 ~
# 정답시도횟수 : 0000 , 정답 000
# from random import randint
# answer = randint(1, 100)
# print('answer - ' , answer)
# tries = 1
# for idx in range(1, 11) :
#     guess = int(input('1 ~ 10 사이의 숫자를 입력하세요 : '))
#     if guess == answer :
#         break
#     elif guess > answer :
#         print('down')
#     else :
#         print('up')
#     tries += 1
# print('정답 {}  , 시되횟수 {}'.format(answer , tries) )

# print('answer - ' , answer)
# guess = int(input('1 ~ 10 사이의 숫자를 입력하세요 : '))
# if guess == answer :
#     print('정답')
# elif guess > answer :
#     print('숫자가 크네요..작은 숫자를 넣어주세요')
# else :
#     print('숫자가 작네요..큰 숫자를 넣어주세요')

# for , while
# for idx in <collection> :
# for idx in range(start , end , step) :
# for idx in str , dict , list :
endingMsg = 'see you next week'
for char in endingMsg :
    print(char , end=" ")
print()
# 리스트에 있는 요소의 cnt
cnt_list  = [1,2,3,23,4,5,6,4,5,5,3,21,1,43,5,6,3,23,4,3,2,3,4,2,3,54,2,2,34,23,4,2,4,5,65,3,2,24,5,6,65,3]
freq = {}
for i in cnt_list :
    if i in freq :
        freq[i] += 1
    else :
        freq[i] = 1
print('freq - ' , freq)




















