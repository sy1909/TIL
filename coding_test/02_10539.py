#https://www.acmicpc.net/problem/10539

N , M = int(input()) , list(map(int , input().split()))
# N은 수열의 길이 , M은 수열 리스트
temp = [M[0]]
for i in range(1 ,N):
    temp.append(M[i]*(i+1) - sum(temp))

for i in temp:
    print(i , end = ' ')

#print 의 기본 개행문자가 들어가있는데 공백으로 바꾸고 일 자로 출력