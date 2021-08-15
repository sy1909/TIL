array = [1, 5, 2, 6, 3, 7, 4]
commands = [[2, 5, 3], [4, 4, 1], [1, 7, 3]]

# 정렬 > K번쨰수
def solution(array, commands):
    answer = []
    for i in commands:
        ar = sorted(array[i[0]-1:i[1]])
        answer.append(ar[i[2]-1])
    return answer
#solution(array, commands)


# 장랼 ? 기징 큰 수
#numbers = [6, 10, 2]
# ,key=lambda x:x*5 -> 33333 3030303030 3434343434 55555 99999 로 비교 기억
numbers = [3, 30, 34, 5, 9]

def solution1(numbers):
    temp = list(map(str , numbers) )
    temp = sorted(temp,key=lambda x:x*5)[::-1]
    print(temp)
    print("".join(temp))
    # int 로 변환해서 00000 같은경우 0으로 만들고 str로 제출
    return str(int("".join(temp)))
#solution1(numbers)


# 정렬 > H-Index
# enumerate  /  map(min , )  /  max
citations = [3, 0, 6, 1, 5]

def solution2(citations):
    answer = 0
    c = sorted(citations)[::-1]
    c1 = enumerate(c , start=1)
    c2 = map(min , c1)
    c3 = max(c2)
    answer = c3

    return answer
