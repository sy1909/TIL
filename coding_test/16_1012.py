#https://www.acmicpc.net/problem/1012
#유기농 배추
import sys
sys.setrecursionlimit(10000)
#런타임 에러가 날 경우 위를 추가

T = int(input())

B , ck  =[] , []

dx , dy = [1,0, -1, 0] , [0, 1, 0 , -1]

def dfs(x, y):
    global B , ck
    ck[x][y] = 1 
    for i in range(4):
        xx, yy = x+ dx[i] , y+dy[i]
        if B[xx][yy] == 0 or ck[xx][yy]:
            continue
        dfs(xx , yy)

def process():
    global B , ck
    M , N , K = map(int , input().split())
    #받는 인덱스를 1로 두는걸 추천 후에 dfs bfs 가장자리에 0으로 채워져 있다고 생각
    B = [[0 for i in range(M+2)]for _ in range(N+2)]
    ck = [[0 for i in range(M+2)]for _ in range(N+2)]
    for _ in range(K):
        X , Y = map(int ,input().split())
        B[Y+1][X+1] = 1
    ans = 0

    #dfs를 더 좋아한다. bfs는 스택을 호출해야 하므로
    for i in range(1, N+1):
        for j in range(1 , M+1):
            #전체를 탐색해야 한다.
            #탐색했는지 안했는지 체크변수 필요
            if B[i][j] == 0 or  ck[i][j]:
                continue
            dfs(i , j)
            ans += 1 #한번 dfs 를 돌았으니 1추가
    print(ans)

for _ in range(T):
    process()