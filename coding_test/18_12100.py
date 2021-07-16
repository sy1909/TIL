#https://www.acmicpc.net/problem/12100
#2048 easy
from copy import deepcopy
N = int(input())

Board = [list(map(int, input().split()) for i in range(N))]
#1024가지 4의 5승 총5번 움직일 수 있으므로 탐색
# 맵을 돌리는게 효과적이다 상하좌우 로직을 잘 필요없이 하나만 짜고

def rotate90(B ,  N):
    NB = deepcopy(B)
    #newBoard
    for i in range(N):
        for j in range(N):
            NB[j][N-i-1] = B[i][j]
    return NB

def convert(lst , N):
    #한 줄을 리스트를 왼쪽으로 슬라이스했을 때 생기는 결과물
    new_list = [i for i in lst if i]
    for i in range(1, len(new_list)):
        if new_list[i-1] == new_list[i]:
            new_list[i-1] += 2
            new_list[i] = 0
    new_list = [i for i in new_list if i]
    return new_list + [0]*(N-len(new_list))


def dfs(N , B , count):
    ret = max([max(i) for i in B])
    if count == 0:
        return ret
    for _ in range(4):
        X = [convert(i , N) for i in B]
        if X != B:
            ret = max(ret, dfs(N, X, count-1))
        B = rotate90(B , N) #한방향으로 완료했으니 맵을 돌린다.
    return ret

print(dfs( N , Board , 5))


