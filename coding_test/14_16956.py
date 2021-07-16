#https://www.acmicpc.net/problem/16956
# 늑대와 양

R , C = map(int  , input().split())
M = [list(input()) for i in range(R)]

dx , dy = [0, 1, 0, -1] , [1, 0, -1, 0]

ck = False

for i in range(R):
    for j in range(C):
        if M[i][j] == 'W':
            for w in range(4): #4방위 체크
                ii ,  jj = i + dx[w], j + dy[w] # 범위를 넘어가는 애들을 예외처리
                if ii <0 or ii==R or jj < 0 or jj ==C:
                    continue #커트라인을 넘는 경우는 넘어간다.
                if M[ii][jj] == 'S':
                    ck = True

if ck : #true 란 것은 울프옆에 양이 있었다는 것
    print(0)
else: # 아닌경우 모든 경우를 울타리로 채우면 된다.
    print(1)
    for i in range(R):
        for j in range(C):
            if M[i][j] not in 'SW':
                M[i][j] = 'D'

for i in M:
    print(''.join(i)) 