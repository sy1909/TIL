
'''
텍스트 파일 입출력
open(file = xxxx , mode = 'r|w|a')
with open ~~~ as file :

'''

def fileFunc(fileName , mode) :
    file = None
    try :
        if mode == 'r' :
            file = open(fileName , mode , encoding='utf-8')
            line = file.read()
            print('file read - ' , type(line))
        elif mode == 'w' :
            file = open(fileName, mode, encoding='utf-8')
            file.write('Hello ~  , Seop ')
        else :
            file = open(fileName, mode, encoding='utf-8')
            file.write('\nSeop append')
    except Exception as e :
        print(str(e))
    finally :
        if file != None :
            file.close()

def withFunc(fileName , mode) :
    with open(fileName , mode , encoding='utf-8') as file :
        print( file.read() )

def withMultiLineWriteFunc(fileName) :
    with open(fileName, 'w' , encoding='utf-8') as file:
        for text in range(3) :
            inputMsg = input('문자열을 입력하세요 : ')
            file.write(inputMsg+'\n')

def withListWriteFunc(fileName , mode , lines : list) :
    with open(fileName, mode , encoding='utf-8') as file:
        # file.writelines(lines)
        for text in lines :
            file.write(text)

def withListReadFunc(fileName) :
    with open(fileName, 'r' , encoding='utf-8') as file:
        line = None
        # while line != '' :
        #     line = file.readline()
        #     print(line.strip('\n'))
        for line in file :
            print(line.strip('\n'))

# cnt_words.txt 파일로부터 줄단위로 읽어서 단어의 길이가 10 이하인 단어들만 카운팅 해 본다면?
def cntFunc() :
    cnt = 0
    with open('./data/cnt_words.txt' , 'r', encoding='utf-8') as file:
        for line in file :
            if len(line.strip('\n')) <= 10 :
                cnt += 1

    print('10자 이하인 단어의 개수 : {}'.format(cnt))

# special_words.txt 파일로부터 문자 'c' 포함된 단어를 각 줄에 출력한다면?
# 단어를 출력할  때 등장한 순서대로 출력
def includeFunc() :
    with open('./data/special_words.txt' , 'r', encoding='utf-8') as file:
        lines = file.readline().split()
        # print(type(lines) , lines)
        lines = [i.strip(',.') for i in lines]
        for word in lines :
            if 'c' in word :
                print(word)


# zipcode.txt
# input() 함수를 이용해서 동 이름을 입력받아
# 예) 개포
# 해당하는 동의 주소를 출력하는 함수를 정의한다
# hint - \t
# startswith() 함수를
# 예외처리

def searchAddr() :
    dong = input('동을 입력하세요 : ')
    try :
        with open('./data/zipcode.txt', 'r', encoding='utf-8') as file:
            line = file.readline()
            while line :
                addrList = line.split('\t')
                if addrList[3].startswith(dong) :
                    print(addrList)
                line = file.readline()
    except Exception as e :
        print(str(e))



# 회문(palindrome)
# madam , nurses run , sos , rotator , level
# str = jslim9413
# idx = len(str) // 2
# 회문을 검사하는 함수를 만들어 본다면?
# 0 1 2 3 4 5 6 7 8 9 10
# m   u  l  t  i c a m p   u  s
# 11 10 9 8 7 6 5 4 3 2 -1

# if word == word[::-1] :
#     isFlag = True
# if list(word) == list(reversed(word)) :
#     isFlag = True

def isPalindrome() :
    word = input('회문 검사를 위한 단어 입력 : ')
    isFlag = True
    for i in range(len(word) // 2) :
        if word[i] != word[-1-i] :
            isFlag = False
            break
    return isFlag

# 회문인 단어만 출력
# hint - \n (제외시키고)
# hint - 단어사이의 줄 바꿈이 두번 일어나면 안됨
def palindromeFunc() :
    with open('./data/palindrome_words.txt', 'r', encoding='utf-8') as file:
        for line in file :
            # print(type(line) , line)
            line = line.strip('\n')
            if line == line[::-1] :
                print(line) 















