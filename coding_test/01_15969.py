#https://www.acmicpc.net/problem/15969


N , lst = input() , list(map(int, input().split()))
print(max(lst) - min(lst))


# input().split() 는 문자열 리스트를 처리할 수 있다. 띄워쓰기 공백기준 
# map 은 정해진 형식으로 모든 요소를 변환 int로 변환시킨다는 의미
# input() 은 있는 그대로 받아들이기
# list는 변환한 map을 list방식으로 변환