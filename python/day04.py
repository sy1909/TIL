
# 반복구문 (for ~  , while)

for v1 in range(10) :
    print('v1 is ' , v1)
print()
for v2 in range(1, 11) :
    print('v2 is ' , v2)

print()
for v3 in range(1, 11, 2) :
    print('v3 is ' , v3)

print()
# scores = []
# for i in range(5) :
#     scores.append( int(input('점수 입력 : ')))
#
# for element in scores :
#     print(element)
# print()
#
# for idx in range(len(scores)) :
#     print(scores[idx] , end='\t')
# print()
# print('scores 총합 평균')
# sum = 0
# avg = 0
# for idx in range(len(scores)) :
#     sum += scores[idx]
#
# print('총합 : ', sum)
# print('평균 : ', sum / len(scores) )

# while~
# dogNames = []
# isFlag = True
#
# while isFlag :
#     name = input('애완견의 이름을 입력하세요(종료시 엔터키 입력) : ')
#     if name == "" :
#         isFlag = False
#         # break
#     else :
#         dogNames.append(name)
# print('outer while : ' , dogNames )

# while 이용한 guessGame
# from random import randint
# answer = randint(1, 100)
# print('answer - ' , answer)
# tries = 1
# while tries <= 10 :
#     guess = int(input('1 ~ 10 사이의 숫자를 입력하세요 : '))
#     if guess == answer :
#         break
#     elif guess > answer :
#         print('down')
#     else :
#         print('up')
#     tries += 1
# print('정답 {}  , 시도횟수 {}'.format(answer , tries) )

tmpList = [ ('name' , 'jslim') , ('age' , 20) , ('address' , 'seoul') ]
for key , value in tmpList :
    # print(e)
    print('{} , {}'.format(key , value))

tmpList = [1,2,3,4,5,6,7,8,9]
myList  = []
for e in tmpList :
    myList.append(e*2)
print(myList)

myList  = [ e * 2 for e in tmpList if e % 2 == 0 ]
print(myList)

# 올림픽은 4년 개최
# 2000 ~ 2050 년 사이의 올림픽이 개최되는 년도를 출력
# 한 줄에 5개년도씩 출력
# print(end=)
cnt = 0
for year in range(2000 , 2051 , 4) :
    cnt += 1
    if cnt%5 == 0 :
        print(year , end='\n')
    else :
        print(year , end='\t')

# 아래 리스트에서 세 글자 이상인 문자만 출력한다면?
# len()
print()
tmpList = ['I' , 'AM' , 'study' , 'PYTHON' , 'language' , '!']
for e in tmpList :
    if len(e) >= 3 :
        print(e)

# 대문자인 문자들만 출력
# isupper()
for e in tmpList :
    if e.isupper() :
        print(e)

# 확장자를 제외하고 파일 이름만 출력한다면?
# split()
tmpList = ['greeting.py' , 'ex01.py' , 'intro.hwp' , 'bigdata.doc']
for idx in range(len(tmpList)) :
    print( tmpList[idx].split('.')[0])

# 구구단
# 이중 루프구문
# 출력형식
# 2 * 1 = 2 , 2 * 2 = 4
# break , continue
for i in range(2, 10) :
    for j in range(1, 10) :
        print('{} * {} = {}'.format(i, j, (i*j) ) , end='\t')
    print()
    if i == 5:
        break

# 인덱스 번호와 요소값을 확인 할 수 있는 enumerate()
tmpList = ['greeting.py' , 'ex01.py' , 'intro.hwp' , 'bigdata.doc']
for idx , value in enumerate(tmpList) :
    print('{} 번째 인덱스이고 값은 {} 입니다'.format(idx , value))

# 분류정확도
answer = [1, 0, 2, 1, 0]
pridct = [1, 0, 2, 0, 0]
acc = 0
for i in range(len(answer)) :
    fit = answer[i] == pridct[i]
    # print(int(fit) , end='\t')
    acc += int(fit) * 20
print('분류정확도는 {}% 입니다'.format(acc) )

# for ~ else
numbers = [14, 3, 4, 7, 45, 17, 8, 65, 34]
for num in numbers :
    if num == 17 :
        print('Found - ' , 17)
        break
else :
    print('Not Found - ' , 17)

apartments = [ ['101호', '102호'] , ['201호', '202호'] , ['301호', '302호'] ]
for row in apartments :
    for col in row :
        print(col)
    print('------')

# function : 사용자 정의 함수를 만들어본다면?

from bigdata.study.userFunc import *
# from bigdata.study import userFunc

# 호출
# printGreeting()
# printCoin()
# result = mySum(1,2)
# print('call mySum() - ' ,result)

# msg = returnMsg(10)
print('msg - ' , printCoin() )

# 변수의 스코프
data = [1,3,5,7,9]
tot  = 0
# for d in data :
#     tot += d
# print('tot - ' , tot)

def totalCalc(data) :
    total = 0
    for d in data :
        total += d
    return total

print( totalCalc(data) )
print('tot - ' , tot)


oddSum , evenSum = countSum(1, 1000)
print('unpacking - ' , oddSum , evenSum)

# makeUrl() call
# print('makerUrl call - ' , makeUrl('naver'))
# makeUrl() call - list
url = ['naver', 'goggle' , 'samsung']
urlList = makeUrl(url)
print(urlList)

# 입력 문자열을 한줄에 다섯글자씩 출력하는 print_5line(line) 함수를 작성해보자
print_5xn('아이엠어보이유알어걸')

# 숫자로 구성된 리스트를 입력받아 , 짝수들을 추출하여 리스트로 반환하는 pickupEven 함수를 구현하라
myList = [3, 4, 10, 23, 34, 3, 6]

result = pickupEven(myList)
print('result - ' , result )

argsTuple('kim')
argsTuple('kim' , 'lim')
argsTuple('kim' , 'lim', 'park')

userStatistic('SUM' , 1,2,3,4)
userStatistic('AVG' , 1,2,3,4,5)
userStatistic('STD' , 1,2,3)

kwargsDict(name='jslim')
kwargsDict(name='jslim' , name1='parksu')
kwargsDict(name='jslim' , name1='parksu' , name2 = 'cho')

personInfo(77, 178, name='jslim' , address='seoul', gender='M')

# 전체혼합
mixtype(10, 20, 'kim', 'lim', 'park', 'cho' , age1 = 20 , age2 = 30 , age3 = 40 )

# lambda 함수
# lambda 인자 : 구현부
# def mulFunc(x, y) :
#     return x * y

lambdaFunc = lambda x, y  : x * y
print( lambdaFunc(10, 20) )

def func_final(x, y, func) :
    print(">>>> " , x * y , func(x, y))

func_final(10, 20 ,  lambda x, y : x * y)

# Hint
def tot_length(word : str , num : int ) -> int :
    return len(word) * num

print('hint - ' , tot_length('i love you' , 10))

def tot_length2(word : str , num : int ) -> None :
    print('hint - ' , len(word) * num )

tot_length2('niceman' , 10)

# 인자로 넘겨받은 년도에서 윤년에 해당하는 년도만 한 줄에 5개씩 출력
leap_year_list = leay_year_loop(1900, 2021)
print('leap year - ' , leap_year_list)

cnt = 0
for idx in range(len(leap_year_list)) :
    print(leap_year_list[idx] , end='\t')
    cnt += 1
    if cnt%5 == 0 :
        print()





