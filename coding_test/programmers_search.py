# 코딩테스트 > 완전탐색 > 모의고사
#answers = [1, 2, 3, 4, 5]
#answers = [1, 3, 2, 4, 2]
answers = [0, 0, 0, 0, 0]
'''
12345 / 12345
21 23 24 25 / 21232425
33 11 22 44 55 / 3311224455
'''
# p 안에서 반복문 돌릴떄 answer의 길이 의 나머지로 index를 설정하면 더 편하다.
def solution(answers):
    answer = []
    p = ['12345' ,'21232425' ,'3311224455']
    ans = ''.join(list(map(str , answers)))
    for j in range(len(p)):
        cnt =0 
        for i in range(len(answers)):
            if len(p[j]) < len(answers):
                p[j] = p[j] * (int(len(answers) / len(p[j])) +1 )
                if int(p[j][i])==int(answers[i]):
                    cnt+=1
            elif len(p[j]) >= len(answers):
                if str(p[j][i])==str(answers[i]):
                    cnt+=1
        answer.append(cnt)
    print(int(''.join(list(map(str , answers)))))
    if int(''.join(list(map(str , answers)))) ==0:
        return []
    an_f=[]
    for idx , i in enumerate(answer):
        if int(i) == int(max(answer)):
            an_f.append(idx+1)

    return an_f
#solution(answers)



# 코딩테스트 > 완전탐색 > 소수찾기
#numbers = "17"
numbers = "011"
from itertools import permutations
from itertools import combinations
# 에라토스테네스 체를 set을 이용해서 쓰면 코드가 훨씬 줄어든다.
# https://programmers.co.kr/learn/courses/30/lessons/42839/solution_groups?language=python3
# 참고해야할듯
# permutations 와 소수 알고리즘을 알고있는지 묻는 문제
def is_prime(prime_ , temp):
    
    if prime_ not in temp:
        temp.append(prime_)
        if prime_!=1 and prime_!=0:
            for i in range(2,prime_):
                if prime_ % i == 0:
                    return False
        else:
            return False
        return True
    else:
        return False
def solution42839(numbers):
    answer = 0 ; temp = []
    for i in range(1, len(numbers)+1):
#        print(list(permutations(numbers , i)))
        comb = list(permutations(numbers , i))
        for c in comb:
            prime_ = int(''.join(list(c)))
            #print(prime_)
            if is_prime(prime_ , temp):
                answer+=1

    return answer
#solution42839(numbers)


# 코딩테스트 > 완전탐색 > 카펫
brown = 10
yellow = 2
# brown = 8
# yellow = 1
# brown = 24
# yellow = 24
def solution42842(brown, yellow):
    answer = []

    carpet_count = brown + yellow
    for i in range(1, yellow+1):
        x = int(yellow/i)
        if x>=i and 2*x + 2*i + 4 == brown:
            answer = [x+2 , i+2]
   # print(answer)
    return answer
solution42842(brown, yellow)