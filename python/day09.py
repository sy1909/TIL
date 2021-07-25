import pandas as pd

#csv excel json
# restful service - ajax - 비동기통신
# json - {key : {key : value} , key : []}

# def load_csv(filePath):
#     raw_data = pd.read_csv(filePath , encoding = 'utf-8')
#     return raw_data

def load_file(filePath):

    if filePath.split('.')[-1] == 'csv':
        #raw_data = pd.read_csv(filePath , encoding = 'utf-8')
        #spam_data 관련 read ms949파일 이고 헤더가 없기에 none
        raw_data = pd.read_csv(filePath , encoding = 'ms949' , header=None)

    elif filePath.split('.')[-1] == 'xlsx' :
        raw_data = pd.ExcelFile(filePath , engine='openpyxl')
    else:
        with open(filePath , 'r' , encoding='utf-8') as file:
            raw_data = file.readlines()

    return raw_data


def bim_caller(filePath):
    #data = load_csv(filePath)
    data = load_file(filePath)
#    print(type(data))
#    print(type(data['height']) , data.height)

    # int , object(대부분 문자열)
    print(data.info())

#   label 컬럼을 활용하여 빈도수를 출력한 구문 작성해 본다면?
#   딕셔너리 활용 해당키의 빈도수를 구하는 반복문 get 함수
    labelFreq = {}
    for key in data.label:
        labelFreq[key] = labelFreq.get(key , 0) + 1

    print(labelFreq)    

#bim_caller('C:\\Users\\ksy\\TIL\\python\\service_bmi.csv')    

def kospi_caller(filePath):
    data = load_file(filePath)
    print(type(data))
    #dataframe 으로 변환
    data = data.parse('sam_kospi')
    print(type(data))
    print(data.info())

#kospi_caller('C:\\Users\\ksy\\TIL\\python\\sam_kospi.xlsx')


#json
#네트워크 상에서 표준으로 사용되는 파일 형식
# json -> python(dict , list) : decoding
# json <- python(dict , list) : encoding

import json as j

tmpdict = {'id' : 'ksy' , 'pwd' : 'ksy'}
print(type(tmpdict))

#dict -> json
jsondict = j.dumps(tmpdict)
print(type(jsondict))

#json -> dict
pyobj = j.loads(jsondict)
print(type(pyobj))

def json_caller(filePath):
    lines = load_file(filePath)
    print(type(lines) , lines)
    print(type(j.loads(lines[0])))

    # j.loads 는 json 형식을 dict 로 형변환
    # str로된 내용을 dict 로 형변환한 후 lines 에 딕셔너리들을 리스트로 담기
    lines = [j.loads(i) for i in lines]
    print(type(lines[3]) , lines[3])

    dataDF = pd.DataFrame(lines)
#    print(type(dataDF) , dataDF)
#   위까지 저 위에 load file else 부분에 갖다 놓고 raw_data 리턴시키면 될듯

    print(dataDF.head())

#json_caller('C:\\Users\\ksy\\TIL\\python\\usagov_bitly.txt')
#정규표현식 사용

import re

# 텍스트 전처리 -> 특수문자 숫자 공백 영문제거 -> 한글단어만
def clean_txt(msg):
    # 문장부호 제거
    print(type(msg))
    msg_re = re.sub('[,.?!:;]' , ' ' , str(msg))
    print()
    # 특수문자 제거
    msg_re = re.sub('[@#$%^&]|[0-9]' , ' ' , str(msg_re))
    # 영문자를 소문자로 변경
    msg_re = re.sub('[[@#$%^&]|[0-9]]' , ' ' , msg_re.lower())
    #공백제거
#    msg_re = re.sub(' ' , '' , msg_re)
    msg_re = ' '.join(msg_re.split())
    return msg_re



def spam_caller(filePath):
    data = load_file(filePath)
    # print('spam_caller' , type(data))
    print(data.head())
    # data.info()

    target = data[0]
    msg = data[1]    
    print(target)
    print(msg)

    clean_msg = clean_txt(msg)
    print(clean_msg)

spam_caller('C:\\Users\\ksy\\TIL\\python\\spam_data.csv')



