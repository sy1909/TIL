#https://www.acmicpc.net/problem/16768
# mooyo mooyo

# 같은 수들이 k 개 이상이면 터지는 게임 문제
# 플러드 필 기본 문제 2차원 배열에서 어떻게 이동시킬 수 있을지 묻는 문제
# 그룹을 찾고 반환하는 문제 

def new_array(N):
    return [[False for i in range(10)] for _ in range(N)]


N , K  = map(int, input().split())
M = [list(input()) for _ in range(N)] 
#입력을 리스트로 바꾼다(숫자로 받지 않고)
#입력이 공백없이 붙어서 들어오므로 처리해야한다.

ck = new_array(N)
ck2 = new_array(N)
dx , dy = [1,0, -1, 0] , [0, 1, 0 , -1]

def dfs(x,y):
    ck[x][y] = True
    ret = 1
    for i in range(4):
        xx, yy = x +dx[i] , y + dy[i]
        if xx <0 or xx >= N or yy<0 or yy>=10:
            continue
        if ck[xx][yy] or M[x][y] != M[xx][yy]:
            continue
        ret += dfs(xx , yy)
    return ret


def dfs2(x,y , val):
    ck2[x][y] = True
    M[x][y] = '0'
    for i in range(4):
        xx, yy = x +dx[i] , y + dy[i]
        if xx <0 or xx >= N or yy<0 or yy>=10:
            continue
        if ck2[xx][yy] or M[xx][yy] != val:
            continue
        dfs2(xx, yy, val)
   

def down():
    for i in range(10):
        tmp = []
        for j in range(N):
            if M[j][i] != '0':
                tmp.append(M[j][i])
        for j in range(N - len(tmp)):
            M[j][i] = '0'
        for j in range(N - len(tmp), N):
            M[j][i] = tmp[j - N+ len(tmp)]





while True:
    exist = False
    #바뀌는게 있을 때까지 계속 진행
    ck = new_array(N)
    ck2 = new_array(N)
    for i in range(N):
        for j in range(10):
            if M[i][j] == '0' or ck[i][j]:
                continue
            res = dfs(i,j) # 개수 세기
            if res >= K:
                dfs2(i,j , M[i][j]) # 지우기
                exist = True

    if not exist:
        break
    down() #지우고 내려오는 함수

for i in M:
    print(''.join(i))