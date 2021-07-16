#https://www.acmicpc.net/problem/2484
#주사위 네개

N = int(input())
result = [0 for i in range(N)]
for i in range(N):
    lst = sorted(list(map(int , input().split())))

    if len(set(lst)) == 1:
        result[i] = 50000 + lst[0] *5000
    elif len(set(lst)) == 2:
        if lst[1] == lst[2]:
            result[i] = 10000 + lst[1] *1000
        else:
            result[i] =  2000+lst[1]*500 +lst[2]*500
    elif len(set(lst)) == 3:
        if lst[0] == lst[1]:
            result[i] = 1000 +lst[0]*100
        else:
            result[i] = 1000 +lst[2]*100

    else:
        result[i] = lst[-1]*100

print(max(result))
