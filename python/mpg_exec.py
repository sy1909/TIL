import mpg as m
from statistics import mean

mpgList = []

with open('C:\\Users\\ksy\\TIL\\python\\mpg.txt' , 'r' , encoding = 'utf-8') as file:
    lines = file.readline()
    lines = file.readlines()
#    print(lines[0])
    for line in lines :
        data = line.strip('\n').split(',')
        #print(data)
        instance = m.Mpg(data[0] , data[1] , data[2], data[3], data[4], data[5], data[6], data[7], data[8], data[9], data[10])
        mpgList.append(instance)


# 1. displ(배기량)이 4 이하인 자동차와 5 이상인 자동차 중
# 어떤 자동차의 hwy(고속도로 연비)가 평균적으로 더 높은지 확인하세요.

def question01() :
    print("1번 문제")
    displ04 = []
    displ05 = []
    for instance in mpgList:
        if float(instance.getDispl()) <= 4:
            displ04.append(int(instance.getHwy()))
        if float(instance.getDispl()) >= 5:
            displ05.append(int(instance.getHwy()))
    print('4 - ', mean(displ04))
    print('5 - ', mean(displ05))
    if mean(displ04) > mean(displ05) :
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
    mpg_1 = []
    mpg_2 = []
    for instance in mpgList:
        if instance.getManufacturer() == 'audi':
#            print("mpg1 실행" , instance.getManufacturer())
            mpg_1.append(instance.getCty())
        if instance.getManufacturer() == 'toyota':
#            print("mpg2 실행" , instance.getManufacturer())
            mpg_2.append(instance.getCty())
    mpg_1 = map(int, mpg_1)
    mpg_2 = map(int, mpg_2)
    m_mpg_1 = mean(mpg_1)
    m_mpg_2 = mean(mpg_2)
    print("  audi - " , m_mpg_1)
    print("toyota - " , m_mpg_2)

    if m_mpg_1 > m_mpg_2:
        print('audi 가 연비가 더 높습니다.')
    else:
        print('toyota 가 연비가 더 높습니다.')
    print()

question02()


# 3. "chevrolet", "ford", "honda" 자동차의 고속도로 연비 평균을 알아보려고 한다.
# 이 회사들의 데이터를 추출한 후 hwy(고속도로 연비) 평균을 구하세요.


def question03():
    print("3번 문제")
    mpg_1 = []
    for instance in mpgList:
        if instance.getManufacturer() in ["chevrolet", "ford", "honda"]:
            mpg_1.append(instance.getHwy())
    mpg_1 = map(int, mpg_1)
    m_mpg_1 = mean(mpg_1)
    print('chevrolet", "ford", "honda 의 연비 평균은 - ' , m_mpg_1)
    print()

question03()

# 4. "audi"에서 생산한 자동차 중에 어떤 자동차 모델의 hwy(고속도로 연비)가
# 높은지 알아보려고 한다. "audi"에서 생산한 자동차 중 hwy가 1~5위에 해당하는
# 자동차의 데이터를 출력하세요.

def question04():
    print("4번 문제")
    mpg_1 = []
    for instance in mpgList:
        if instance.getManufacturer() == 'audi':
#            print(instance.getHwy())
            mpg_1.append([instance.getManufacturer() , instance.getModel() , instance.getDispl() , instance.getYear() , instance.getCty() , int(instance.getHwy()) ,instance.getFl()])
            
#    mpg_1 = sorted(mpg_1 , reverse = True)
    mpg_1.sort(key = lambda x: (x[0] , -x[5]))
    for i in mpg_1[0:5]:
        print(i)
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
        #print(i)
        a.append(i[0])
    b = list(set(a))
#    print(b) #중복제거 항목

    result = []
    for j in b:
        temp = 0
        cnt = 0
        for i in mpg_1:
            if i[0] == j:
                temp += i[1]
                cnt += 1
#                print(i[0] , temp , cnt)
        result.append( [j , round(temp/cnt , 1)] )
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