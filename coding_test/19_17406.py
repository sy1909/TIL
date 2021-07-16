#https://www.acmicpc.net/problem/17406
# 배열돌리기 4

#탐색 문제이면서 탐색조건을 어떤식으로 설정하는지
from copy import deepcopy

N , M , K = map(int, input().split())

A = [list(map(int , input().split())) for _ in range(N)]
Q = [tuple(map(int, input().split())) for _ in range(K)]
dx , dy = [1,0,-1,0] , [0,-1,0,1]
ans = 10000


def value(arr):
    return min([ sum(i) for i in arr])

def convert(arr , qry):
    (r, c ,s) = qry
    r, c = r-1 , c-1
    new_arr = deepcopy(arr)
    for i in range(1 , s+1):
        rr , cc = r-i , c+i
        for w in range(4):#한번당 방향을 한번씩 바꿀건데
            for d in range(i*2):#중심에서 2배씩 멀어질것이다.
                rrr , ccc = rr+dx[w] , cc + dy[w]
                #다음으로 움직여야할 칸
                new_arr[rrr][ccc] = arr[rr][cc]
                rr , cc = rrr, ccc
    return new_arr




def dfs(arr ,qry):
    global ans
    if sum(qry) == K:
        ans = min(ans , value(arr))
        return

    for i in range(K):
        if qry[i]:#처리했다면 컨티뉴
            continue
        new_arr = convert(arr, Q[i])
        # 쿼리를 처리하고 넘긴 값을 만들어주는 함수 쿼리로 배열을 변환
        qry[i] = 1
        dfs(new_arr , qry)
        qry[i] = 0

dfs(A , [0 for i in range(K)])
print(ans)


