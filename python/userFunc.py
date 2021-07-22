
# def 함수이름(option) :
#   statement
#   return value

def printGreeting() :
    print('이제 함수를 살펴보고 있습니다~~~')

def printCoin() :
    print('bitcoin~~')

def test() :
    pass

def mySum(x , y, z=10) :
    return x + y + z

def returnMsg(name) :
    msg = 'Hello , ' + str(name)
    return msg

def countSum(start , end) :
    oddSum = evenSum = 0
    for x in range(start , end+1) :
        if x%2 == 0 :
            evenSum += x
        else :
            oddSum += x
    return (oddSum , evenSum)

# 입력받은 문자열에 인터넷주소를 반환하는 함수를 정의
# naver -> www.naver.com
# def makeUrl(string) :
#     return "www."+string+".com"

def makeUrl(url_list) :
    returnList = []
    for url in url_list :
        returnList.append("www."+url+".com")
    return returnList

def print_5xn(line) :
    chk_num = int(len(line) / 5)
    for x in range(chk_num+1) :
        print( line[x * 5 : x * 5 + 5] )

def pickupEven(numList) :
    result = []
    for num in numList :
        if num % 2 == 0 :
            result.append(num)
    return result


# *args , **kwargs
# *args -> tuple
# **kwargs -> dict

def argsTuple(*args) :
    for idx , value in enumerate(args) :
        print('result idx {} , value {}'.format(idx , value))
    print("*" * 50)

def userStatistic(func , *data) :
    from statistics import mean , stdev
    if func == 'SUM' :
        print(sum(data))
    if func == 'AVG' :
        print(mean(data))
    if func == 'STD' :
        print(stdev(data))

def kwargsDict(**kwargs) :
    for key , value in kwargs.items() :
        print('key {} , value {}'.format(key , value ))
    print('*' * 50)

def personInfo(w , h , **other) :
    print(w)
    print(h)
    print(other , type(other))

def mixtype(arg1, arg2, *arg3 , **arg4 )  :
    print(arg1)
    print(arg2)
    print(arg3, type(arg3))
    print(arg4, type(arg4))


def leay_year_loop(strYear : int , endYear : int) -> list :
    yearList = []
    for year in range(strYear , endYear+1) :
        if( (year%4 == 0 and year%100 != 0) or (year%400 == 0)) :
            yearList.append(year)
    return yearList


