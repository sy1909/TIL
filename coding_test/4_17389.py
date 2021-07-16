#https://www.acmicpc.net/problem/17389
#보너스 점수

N , S = int(input()) , input()
#print(M)
score = 0
Bonus = 0

for i in range(N):
    if S[i] == 'O':
        score = score + Bonus + i +1
        Bonus += 1
    else:
        Bonus = 0

#위처럼 index가 같이 필요한 경우 enumerate 로 사용할 수 있다.
# for idx , ox in enumerate(S) 이런식으로 하여 idx가 index ox가 값

print(score)

