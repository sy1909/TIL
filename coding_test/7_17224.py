#https://www.acmicpc.net/problem/17224
#apc는 왜 서브태스크 대회가 되었을까

'''
난이도 설정
쉬운버전의 난이도 순으로 배치
L 만큼의 역량을 가지고 있어 작거나 같은 문제의
시간이 부족해 K 보다 많은 문제는 해결 못함
쉬운버전 100점
어려운버전 +40점 140점
'''
#문제개수 역량L 해결최대개수
N , L , K = map(int , input().split())
score , sol = 0 , 0
for i in range(N):
    sub1 , sub2 = map(int , input().split())
    if sub2 <= L:
        score += 140
        sol += 1
    elif sub1 <= L:
        score += 100
        sol += 1
    if K == L:
        break

print(score)