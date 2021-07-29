#import mpg as m
from statistics import mean
import pandas as pd
#import numpy as np
#from IPython.display import display 

file_path = 'C:\\Users\\ksy\\TIL\\python\\mpg.txt'
lines = pd.read_csv(file_path , sep =',')

# print(type(lines))
# print(lines.head())
# print(lines.columns) # 컬럼들 (= 피처들)

# print(lines.dtypes)  # 전체 컬럼들의 타입 
# print()

# print(lines["manufacturer"])
# print(lines["manufacturer"].unique()) #중복제거
# #lines[["displ" , "hwy"]] = lines[["displ" , "hwy"]].apply(pd.to_numeric)
# print()
# print(lines.dtypes)
#print(lines.loc[0:3])

# 1. displ(배기량)이 4 이하인 자동차와 5 이상인 자동차 중
# 어떤 자동차의 hwy(고속도로 연비)가 평균적으로 더 높은지 확인하세요.

def question01() :
    print("1번 문제")
#    print(lines[ lines["displ"] <= 4 ]["hwy"])
    displ04 = lines[ lines["displ"] <= 4 ]["hwy"].mean()
    displ05 = lines[lines["displ"] >= 5]["hwy"].mean()
    # print(lines[lines["displ"] <= 4]["hwy"].mean())
    # print(lines[lines["displ"] >= 5]["hwy"].mean())

    print('4 - ', displ04)
    print('5 - ', displ05)
    if displ04 > displ05:
        print('배기량 4의 연비가 더 높습니다.')
    else:
        print('배기량 5의 연비가 더 높습니다.')
    print()

question01()

# 2. 자동차 제조 회사에 따라 도시 연비가 다른지 알아보려고 한다.
# "audi"와 "toyota" 중 어느 manufacturer(제조회사)의 cty(도시 연비)가
# 평균적으로 더 높은지 확인하세요.

def question02():
    print("2번 문제")
    mpg_1 = lines[ lines["manufacturer"] == 'audi' ]["cty"].mean()
    mpg_2 = lines[lines["manufacturer"] == 'toyota']["cty"].mean()

    print("  audi - " , mpg_1)
    print("toyota - " , mpg_2)

    if mpg_1 > mpg_2:
        print('audi 가 연비가 더 높습니다.')
    else:
        print('toyota 가 연비가 더 높습니다.')
    print()

question02()

# 3. "chevrolet", "ford", "honda" 자동차의 고속도로 연비 평균을 알아보려고 한다.
# 이 회사들의 데이터를 추출한 후 hwy(고속도로 연비) 평균을 구하세요.


def question03():
    print("3번 문제")
    mpg_1 = lines[ lines["manufacturer"].isin( ["chevrolet", "ford", "honda"] ) ]["hwy"].mean()
    print('chevrolet", "ford", "honda 의 연비 평균은 - ' , mpg_1)
    print()

question03()

# 4. "audi"에서 생산한 자동차 중에 어떤 자동차 모델의 hwy(고속도로 연비)가
# 높은지 알아보려고 한다. "audi"에서 생산한 자동차 중 hwy가 1~5위에 해당하는
# 자동차의 데이터를 출력하세요.

def question04():
    print("4번 문제")
#    print(lines[lines["manufacturer"] == 'audi'])  
    mpg_1 = lines[ lines["manufacturer"] == 'audi'].sort_values(by=['hwy'] , ascending=False)[:5]
    print(mpg_1)
    print()
question04()

# 5. mpg 데이터는 연비를 나타내는 변수가 2개입니다.
# 두 변수를 각각 활용하는 대신 하나의 통합 연비 변수를 만들어 사용하려 합니다.
# 평균 연비 변수는 두 연비(고속도로와 도시)의 평균을 이용합니다.
# 회사별로 "suv" 자동차의 평균 연비를 구한후 내림차순으로 정렬한 후 1~5위까지 데이터를 출력하세요.

def question05():
    print("5번 문제")
    mpg_1 = []
    for instance in mpgList:
        if instance.getCls() == 'suv':
            mean_tot = (int(instance.getCty()) + int(instance.getHwy() ) ) /2
            mpg_1.append( [instance.getManufacturer() , mean_tot] )

    a = []
    for i in mpg_1:
#        print(i)
        a.append(i[0])
    b = list(set(a))
    print(b) #중복제거 항목

    result = []
    for j in b: # 각 제조사 별로 반복문 실행
        temp = 0 # 임시 저장 변수
        cnt = 0  # 얼마나 반복되었는지 확인할 카운트 변수
        for i in mpg_1:  # mpg_1 에서 [ instance.getManufacturer() , mean_tot ]
            if i[0] == j:   # i[0] = instance.getManufacturer() (제조사)
                temp += i[1] # temp = temp + i[1] (i[1]은 mean_tot 통합 연비)
                cnt += 1 # cnt = cnt + 1  (평균을 내기 위해 얼마나 세었나)
#                print(i[0] , temp , cnt)
        result.append( [j , round(temp/cnt , 1)] )  # j 는 제조사이고 , 통합연비로 더해진 부분을 cnt 로 나누면 평균
    # for i in result:
    #     print("result " , i)

#    print(result)
    result.sort(key = lambda x:-x[1])
    for i in result[0:5]:
        print(i)        
    print()   

question05()


# 6. mpg 데이터의 class는 "suv", "compact" 등 자동차의 특징에 따라
# 일곱 종류로 분류한 변수입니다. 어떤 차종의 도시 연비가 높은지 비교하려 합니다.
# class별 cty 평균을 구하고 cty 평균이 높은 순으로 정렬해 출력하세요.

def question06():
    print("6번 문제")
    mpg_1 = []
    for instance in mpgList:
        mpg_1.append( [instance.getCls() , int(instance.getCty())] )    
    a = []
    for i in mpg_1:
        a.append(i[0])
    b = list(set(a))
#    print(b)

    result = []
    for j in b:
        temp = 0
        cnt = 0
        for i in mpg_1:
            if i[0] == j:
                temp += i[1]
                cnt += 1
                #print(i[0] , temp , cnt)
        result.append( [j , round(temp/cnt , 1)] )

    result.sort(key = lambda x:-x[1])
    for i in result:
        print(i)        
    print()   
question06()

# 7. 어떤 회사 자동차의 hwy(고속도로 연비)가 가장 높은지 알아보려 합니다.
# hwy(고속도로 연비) 평균이 가장 높은 회사 세 곳을 출력하세요.

def question07():
    print("7번 문제")
    mpg_1 = []
    for instance in mpgList:
        mpg_1.append( [instance.getManufacturer() , int(instance.getHwy())] )   
    a = []
    for i in mpg_1:
        a.append(i[0])
    b = list(set(a))
#    print(b)

    result = []
    for j in b:
        temp = 0
        cnt = 0
        for i in mpg_1:
            if i[0] == j:
                temp += i[1]
                cnt += 1
                #print(i[0] , temp , cnt)
        result.append( [j , round(temp/cnt , 1)] )

    result.sort(key = lambda x:-x[1])
    for i in result[0:3]:
        print(i)        
    print()   
question07()

# 8. 어떤 회사에서 "compact" 차종을 가장 많이 생산하는지 알아보려고 합니다.
# 각 회사별 "compact" 차종 수를 내림차순으로 정렬해 출력하세요.

def question08():
    print("8번 문제")
    mpg_1 = []
    for instance in mpgList:
        if instance.getCls() == 'compact':
            mpg_1.append( [instance.getManufacturer() , instance.getCls()] )
    a = []
    for i in mpg_1:
        a.append(i[0])
    b = list(set(a))
#    print(b)

    result = []
    for j in b:
        cnt = 0
        for i in mpg_1:
            if i[0] == j:
                cnt += 1
                #print(i[0] , temp , cnt)
        result.append( [j , cnt] )

    result.sort(key = lambda x:-x[1])
    for i in result:
        print(i)        
    print()      

question08()



# getManufacturer()
# getModel()
# getDispl()
# getYear()
# getCyl()
# getTrans()
# getDrv()
# getCty()
# getHwy()
# getFl()
# getCls()
