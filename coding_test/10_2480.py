#https://www.acmicpc.net/problem/2480
#주사위 세개

#3번주사위를 던진다
#같은눈 3개 10000+(같은번호)*1000원
#같은눈 2개 1000+(같은번호)*100원
#모두 다른눈 (가장큰번호)*100원

lst = sorted(list(map(int, input().split())))
if len(set(lst)) == 1:
    print(10000 + lst[0] * 1000)
elif len(set(lst)) == 2:
    print(1000 + lst[1] * 100)
    #주사위가 3개밖에 없기때문에 중복이라면 무조건 가운데있는 수가 중복된 수이다.
else:
    print(lst[2]*100)