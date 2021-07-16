#https://www.acmicpc.net/problem/17413
#단어 뒤집기2

S , tmp = input() , ""
ck = False
for i in S:
    if i == ' ':
        if not ck:
            print(tmp[::-1] , end = " ")
            tmp = ""
            #현재보고있는 단어를 역순으로 하고 마지막 공백으로 해서 출력
            
        else:
            print(" " , end = "")
    elif i == '<':
        ck = True
        print(tmp[::-1] + '<' , end = "")
        tmp = ""
    elif i == '>':
        ck = False
        print('>' , end="")
        tmp = ""

    else: #알파벳과 숫자
        if ck:
            print(i, end = "")
        else:
            tmp += i

print(tmp[::-1])


