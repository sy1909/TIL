# from urllib.request import urlopen
# from urllib.parse import urlencode, unquote, quote_plus
# import urllib
# import requests
# import json
# import pandas as pd
# from datetime import datetime,timedelta
# import xmltodict # 결과가 xml 형식으로 반환된다. 이것을 dict 로 바꿔주는 라이브러리다

# # 어제 날짜와 오늘날짜를 구하기 위해서  datetime과 timedelta를 사용
# yester = datetime.today() - timedelta(1)
# yseter =  yester.strftime("%Y%m%d") #어제날짜
# now_today = datetime.today().strftime("%Y%m%d") # 오늘날짜


# my_api_key = 'uyztEOQTOe4tPKNOexzkgyVD%2BY7Jx379QbYn%2FXkVnH9hDvM9V4UA1AAu%2BnvAys%2FKE20iY%2BYPvcqzA2hkCNBNsA%3D%3D'

# #일반 인증키
# #(Encoding)   
# #uyztEOQTOe4tPKNOexzkgyVD%2BY7Jx379QbYn%2FXkVnH9hDvM9V4UA1AAu%2BnvAys%2FKE20iY%2BYPvcqzA2hkCNBNsA%3D%3D
# #일반 인증키
# #(Decoding)   
# #uyztEOQTOe4tPKNOexzkgyVD+Y7Jx379QbYn/XkVnH9hDvM9V4UA1AAu+nvAys/KE20iY+YPvcqzA2hkCNBNsA==


# # 서비스 url 주소
# url = 'http://openapi.data.go.kr/openapi/service/rest/Covid19/getCovid19InfStateJson'

# # 서비스에 필요한 파라미터 모음
# queryParams = '?' + \
# 'ServiceKey=' + '{}'.format(my_api_key) + \
# '&pageNo='+ '1' + \
# '&numOfRows='+ '999' + \
# '&startCreateDt={}&endCreateDt={}'.format(yseter,now_today)

# #서비스url에 필요한 파라미터들을 붙여서 응답결과를 얻음.
# result = requests.get(url + queryParams)

# # 응답결과 파싱하기. ( 사용자가 원하는 형태로 변경)
# # 응답 key 값이 영문화 되어 식별이 어려워 openAPI 문서를 참고하여
# # replayce 를 통해 결과를 한글화 했다.

# result = result.content 
# jsonString = json.dumps(xmltodict.parse(result), indent = 4)
# jsonString = jsonString.replace('resultCode', '결과코드').replace('resultMsg', '결과메세지').replace('numOfRows', '한 페이지 결과 수').replace('pageNo', '페이지 수').replace('totalCount', '전체 결과 수').replace('seq', '게시글번호(감염현황 고유값)').replace('stateDt', '기준일').replace('stateTime', '기준시간').replace('decideCnt', '확진자 수').replace('clearCnt', '격리해제 수').replace('examCnt', '검사진행 수').replace('deathCnt', '사망자 수').replace('careCnt', '치료중 환자 수').replace('resutlNegCnt', '결과 음성 수').replace('accExamCnt', '누적 검사 수').replace('accExamCompCnt', '누적 검사 완료 수').replace('accDefRate', '누적 환진률').replace('createDt', '등록일시분초').replace('updateDt', '수정일시분초')

# js = json.loads(jsonString)
# # 파싱한 전체 결과 보기.
# print(js)
# js_check_count = js["response"]['body']['items']['item'][0]['검사진행 수']
# js = js["response"]['body']['items']['item']
# pdata = pd.DataFrame(js)

# # 원하는 정보만 파싱한 결과
# # 누적 검사자 수와 누적 확진자수를 제공하기 때문에
# # 전일과의 차이로 일일 확진자, 검사자 수를 구했다.

# print('전일 검사 확진자수 : ',int(pdata.loc[0][7]) - int(pdata.loc[1][7]))
# print('전일 코로나 검사 수',int(pdata.loc[0][8]))


#사망자수, 확진자수, 검사진행수, 누적검사수, 날짜




# import requests
# import pandas as pd

# url='http://openapi.seoul.go.kr:8088/API KEY/json/Corona19Status/1/2'
# re=requests.get(url)
# rjson=re.json()
# total_num=rjson['Corona19Status']['list_total_count']
 

# 총 확진자 수를 확인했으면 바로 코로나 확진자 개별 데이터를 보도록 하겠다. 총 5,827개의 데이터가 있었기 때문에 반복문으로 데이터를 가져오도록 하겠다. 굉장히 쉽다. 별 설명이 필요가 없다.

 

# ids=[]
# corona_dates=[]
# address=[]
# corona_contact_detail=[]
# status=[]

# for i in range(1,int(round(total_num/1000,0))+1):
#     end=i*1000
#     start=end-1000 +1
    
#     if end >total_num:
#         end = total_num
    
#     url=f'http://openapi.seoul.go.kr:8088/API KEY/json/Corona19Status/{start}/{end}'
#     re=requests.get(url)
#     rjson=re.json()
    
#     for v in rjson['Corona19Status']['row']:
#         ids.append(v['CORONA19_ID'])
#         corona_dates.append(v['CORONA19_DATE'])
#         address.append(v['CORONA19_AREA'])
#         corona_contact_detail.append(v['CORONA19_CONTACT_HISTORY'])
#         status.append(v['CORONA19_LEAVE_STATUS'])
        
# df=pd.DataFrame([ids,corona_dates,address,corona_contact_detail,status]).T
# df.columns=['코로나 순번','확진 날짜','지역','접촉','현재 상태']















from urllib.request import urlopen
from urllib.parse import urlencode, unquote, quote_plus
import urllib
import requests
import json
import pandas as pd
from datetime import datetime,timedelta

## api에 데이터가 3/2일 정도부터 정상? 이여서 3/2일부터
## 조회 당일까지 데이터 받기
yseter = "20200302"
#오늘 날짜
now_today = datetime.today() - timedelta(0)
now_today = now_today.strftime("%Y%m%d") 
print("오늘과 어제 날짜 확인")
print(yseter)
print(now_today)
my_api_key = 'uyztEOQTOe4tPKNOexzkgyVD%2BY7Jx379QbYn%2FXkVnH9hDvM9V4UA1AAu%2BnvAys%2FKE20iY%2BYPvcqzA2hkCNBNsA%3D%3D'

url = 'http://openapi.data.go.kr/openapi/service/rest/Covid19/getCovid19InfStateJson'

queryParams = '?' + \
'ServiceKey=' + '{}'.format(my_api_key) + \
'&pageNo='+ '1' + \
'&numOfRows='+ '999' + \
'&startCreateDt={}&endCreateDt={}'.format(yseter,now_today)



# 받은 데이터 파싱하기.
# api 문서를 참조하여 영문명의 데이터를
# replace() 함수를 사용하여 한글명으로 바꿨다.

import xmltodict

result = requests.get(url + queryParams)
print(result)
result = result.content 
jsonString = json.dumps(xmltodict.parse(result), indent = 4)
jsonString = jsonString.replace('resultCode', '결과코드').replace('resultMsg', '결과메세지').replace('numOfRows', '한 페이지 결과 수').replace('pageNo', '페이지 수').replace('totalCount', '전체 결과 수').replace('seq', '게시글번호(감염현황 고유값)').replace('stateDt', '기준일').replace('stateTime', '기준시간').replace('decideCnt', '누적 확진자 수').replace('clearCnt', '격리해제 수').replace('examCnt', '검사진행 수').replace('deathCnt', '사망자 수').replace('careCnt', '치료중 환자 수').replace('resutlNegCnt', '결과 음성 수').replace('accExamCnt', '누적 검사 수').replace('accExamCompCnt', '누적 검사 완료 수').replace('accDefRate', '누적 확진률').replace('createDt', '등록일시분초').replace('updateDt', '수정일시분초')

js = json.loads(jsonString)
print(js)
js_check_count = js["response"]['body']['items']['item'][0]['검사진행 수']
js = js["response"]['body']['items']['item']
pdata = pd.DataFrame(js)

#날짜가 간혹 뒤바뀐게 있어서 정렬하고
#인덱스를 새로 생성했다.
pdata.sort_values(by = '기준일', inplace=True, ascending = False)
pdata = pdata.reset_index(drop = True)

# 일일 확진자 수와, 검사자 수의 데이터가 누적 값만 있어서
# 전일과의 차로 값을 일일 값을 구했다.

for row in range(0,289):
    pdata['치료중 환자 수'][row] = int(pdata.loc[row][7]) - int(pdata.loc[row+1][7])
    pdata['격리해제 수'][row] = int(pdata.loc[row][1]) - int(pdata.loc[row+1][1])
# 여러 컬럼중 내가 원하는 컬럼만 선택해서 출력, 저장한다.
# 사용하지 않을 컬럼인 치료중과 격리해제 컬럼에 저장하고 컬럼명을 바꾸겠다.( 새로운 컬럼을 추가하는 방법도 있음..)

pdata = pdata[['기준일','격리해제 수','치료중 환자 수','누적 확진률','누적 검사 수','사망자 수']]
pdata = pdata.rename(columns = {'치료중 환자 수' : '일일 확진자 수','격리해제 수':'일일 검사 수'})
pdata.to_csv('total_corona_count.csv')
print(pdata)
#일일 확진자 수가 많은 순서대로 정렬하여 출력해봤다.(20개)

pdata['일일 확진자 수'] = pd.to_numeric(pdata['일일 확진자 수'])
sortdata = pdata.sort_values(by = '일일 확진자 수', inplace=False, ascending = False)

print(sortdata[:20])