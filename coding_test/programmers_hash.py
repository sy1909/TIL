# https://programmers.co.kr/learn/courses/30/lessons/42579
# 베스트앨범

'''
장르별 가장많이 재생 2개 베스트앨범 출시
노래 고유번호 구분
총 재생수가 높은 장르 수록
장르 내에서 많이 재생된 노래 수록
재생횟수가 같아다면 고유번호가 낮은 노래 먼저 수록
'''

genres = ["classic", "pop", "classic", "classic", "pop"]	
plays = [500, 600, 150, 800, 2500]
import pandas as pd
def solution(genres, plays):
    answer = []
    # 장르와 재생수 묶어서 dataframe으로
    table = [x for x in zip(genres , plays)]
    gen = pd.DataFrame(table)
    # 중복을제외한 장르만 가져와서 필터링하고 재생수의 합 그 값을 print
    #print(ge[ ge[0] == i for i in col].sum())
    ge = gen.groupby( 0 , as_index = False ).sum()
    #재생수 많은순서로 장르들 이름만 리스트로
    genres_index = ge.sort_values(1 , ascending = False)[0].to_list() 

    print(gen)
    for i in genres_index:
        temp = gen[gen[0] == i].sort_values(1,ascending=False)
        answer += temp.index.to_list()[0:2]
    
    print(answer)
    return answer

#solution(genres, plays)

#완주하지 못한 선수
# participant = ["leo", "kiki", "eden"]
# completion = ["eden", "kiki"]
# participant = ["marina", "josipa", "nikola", "vinko", "filipa"]
# completion = ["josipa", "filipa", "marina", "nikola"]
participant = ["mislav", "stanko", "mislav", "ana"]
completion = ["stanko", "ana", "mislav"]
# 답은 맞지만 효율성테스트에서 시간초과 코드
def solution_42576_timeout(participant, completion):
    answer = ''

    for i in participant:
        if participant.count(i) == completion.count(i):
            if i not in completion:
                answer = i
        elif participant.count(i) > completion.count(i):
            answer =i
    print(answer)
    return answer

import collections
def solution_42576(participant, completion):
    answer = ''

    print(collections.Counter(participant))
    print(collections.Counter(completion))
    answer = collections.Counter(participant) - collections.Counter(completion)
    print(answer)
    print(answer.keys())
    print(list(answer.keys())[0])
    answer = list(answer.keys())[0]    
    return answer
#solution_42576(participant, completion)

# 전화번호 목록
# zip 을 사용한 방법 sorted통해 앞뒤만 비교
# 문자열 정렬 (정수 아님 str 정렬)
# sorted(phone_book , key=len)
#phone_book = ["119", "97674223", "1195524421"]
phone_book = ["119","1149","1190", "97674223", "1195524421"]
# phone_book = ["123", "456", "789"]
# phone_book = ["12", "123", "1235", "567", "88"]
def solution_42577(phone_book):
    answer = True
    phone_book = sorted(phone_book)
    print(phone_book)
    # for i ,j in zip(phone_book , phone_book[1:]):
    #     print(i , j)
    for i in range(1, len(phone_book)):
        if phone_book[i].startswith(phone_book[i-1]) == True:
            print("False")
            return False
    print(answer)
    return answer
#solution_42577(phone_book)


clothes=[["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]]
# clothes=[["crow_mask", "face"], ["blue_sunglasses", "face"], ["smoky_makeup", "face"]]

# 위장
# dictionary 사용 , 경우의수 2로 시작 추가되면 1개 추가 , 최종 다 안쓰는 경우는 없으므로 -1
def solution_42578(clothes):
    answer = 0
    clothes_type = {}
    for _ , i in clothes:
        if i not in clothes_type:
            print(i)
            clothes_type[i] = 2
        else:
            print(i)
            clothes_type[i] +=1
    print(clothes_type)
    
    cnt = 1
    for i in clothes_type.values():
        cnt *= i
    print(cnt-1)
    return cnt -1
solution_42578(clothes)