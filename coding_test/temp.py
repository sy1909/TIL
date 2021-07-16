import sys
sys.setrecursionlimit(10000)
#런타임 에러가 날 경우 위를 추가

T = int(input())

dx , dy = [0, -1, 0 ,1] , [1, 0 , -1, 0]
ans = 0
B , ck =[] , []

def dfs(x, y):
    global B, ck
    ck[x][y] = 1
    for i in range(4):
        xx , yy = dx[i] + x , dy[i] + y
        if xx <0 or xx >= N or yy<0 or yy >=M or B[xx][yy] == 0 or ck[xx][yy]:
            continue
        dfs(xx,yy)


for i in range(T):
    ans = 0
    M , N , K = map(int, input().split())
    B = [[0 for _ in range(M) ] for _ in range(N)]
    ck = [[0 for _ in range(M) ] for _ in range(N)]    
    for _ in range(K):
        X , Y = map(int, input().split())
        B[Y][X] = 1

    for j in range(N):
        for k in range(M):
            if B[j][k] == 0 or ck[j][k]:
                continue
            dfs(j,k)
            ans+=1


    print(ans)