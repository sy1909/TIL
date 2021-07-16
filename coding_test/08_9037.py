#https://www.acmicpc.net/problem/9037
#the candy war

#아이들이 사탕을 마구잡이로 집어가 없는 아이도 있다
#절반 넘기기 홀수 +1 로 짝수

def check(N , candy):
    for i in range(N):
        if candy[i] %2 == 1:
            candy[i] += 1
    return len(set(candy)) == 1

T = int(input())
#테스트 케이스의 개수
for i in range(T):
    N = int(input())
    #아이들의 인원
    candy = list(map(int , input().split()))
    cnt = 0
    while not check(N , candy):
        cnt+=1
        tmp_lst = [0 for i in range(N)]
        for idx in range(N):
            if candy[idx]%2:
                candy[idx] += 1
            candy[idx] //= 2
            tmp_lst[(idx+1)%N] = candy[idx]

        for idx in range(N):
            candy[idx] += tmp_lst[idx]
    print(cnt)
