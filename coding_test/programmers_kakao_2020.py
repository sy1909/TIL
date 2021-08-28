#코딩테스트 연습 > 2020 KAKAO > 문자열 압축
def solution(s):
    answer = 0
    result = [len(s)]
    print(s)
    
    for size in range(1, len(s)):
        comp = [] 
        # size 별로 쪼개기
        splited = [ s[i:i+size] for i in range(0, len(s), size) ]
        #print(len(splited))
        count = 1
        for i in range(1,len(splited)):
            #print(splited[i-1] , splited[i])
            if splited[i-1] == splited[i]: # 이전문자와 동일하다면
                count += 1
            else: #이전문자와 다르다면
                if count>1:
                    comp.append(str(count))
                    comp.append(splited[i-1])
                else:
                    comp.append(splited[i-1])
                count = 1
        if count> 1:
            comp.append(str(count))
            comp.append(splited[-1])
        else:
            comp.append(splited[-1])

        result.append(len("".join(comp)))
        
    print(min(result))
    answer = min(result)
    return answer

'''
문자열 압축
비손실 압축방법 공부
문자열에서 같은 값이 연속해서 나타나는 것을 그 문자의 개수가 반복되는 값으로 표현하여 더 짧은 문자열로 줄이기

'''

#코딩테스트 연습 > 2020 KAKAO > 괄호 변환
# 입력값으로 들어온 string 올바를 괄호쌍으로 묶여있다면 빈리스트가 리턴될거고 아니라면 값이 있을것
def is_correct(string):
    stack = []
    for s in string:
        if s == '(':
            stack.append(s)
        elif stack: #stack이 비어있지 않고 s가 ')' 라면 stack에 들어있는 '(' 를 pop한다.
            stack.pop()
    # print(stack) 
    # 빈리스트 라면 False가 들어가고 올바른 쌍이었다는 얘기기때문에 not stack True로 반환
    # print(not stack)
    return not stack

def uv(string):
    strq = list(string)
    u = "" ; v ="" ; left ,right = 0,0
    while strq: # strq 에 있는 리스트가 빌때까지
        u += strq.pop(0) # 왼쪽부터 pop 해서 값 추출하고
        if u[-1] == '(':
            left += 1
        else:
            right += 1
        if left == right: #짝이맞다면 종료
            break
    v = ''.join(strq) #남아있는 strq 가 v가 된다.
    print(u ,v)
    return u,v

def recursive(string):
    if string == '': # 1번
        return ''
    u, v = uv(string) # 2번
    if is_correct(u):  # 3번
        return u + recursive(v)
    else:  # 4번
        return '(' + recursive(v) + ')' + reverse(u[1:-1])

def reverse(u):
     # 뒤집어진 u를 뒤집기 위한 함수
    return ''.join([')' if s == '(' else '(' for s in u])

def solution(p):
    if is_correct(p):
        return p
    else:
        return recursive(p)

'''
다른 개발자가 작성한 소스 코드 분석 문제점 수정
괄호가 개수는 맞지만 짝이 맞지 않다
모든 괄호를 뽑아서 올바른 순서대로 배치된 괄호 문자열을 알려주는 프로그램
'(' ')' 로만 이루어지고 개수가 같다면 균형잡힌 괄호문자열
짝까지 맞으면 올바른 괄호 문자열

'''