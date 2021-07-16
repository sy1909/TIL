'''
#boj1920
#사전형(딕셔너리) 사용법
N,A = int(input()) , {i: 1 for i in map(int, input().split())}
#값이 있다면 1로 매칭하는 딕셔너리 표현
M = input()
for i in list(map(int,input().split())):
#    print(A[i]) #error 파이썬의 딕셔너리는 없는값을 출력해주지 않는다
    print(A.get(i,0)) #아직 key가 등록이 안되는 애들은 0으로 디폴트를 설정한다.
'''
'''
#boj16165
#딕셔너리를 어떻게 활용하는지 리스트와 연결도 되고 확장도 가능한 점 활용
N , M = map(int, input().split())
#dictionary list 둘다 사용
team_mem , mem_team = {} , {}

for i in range(N):
    team_name , mem_num = input() , int(input())
    team_mem[team_name] = []
    for j in range(mem_num):
        name = input()
        team_mem[team_name].append(name)
        mem_team[name] = team_name

for i in range(M):

    name , q = input() , int(input())
    if q:
        print(mem_team[name])
    else:
        for mem in sorted(team_mem[name]):
            print(mem)
'''
'''
#boj 17224 
#
N, L , K = map(int, input().split())

easy , hard = 0,0

for i in range(N):
    sub1 , sub2 = map(int , input().split())
    if sub2 <= L:
        hard += 1
    elif sub1 <= L :
        easy += 1

#hard 문제
ans = min(hard , K )* 140

#easy 문제
if hard < K :
    ans += min(K-hard , easy)*100

print(ans)
'''

T = int(input())
B , ck = [] , []

dx  , dy = [0,1,0,-1] , [1, 0 , -1 , 0]

def dfs(x , y ):
    global B , ck
    ck[x][y] = 1
    for i in range(4):
        xx , yy = x + dx[i] , y + dy[i]
        if B[xx][yy] == 0 or ck[xx][yy]:
            continue
        dfs(xx , yy)



for _ in range(T):
    M, N, K = map(int , input().split())
    B = [[0 for i in range(M+2)] for i in range(N+2)]
    ck =  [[0 for i in range(M+2)] for i in range(N+2)]
    for i in range(K):
        X , Y = map(int , input().split())
        B[Y+1][X+1] = 1
    #print(B)

    ans = 0
    for i in range(1, N+1):
        for j in range(1, M+1):
            if B[i][j]==0 or ck[i][j]:
                continue
            dfs(i, j)
            ans +=1

    print(ans)



