def cntFunc():
    cnt =0
    with open("C:\\Users\\ksy\\TIL\\python\\cnt_words.txt" , 'r' , encoding='utf-8') as file:
        for line in file:
            if len(line) <= 10:
                cnt += 1
    print('10자 이하인 단어의 개수 : ' , cnt)

#cntFunc()



def includeFunc():
    with open("C:\\Users\\ksy\\TIL\\python\\special_words.txt" , 'r' , encoding='utf-8') as file:
        lines = file.read()
        print(lines)

#includeFunc()

def zip():
    with open("C:\\Users\\ksy\\TIL\\python\\zipcode.txt" , 'r' , encoding='utf-8') as file:
        lines = file.readlines() #.split('\t')
        #print(lines)
    c = input()
    for line in lines:
        l2 = line.split('\t')
        if l2[3].startswith(c):
            for i in l2:
                print(i , end = ' ')
    



zip()
