
# 주석문 & 출력함수

# print('섭섭이와 함께하는 즐겁않는 파이썬 수업~~')
#
# '''
# 우리는 달려간다
# 이상한 나라로 ~ 섭섭이가 잡혀있는 마왕의 소굴로
# 어른들은 모르는
# '''

# print('''우리는 달려간다
# 이상한 나라로 ~ 섭섭이가 잡혀있는 마왕의 소굴로
# 어른들은 모르는''')

# print() : sep , end
# print('010' , '4603' , '2283' , sep='-')
# print('P','Y','T','H','O','N' , sep='')
# print('jslim9413' , 'naver.com' , sep='@')
# print('Welcome To ', end=' ')
# print("Seop's World")

# format (d, s, f)
# print('{} {}'.format('one' , 'two'))
# print('{1} {0}'.format('one' , 'two'))
# print('%s %d' % ('one' , '100'))

# 자리수 지정
# print('%10s' % 'seop')
# print('%-10s' % 'seop')
# print('%5s' % 'pythonGood')
#
# print('%d' % 100)
# print('%1.3f' % 3.14159)
#
# print('{:>10}'.format('nice'))
# print('{:_>10}'.format('nice'))
# print('{:$>10}'.format('nice'))
# print('{:10}'.format('nice'))
# 중앙정렬
# print('{:^10}'.format('nice'))
# 절삭 .
# print('%.5s' % 'pythonstudy')
# print('{:10.5}'.format('pythonstudy'))
# print('{:.5}'.format('pythonstudy'))
# print('%4d' % 42)
# print('{:4d}'.format(42))

# 변수 Variable
'''
Built-In Types
- Numeric
- Sequence
- Text Sequence
- Set
- Mapping(dict , tuple)
- Boolean
- Class(Object Oriented Programming)
변수 지정방법
- Camel  Case -> function , method (ex numberOfCollege)
- Pascal Case -> class (ex NumberOfCollege)
- Snake  Case -> variable , method , function (ex number_of_college)
주의사항
변수는 숫자로 시작할 수 없다
허용되는 특수문자 _ , $
예약어는 변수명으로 사용이 불가
'''
# year  = 2021
# month = 7
# day   = 14
#
# print('{}년 {}월 {}일'.format(year , month , day))
# print(type(year) , type(month) , type(day))
#
# import keyword
# print(keyword.kwlist)
#
intValue   = 123
floatValue = 3.14
boolValue  = True
strValue   = 'jslim'
print( type(intValue) , type(floatValue) , type(boolValue) , type(strValue))

# 형변환
numStr = "720"
numCnt = 100

print( numStr + str(numCnt) )
print( int(numStr) + numCnt )

# list
# list = ['jslim' , 'python' , numStr]
# print(list , type(list))
# print(list[0])

# dict(key , value)
# dict = {
#     "name"    : "machine Learning" ,
#     "version" : 2.0
# }
# print(dict, type(dict))

# tuple()
# tuple = (3,5,7)
# print(tuple , type(tuple))

# set {}
# set = {3,5,7}
# print(set , type(set))

# input()
# 키보드 입력시 사용하는 함수

# inputNum = int(input('숫자를 입력하세요 : '))
# print(inputNum + 100)

# 문자형(중요)
str01 = "I am Python"
str02 = 'I am Python'
str03 = """this is a
           multi line"""
str03 = '''this is a
           multi line'''

query = '''
select  *
from    emp
where   deptno = {no}
order by eno desc
'''

seqTxt = 'Talk is cheap. Show me the code'
print(seqTxt , type(seqTxt) , len(seqTxt))
print(dir(seqTxt))

# 문자열의 인덱싱 및 슬라이싱 가능하다
print(seqTxt[-1])
print(seqTxt[0:4])

strSlicing = 'nice Python'
print(strSlicing[0:4])
print(strSlicing[5:])
print(strSlicing[0:len(strSlicing):2])
print(strSlicing[-6:])
print(strSlicing[::-1])

# 홀만 출력한다면?
# [start : end-1 : step]
exStr = '홀짝홀짝홀짝홀짝홀짝홀짝'
print( type(exStr))
print(exStr[::2])
print(exStr[1::2])
print('Capitalize : ' , strSlicing.capitalize())

phone_number = "010-4603-2283"
print(phone_number , phone_number.replace('-' , " "))
dumpStr = "sakljalfjelkjasdfjalekjlajlasjdfa"
print(dumpStr , dumpStr.replace('a' , "A"))
print(dumpStr , dumpStr.upper())

# 문자열에서 도메인만 출력
url = 'http://www.naver.com'
print(url[-3:])
print(url[-3:] , url[url.find('com'):])
print(url[len(url)-3 : ])

url_list = url.split('.')
print(url_list , type(url_list) , url_list[-1])

company_name = "   삼성전자   "
# strip() , rstrip() , lstrip()
print(company_name * 4)
print(company_name.strip() , company_name.rstrip() , company_name.lstrip())
print(len(company_name.strip()) , len(company_name.rstrip()) , len(company_name.lstrip()))

company_name = "samsung"
# upper() , lower()
print(company_name.upper() , company_name.upper().lower())

# 확장자가 xls , xlsx 파일인지 여부를 확인하고 싶다면?
# endswith()
file_name = 'report.xls'
print(file_name , file_name.endswith(('xls' , 'xlsx')) , type(file_name.endswith(('xls' , 'xlsx'))))

dumyTxt = 'apple banana fineapple mango grape melon'
# in , not in -> T | F
print('Apple'.lower() in dumyTxt)

drinking = 'cocacola'
print( len(drinking) , drinking.count('c') , drinking.find('l') , drinking.index('a'))

x = '::'
y = 'abcd'
print( x.join(y) )

# list (중요)
# array X  , R - Vector
# 순서 0 , 중복 0 , 수정, 삭제 가능
# index 0 ~
# 선언 [] 또는 list()
# dumyList = []
# dumyList = list()
# print(dumyList)

dumyList = [1,2,3,4]
print(dumyList)

dumyList = [1,2,3,4 , 'jslim' , ['show' , 'me' , 'the' , 'money'] ]
print(dumyList , type(dumyList))
print( dumyList[5][1] )
print( dumyList[-1][1:3] )

# list 연산 가능
x = [1,2,3]
y = [4,5]
z = x + y
print(z ,  type(z))
print( z[0] )
z[0] = 10
print(z ,  z[0] )
z.append(7)
print('append - ' , z)
z.insert(0,6)
print('insert - ' , z)

# inplace = True
z.sort()
print('sort   - ' , z)
z.reverse()
print('reverse - ' , z)

print('result - ' , z , z[0] , z)
# pop() : 기존 리스트에서 원소를 가져오고 삭제
print('pop - ' , z.pop(0) , z )

# ---- 실습
movie_rank = ['그루엘라' , '랑종' , '모가디슈' , '블랙위도우' , '강철비2' , '반도' , '킹덤']
'''
1. 배드맨을 마지막에 추가
2. 랑종과 모가디슈 사이에 임정섭을 추가
3. 블랙위도우 삭제
4. 모가디슈와 강철비2 삭제
5. 그루엘라의 인덱스를 구해서 pop()함수를 이용한 삭제
6. 최종 리스트 출력 
'''







































