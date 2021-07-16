#https://www.acmicpc.net/problem/17269
#이름궁합 테스트

N , M = map(int , input().split())
#string으로 받은 내용을 int로 변환
A , B = input().split()
#string으로 그대로 사용하기 때문에 그대로 사용

alp = [3,2,1,2,4,3,1,3,1,1,3,1,3,2,1,2,2,2,1,2,1,1,1,2,2,1]

AB = ''
#이름두개를 이어붙여 합칠 string 하나 생성
min_len = min(N, M)
#길이가 어느 이름이 더 짧은지 확인
for i in range(min_len):
    AB += A[i] + B[i]
#짧은 길이만큼 반복하며 string 합치기
AB += A[min_len:] + B[min_len:]
#짧은 길이 이후의 길이를 한번에 합치기
lst = [alp[ord(i) - ord('A')] for i in AB]
#ord 문자의 유니코드 값을 돌려주고 A의 유니코드 값을 뺌으로써 
#alp의 index에 A가 0으로 동작한다.
for i in range(N+M-2):
    for j in range(N+M-1-i):
        lst[j] += lst[j+1]
# 연결된 숫자의 합이므로 2개의 길이가 사용되지 않아 -2를 하고
# 그 합을 하는 반복문 까지
print("{}%".format(lst[0]% 10*10 +lst[1]%10))
#리스트로 나오는 두 숫자를 %로 나타내는 


