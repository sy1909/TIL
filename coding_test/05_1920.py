#https://www.acmicpc.net/problem/1920
#수찾기

N,A = int(input()) , {i: 1 for i in map(int, input().split())}
#값이 있다면 1로 매칭하는 딕셔너리 표현
print(A)
M = input()
for i in list(map(int,input().split())):
#    print(A[i]) #error 파이썬의 딕셔너리는 없는값을 출력해주지 않는다
    print(A.get(i,0)) #아직 key가 등록이 안되는 애들은 0으로 디폴트를 설정한다.
