import math
def solution(progresses, speeds):
    answer = []
    result = [ math.ceil((100-i)/j) for i , j in zip(progresses , speeds) ]
    print(result)
     
    for _ in result:
        cnt = 0
        tmp = result.pop(0)
        cnt +=1
        temp = list(result)
        for i in result:
            if i <= tmp:
                cnt +=1
                temp.pop(0)
            else:
                break
        answer.append(cnt)
        result = list(temp)
        if len(result) == 0:
            break
        
    return answer

'''
진도가 100% 되어야 서비스 반영
각 기능의 개발속도는 모두 다르다 뒤 기능이 앞 기능보다 먼저개발 가능
이때 뒤에있는 기능은 앞에있는 기능이 배포뙬 때 함께 배포
먼저 배포되어야 하는 순서대로 작업의 진도가 적힌 정수배열 progresses 
각 작업의 개발 속도가 적힌 정수 배열 speeds 
배포마다 몇개의 기능이 배포되는지를 return 
'''



def solution(priorities, location):
    answer = 0
    temp = [] ; index = [i for i in range(len(priorities))] ; index1 = []
    while True:
        j = priorities.pop(0)
        j2 = index.pop(0)
        if len(priorities) == 0:
            temp.append(j)
            index1.append(j2)
            break
        else:
            if j < max(priorities):
                priorities.append(j)
                index.append(j2)
            else:
                temp.append(j)
                index1.append(j2)
                
    print(index)
    for idx ,i in enumerate(index1):
        if i == location:
            answer = idx+1
    return answer


'''
인쇄 대기목록 가장 앞에 있는 문서를 대기목록에서 pop
나머지 중 pop한 것보다 중요도가 높은 문서가 있다면 pop 한 값이 append
중요도가 높은게 없다면 pop 그대로 인쇄
'''