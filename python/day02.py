
# list
num_list = [1,2,3,4,5,6,7]

print('max : ' , max(num_list))
print('min : ' , min(num_list))
print('sum : ' , sum(num_list))
print('mean : ', sum(num_list) / len(num_list))

list01 = [1,2,3]
list02 = [1,2,3]
print('object address : ' , id(list01) , id(list02))
# is 연산자 : 객체의 주소값을 비교
print('객체의 주소값을 비교' , list01 is list02 )

list03 = list01
print('object address : ' , id(list01) , id(list03) , list01 is list03)

list03.append('jslim')
print('list03 append - ' , list01)

from copy import copy
list04 = copy(list01)
print('object address : ' , id(list01) , id(list04) , list01 is list04)


# inner list
# [ [] , [] ]
a = ['a', 'b', 'c']
b = [10 , 3.14 , True , 'string' , a ]
print('inner list - ' , b[-1][1:]  , type(b[-1][1:]))

# range() : 숫자를 sequence
tmpRange = range(1 , 11 , 2)
print('range - ' , tmpRange , 10 in tmpRange)
for idx in tmpRange :
    print(idx , end='\t')

print()
import random

tmpList = []
for idx in range(5) :
    tmpList.append(random.randint(1,5))

print('tmpList - ' , tmpList)

if 4 in tmpList :
    print('ok')
else :
    print('fail')

'''
list Comprehension
list 안 for 구문 포함
변수 = [ 실행문 for 변수 in 열거형객체]
변수 = [ 실행문 for 변수 in 열거형객체 if 조건식]
'''
x = [2, 4, 1, 5, 3]
for value in x :
    print(value)
# x ** 2 -- error
result = [ value ** 2 for value in x if value%3 == 0 ]
print('comprehension result - ' , result)

# for + list
result = []
for value in x :
    calc = value ** 2
    if calc%3 == 0 :
        result.append(calc)
print('for + list result - ' ,result)

# range()함수를 이용해서 1 ~ 100 사이의 3의 배수만 출력해본다면?
# list Comprehension
result = []
for num in range(1, 101) :
    if num%3 == 0 :
        result.append(num)

print('3의 배수 result - ' , result)

result = [num for num in list( range(1, 101) ) if num%3 == 0]
print('3의 배수 result - ' , result)

print( list(range(1, 101)) , type(range(1, 101)))

# 튜플(tuple)
# 순서 0 , 중복 0 , 수정 X , 삭제 X - 불변(immutable)
# 읽기 전용
# 선언 () , tuple()
# indexing , scling
myTuple = (3,)
print( myTuple , type(myTuple))
myTuple = 1,2,3,4,5 , 4
print( myTuple , type(myTuple))
print( myTuple[0:2] , type(myTuple[0:2]))

a, b, c = (1,2,3)
print(a, b, c, type(a) )

# myTuple[0] = 10 -- error
# print('append - ' , myTuple)
# tuple -> list
print('index - ' , myTuple.index(4) )
print('count - ' , myTuple.count(4) )
myList = list(myTuple)

myList[0] = 10
print('append - ' , myList)

# 1 ~ 99까지의 정수 중 짝수만 튜플에 저장한다면?
data = tuple(range(2, 100, 2))
print(data , type(data))

# Packing & Unpacking
packing = ('최동렬' , '조수연' , '강려명' , '섭섭이')

k , j , g , s = packing
print(k, j, g, s)

a, *b, c = (0,1,2,3,4,5)
print(a, b, c , type(a) , type(b) , type(c))


# dict(key : value)
# 순서 X , 키 중복 X , 수정 0, 삭제 0
# 선언 {} , dict()

tmpDict = {}
print(tmpDict , type(tmpDict))

tmpDict = {
    'name'    : 'jslim' ,
    'address' : 'seoul'
}
print(tmpDict , type(tmpDict))

# 키 유무를 검삭할 수 있다
# in 연산자
print('birth' in tmpDict)

iceDict = {
    'melona'  : [300, 20] ,
    'bibibig' : [400, 20] ,
    'bravo'   : [100, 50]
}
print( iceDict , type(iceDict))

print('메로나의 가격은 %d 이고 수량은 %d 개입니다' % (iceDict['melona'][0] , iceDict['melona'][1]))
print('메로나의 가격은 {} 이고 수량은 {} 개입니다'.format(iceDict['melona'][0] , iceDict['melona'][1]))

# 메로나 가격을 인상한다
melonaValue = iceDict['melona']
print(melonaValue[0])
melonaValue[0] = melonaValue[0] * 1.1
print(melonaValue)

iceDict['melona'][0] = iceDict['melona'][0] * 1.1
print(iceDict)

tmpDict = dict([
    ('city', 'seoul') , ('age','27')
])
print(tmpDict , type(tmpDict))

tmpDict = dict(
    city = 'seoul' ,
    age  = 27
)

print(tmpDict , type(tmpDict))
# print('key를 이용한 값 출력 - ' , tmpDict['address']) -- error
# print('key를 이용한 값 출력 - ' , tmpDict.get[0]) -- error

print('key를 이용한 값 출력 - ' , tmpDict.get('address'))

# 요소를 추가하다면?
tmpDict.update({'name' : 'jslim'})
print('upadte - ' , tmpDict , type(tmpDict))

# zip
# 아래 두개의 튜플을 하나의 딕셔너리로 만들고 싶다면?
keys = ('apple' , 'pear' , 'peach')
vals = (1000 , 1500 , 2000)

keys = [1,2,3,4,5]
vals = [6,7,8,9,10]

zipDict = dict(zip(keys , vals))
print('zipDict - ' , zipDict , type(zipDict))

# print(len(keys) , len(vals))
# size = len(keys)
# zipDict = {}
# for idx in range(size) :
#     zipDict.update({keys[idx] : vals[idx]})
# print('zipDict - ' , zipDict , type(zipDict))

print( tmpDict )

# dict_keys , dict_values , dict_items
for key in tmpDict.keys() :
    print('{} :  {}'.format(key , tmpDict.get(key)))
for value in tmpDict.values() :
    print(value)
for key , value in tmpDict.items() :
    print('{} :  {}'.format(key , value))

# 없애기
tmpDict.clear()
print( tmpDict )


# set 집합의 자료형
# 순서 X , 중복 X
# 선언 {} , set()
# i, s X
tmpSet = {1,2,3,3,3,3,3,3,'jslim'}
print( tmpSet , type(tmpSet) )

tmpSet = set([1,2,3,4,4, 'jslim'])
print( tmpSet , type(tmpSet) )
# print( tmpSet[0] ) -- error
tmpT = tuple(tmpSet)
print( tmpT , type(tmpT) )
tmpL = list(tmpT)
print( tmpL , type(tmpL) )

s01 = set([1,2,3,4,5,6])
s02 = set([4,5,6,7,8,9])

# 교집합(intersection) & , 합집합(union) | , 차집합(difference) -
print('교집합(intersection) & ' , s01.intersection(s02)  , s01&s02)
print('합집합(union) ' , s01.union(s02)  , s01|s02)
print('차집합(difference) - ' , s01.difference(s02)  , s01-s02)

# 중복제거
gender  = ['남','남','남','여','남','여','남','여','남','여','여']
sgender = set(gender)
print('중복제거 - ' , sgender)

lgender = list(sgender)
print( lgender )

lst = list(range(1, 101))
print('lst - ' , lst )
slst = set(lst)
print('slst - ' , slst)

for value in slst :
    print(value , end = ' ')

print()

wc = {}
wc['love'] = 1
print('wc' , wc)

# 단어의 빈도수를 구해보자
# { love : 2 , jslim : 2 , cat : 2 , word : 1 , lucky : 3 }
word_list = ['love' , 'jslim' , 'cat' , 'cat' , 'jslim' , 'word' , 'love' , 'lucky', 'lucky', 'lucky']
wc = {}
for word in word_list :
    wc[word] = wc.get(word , 0) + 1
print('wc' , wc)

# case 01
dict(zip(set(word_list) , [word_list.count(i) for i in set(word_list)]))

# case 02
word_set = list(set(word_list))
tmpDict ={}
for i in word_set :
    tmpDict.update({i : word_list.count(i)})

# case 03
word_list = ['love','jslim','cat','cat','jslim','word','love','lucky','lucky','lucky']
word_set = set(word_list)
word_cnt = {}
for word in word_set:
    cnt = 0
    for i in range(len(word_list)):
        if word_list[i] == word:
            cnt +=1
    word_cnt[word] = cnt
print(word_cnt)


# list : [] , tuple : () , set : {} , dict : {key , value}




















