
# 프로그래머스 위클리2
scores = [[100,90,98,88,65],[50,45,99,85,77],[47,88,95,80,67],[61,57,100,80,65],[24,90,94,75,65]]
import pandas as pd
def solution(scores):
    #print(scores , len(scores) , len(scores[0]))  
    scores = pd.DataFrame(scores)
    print(scores)
    answer = ''
    l1 = []
    # min max 구분하지 않아도되고 round 묶지 않아도 되고 
    for idx in scores:
        if scores[idx][idx] == max(scores[idx]) and scores[idx].count(max(scores[idx])) == 1 :
            l1.append( round( (scores[idx].sum()-scores[idx].max()) / (len(scores[idx])-1) , 1 )  )
        elif scores[idx][idx]  == min(scores[idx]) and scores[idx].count(min(scores[idx])) == 1:
            l1.append( round( (scores[idx].sum()-scores[idx].min()) / (len(scores[idx])-1) , 1 )  )
        else:
            l1.append( round( scores[idx].sum() / len(scores[idx]) ,1 )  )
    
    # 여기부터 list comp 쓰고 "".join 써서 1줄로 가능
    for i in l1:
        if i >= 90:
            answer+='A'
        elif i>=80 and i<90:
            answer+='B'
        elif i>=70 and i<80:
            answer+='C'
        elif i>=50 and i<70:
            answer+='D'
        elif i<50:
            answer+='F'
    print(answer)
    return answer
solution(scores)

#다른사람 풀이 아래
#solution = lambda scores: "".join(map(lambda m: "FDDCBAA"[max(int(sum(m) / len(m) / 10) - 4, 0)], map(lambda m: (m[0], *m[1]) if min(m[1]) <= m[0] <= max(m[1]) else m[1], ((s[i], s[:i] + s[i+1:]) for i, s in enumerate(zip(*scores))))))

# def solution(scores) :
    
#     avgs=[]

#     score=[ [i[j] for i in scores] for j in range(len(scores))]

#     for idx,i in enumerate(score) :

#         avg=sum(i) ; length=len(i)

#         if i[idx] == max(i) or i[idx] == min(i) :

#             if i.count(i[idx]) == 1 :

#                 avg-=i[idx] ; length-=1

#         avgs.append(avg/length)

#     return "".join([ avg>=90 and "A" or avg>=80 and "B" or avg>=70 and "C" or avg>=50 and "D" or "F" for avg in avgs ])
