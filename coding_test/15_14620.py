#https://www.acmicpc.net/problem/14620
# 꽃길

N = int(input())
G = [list(map(int, input().split())) for i in range(N)]  #이중리스트 생성

ans = 10000

dx , dy= [0,0, 0,1,-1] ,[0,1,-1,0,0] #방향벡터에 가만히 있는것까지 포함해서 5개

def ck(lst): #꽃이 a,b,c 있을때 비용
    ret = 0
    flow = [] #꽃이 들어가는 곳 리스트로 정의
    for flower in lst:
        x = flower // N
        y = flower % N
        if x == 0 or x == N -1 or y == 0 or y == N-1:
            return 10000   #이케이스는 안된다고 정의 한것 예외처리  꽃잎이 화단밖으로 넘어간 경우
        for w in range(5):
            flow.append( (x+dx[w] , y+dy[w]) )
            ret += G[x+dx[w]][y+dy[w]]
    if len(set(flow)) != 15:
        return 10000
    return ret

for i in range(N*N):
    for j in range(N*N):
        for k in range(N*N):
            ans = min(ans, ck([i,j,k]))

print(ans)