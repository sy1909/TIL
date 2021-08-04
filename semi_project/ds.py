#%%
# -*- coding: utf-8 -*-
import pandas as pd
from statistics import mean
import matplotlib.pyplot as plt # 막대그래프
#import seaborn as sns  # 

def corona(): # 파일 읽어오기
#    file_path = 'C:\\Users\\ksy\\downloads\\CARD_SUBWAY_MONTH_202106.csv'
    file_path = 'C:\\Users\\ksy\\downloads\\total_corona_count.csv'
    pdata = pd.read_csv(file_path , sep =',', encoding='euc-kr')
#    pdata = pd.read_csv(file_path2 , sep ='\t')

    print(pdata.columns)
    corona_col = [i for i in pdata.columns]
    # index 타입으로 되어있는 컬럼들을 리스트로 변환

    #.sort_values()를 사용하여 데이터 정렬
    # 자료의 기준일이 역순이므로  
    pdata_sort = pdata.sort_values(by= "기준일" , ascending=True)
    print(pdata_sort.head())
    
    #선그래프
    plt.plot(pdata_sort["기준일"] , pdata_sort["일일 확진자 수"])
    plt.show()

    # 한 그래프에 선 두개 표현
    plt.plot(pdata_sort["기준일"], pdata_sort["일일 확진자 수"])
    plt.plot(pdata_sort["기준일"], pdata_sort["일일 검사 수"])
    # 화면에 그래프를 보여줍니다
    plt.show()

    #Axis and Labels
    #종종 그래프의 특정 영역을 확대하거나 강조하고 싶을 수 있습니다. 
    # 이 때 보여줄 축의 범위를 .axis() 함수로 지정할 수 있습니다. 
    # .axis() 함수는 [ x_min, x_max, y_min, y_max ] 를 파라미터로 전달
    plt.plot(pdata_sort["기준일"], pdata_sort["일일 확진자 수"])
    plt.axis([20200201, 20201201, 0 , 10000] )
    plt.show()

    # 전일대비 칸을 추가?
    # 막대 그래프
    fig, ax = plt.subplots(1, 1, figsize=(12, 6))
    ax.bar(x=pdata_sort["기준일"].astype(str), height=pdata_sort["일일 확진자 수"])
    plt.show()

def subway():
    file_path = 'C:\\Users\\ksy\\downloads\\CARD_SUBWAY_MONTH_202105.csv'
#    pdata = pd.read_csv(file_path , sep =',', encoding='euc-kr')
    #index_col = False 꼭필요하다 꼭
    pdata = pd.read_csv(file_path , sep =',' , index_col=False)
#    pdata = pd.read_csv(file_path , encoding='CP949')
#    seoul_station = ["가락시장","가산디지털단지","가양","가오리",	"가좌",	"강남",	"강남구청",	"강동",	"강동구청",	"강변",	"강일",	"개롱",	"개봉",	"개포동",	"개화",	"개화산",	"거여",	"건대입구",	"경복궁",	"경찰병원",	"고덕",	"고려대",	"고속터미널",	"공덕",	"공릉",	"공항시장",	"광나루",	"광운대",	"광화문",	"광흥창",	"교대",	"구로",	"구로디지털단지",	"구룡",	"구반포",	"구산",	"구의",	"구일",	"구파발",	"국회의사당",	"군자",	"굽은다리",	"금천구청",	"금호",	"길동",	"길음",	"김포공항",	"까치산",	"낙성대",	"남구로",	"남부터미널",	"남성",	"남영",	"남태령",	"내방",	"노들",	"노량진",	"노원",	"녹번",	"녹사평",	"녹천",	"논현",	"답십리",	"당고개",	"당산",	"대림",	"대모산입구",	"대방",	"대청",	"대치",	"대흥",	"도곡",	"도림천",	"도봉",	"도봉산",	"독립문",	"독바위",	"독산",	"돌곶이",	"동대문",	"동대문역사문화공원",	"동대입구",	"동묘앞",	"동작",	"둔촌동",	"둔촌오륜",	"등촌",	"디지털미디어시티",	"뚝섬",	"뚝섬유원지",	"마곡",	"마곡나루",	"마들",	"마장",	"마천",	"마포",	"마포구청",	"망우",	"망원",	"매봉",	"먹골",	"면목",	"명동",	"명일",	"목동",	"몽촌토성",	"무악재",	"문래",	"문정",	"미아",	"미아사거리",	"반포",	"발산",	"방배",	"방이",	"방학",	"방화",	"버티고개",	"보라매",	"보문",	"복정",	"봉은사",	"봉천",	"봉화산",	"북한산보국문",	"북한산우이",	"불광",	"사가정",	"사당",	"사평",	"삼각지",	"삼성",	"삼성중앙",	"삼양",	"삼양사거리",	"삼전",	"상계",	"상도",	"상봉",	"상수",	"상왕십리",	"상월곡",	"상일동",	"새절",	"샛강",	"서강대",	"서대문",	"서빙고",	"서울대입구",	"서울숲",	"서울역",	"서초",	"석계",	"석촌",	"석촌고분",	"선릉",	"선유도",	"선정릉",	"성수",	"성신여대입구",	"솔샘",	"솔밭공원",	"송정",	"송파",	"송파나루",	"수락산",	"수색",	"수서",	"수유",	"숙대입구",	"숭실대입구",	"시청",	"신금호",	"신길",	"신내",	"신논현",	"신답",	"신당",	"신대방",	"신대방삼거리",	"신도림",	"신림",	"신목동",	"신반포",	"신방화",	"신사",	"신설동",	"신용산",	"신이문",	"신정",	"신정네거리",	"신촌(2)",	"신촌(경)",	"신풍",	"쌍문",	"아차산",	"아현",	"안국",	"안암",	"암사",	"압구정",	"압구정로데오",	"애오개",	"약수",	"양원",	"양재",	"양재시민의숲",	"양천구청",	"양천향교",	"양평(5)",	"어린이대공원",	"언주",	"여의나루",	"여의도",	"역삼",	"역촌",	"연신내",	"염창",	"영등포",	"영등포구청",	"영등포시장",	"오금",	"오류동",	"오목교",	"옥수",	"온수",	"올림픽공원",	"왕십리",	"외대앞",	"용답",	"용두",	"용마산",	"용산",	"우장산",	"월계",	"월곡",	"월드컵경기장",	"을지로입구",	"을지로3가",	"을지로4가",	"응봉",	"응암",	"이대",	"이수",	"이촌",	"이태원",	"일원",	"잠실",	"잠실나루",	"잠실새내",	"잠원",	"장승배기",	"장지",	"장한평",	"정릉",	"제기동",	"종각",	"종로3가",	"종로5가",	"종합운동장",	"중계",	"중곡",	"중랑",	"중앙보훈병원",	"중화",	"증미",	"증산",	"창동",	"창신",	"천왕",	"천호",	"청구",	"청담",	"청량리",	"충무로",	"충정로",	"태릉입구",	"하계",	"학동",	"학여울",	"한강진",	"한남",	"한성대입구",	"한성백제",	"한양대",	"한티",	"합정",	"행당",	"혜화",	"홍대입구",	"홍제",	"화계",	"화곡",	"화랑대",	"회기",	"회현",	"효창공원앞",	"흑석"	]
    print("행과 열의 개수는 " , pdata.shape)
    # 어떤 컬럼들이 있는지 
    print(pdata.columns)
    # 각 컬럼들의 데이터 타입을 알려준다.
    print(pdata.dtypes)

    print(pdata.head())
    # 생략가능 pdata.columns[] 이런식으로 쓰면 되지 않을까 싶음
    # index 타입으로 되어있는 컬럼들을 리스트로 변환
    subway_col = [i for i in pdata.columns]
    #종합 통계를 불러오는 함수
    print(pdata.describe())

#    print(pdata["사용일자"])
#    print(pdata["노선명"]

    print(pdata.groupby(['사용일자'])["하차총승객수"].sum())
    #시각화 사용일자 넣으면 키에러 

    #
    pdata["승하차총승객수"] = pdata["승차총승객수"] + pdata["하차총승객수"]
    print(pdata.head())

    # 사용일자 별로 묶어서 승하차총승객수만 나오는 테이블 저장
    pdata_sum = pdata.groupby(['사용일자'], as_index = False)["승하차총승객수"].sum()
#    pdata_sum = pdata.groupby(['사용일자'])["승하차총승객수"].sum()
    print( "pdata_sum groupby 사용일자 승하차총승객수" )
    print( pdata_sum.head() )
    print( pdata_sum.dtypes )

    #pdata_sum["사용일자"] = pd.to_datetime(pdata_sum["사용일자"] #1970-01-01 00:00:00.020210501
    pdata_sum["사용일자"] = pd.to_datetime(pdata_sum["사용일자"], format='%Y%m%d')
#    subDay['사용일자'] = pd.to_datetime(subDay['사용일자'].astype('str'), errors = 'coerce')
    print(pdata_sum.dtypes)

    print( pdata_sum.head() )

#----------------------------선그래프?----------------------
    plt.plot(pdata_sum["사용일자"] , pdata_sum["승하차총승객수"])
    plt.show()
#----------------------------막대그래프----------------------
    plt.bar(pdata_sum["사용일자"] , pdata_sum["승하차총승객수"])
    plt.show()

#----------------------------스타일 추가----------------------
    # 파선(Dashed)
    #plt.plot(pdata_sum["사용일자"], pdata_sum["승하차총승객수"], linestyle='--')
    # 점선(Dotted)
    plt.plot(pdata_sum["사용일자"], pdata_sum["승하차총승객수"], linestyle=':')
    # 실선(No line)
#    plt.plot(pdata_sum["사용일자"], pdata_sum["승하차총승객수"], linestyle='')
    plt.show()

    # 원(A circle)
    plt.plot(pdata_sum["사용일자"], pdata_sum["승하차총승객수"], marker='o')
    # 정사각형(A square)
#    plt.plot(pdata_sum["사용일자"], pdata_sum["승하차총승객수"], marker='s')
    # 별(A star)
#    plt.plot(pdata_sum["사용일자"], pdata_sum["승하차총승객수"], marker='*')
    plt.show()

#     a_mean = pdata["승차총승객수"].mean()
#     a_mean = pdata[subway_col[3]].mean()
#     print(a_mean)

#     b_mean = pdata[ pdata["노선명"] == '3호선' ]["승차총승객수"].sum()
#     print("승차합" , b_mean)
    
#     b_mean = pdata[ (pdata["사용일자"] == 20210601) & (pdata["역명"] == "어린이대공원(세종대)") ]["승차총승객수"].sum()
#     print(b_mean)

#     sun = pdata["노선명"].unique()
# #    print(sun)

#     station = pdata["역명"].unique()
#     print(len(station))
    # for i in station:
    #     print(i)
#    print(pdata["역명"].unique())


#    print(seoul_station)

    # print(len(station) , len(seoul_station) )
    # cnt =0
    # for i in station:
    #     if i in seoul_station:
    #         cnt +=1
    # print(cnt)

def subway_st(all_data):
    # file_path = 'C:\\Users\\ksy\\downloads\\CARD_SUBWAY_MONTH_202105.csv'
    # pdata = pd.read_csv(file_path , sep =',' , index_col=False)

    #넘겨받은 all_data 를 pdata로 바꾸고 역명체크단계
    pdata = all_data
    seoul_station = ["가락시장","가산디지털단지","가양","가오리",	"가좌",	"강남",	"강남구청",	"강동",	"강동구청",	"강변",	"강일",	"개롱",	"개봉",	"개포동",	"개화",	"개화산",	"거여",	"건대입구",	"경복궁",	"경찰병원",	"고덕",	"고려대",	"고속터미널",	"공덕",	"공릉",	"공항시장",	"광나루",	"광운대",	"광화문",	"광흥창",	"교대",	"구로",	"구로디지털단지",	"구룡",	"구반포",	"구산",	"구의",	"구일",	"구파발",	"국회의사당",	"군자",	"굽은다리",	"금천구청",	"금호",	"길동",	"길음",	"김포공항",	"까치산",	"낙성대",	"남구로",	"남부터미널",	"남성",	"남영",	"남태령",	"내방",	"노들",	"노량진",	"노원",	"녹번",	"녹사평",	"녹천",	"논현",	"답십리",	"당고개",	"당산",	"대림",	"대모산입구",	"대방",	"대청",	"대치",	"대흥",	"도곡",	"도림천",	"도봉",	"도봉산",	"독립문",	"독바위",	"독산",	"돌곶이",	"동대문",	"동대문역사문화공원",	"동대입구",	"동묘앞",	"동작",	"둔촌동",	"둔촌오륜",	"등촌",	"디지털미디어시티",	"뚝섬",	"뚝섬유원지",	"마곡",	"마곡나루",	"마들",	"마장",	"마천",	"마포",	"마포구청",	"망우",	"망원",	"매봉",	"먹골",	"면목",	"명동",	"명일",	"목동",	"몽촌토성",	"무악재",	"문래",	"문정",	"미아",	"미아사거리",	"반포",	"발산",	"방배",	"방이",	"방학",	"방화",	"버티고개",	"보라매",	"보문",	"복정",	"봉은사",	"봉천",	"봉화산",	"북한산보국문",	"북한산우이",	"불광",	"사가정",	"사당",	"사평",	"삼각지",	"삼성",	"삼성중앙",	"삼양",	"삼양사거리",	"삼전",	"상계",	"상도",	"상봉",	"상수",	"상왕십리",	"상월곡",	"상일동",	"새절",	"샛강",	"서강대",	"서대문",	"서빙고",	"서울대입구",	"서울숲",	"서울역",	"서초",	"석계",	"석촌",	"석촌고분",	"선릉",	"선유도",	"선정릉",	"성수",	"성신여대입구",	"솔샘",	"솔밭공원",	"송정",	"송파",	"송파나루",	"수락산",	"수색",	"수서",	"수유",	"숙대입구",	"숭실대입구",	"시청",	"신금호",	"신길",	"신내",	"신논현",	"신답",	"신당",	"신대방",	"신대방삼거리",	"신도림",	"신림",	"신목동",	"신반포",	"신방화",	"신사",	"신설동",	"신용산",	"신이문",	"신정",	"신정네거리",	"신촌(2)",	"신촌(경)",	"신풍",	"쌍문",	"아차산",	"아현",	"안국",	"안암",	"암사",	"압구정",	"압구정로데오",	"애오개",	"약수",	"양원",	"양재",	"양재시민의숲",	"양천구청",	"양천향교",	"양평(5)",	"어린이대공원",	"언주",	"여의나루",	"여의도",	"역삼",	"역촌",	"연신내",	"염창",	"영등포",	"영등포구청",	"영등포시장",	"오금",	"오류동",	"오목교",	"옥수",	"온수",	"올림픽공원",	"왕십리",	"외대앞",	"용답",	"용두",	"용마산",	"용산",	"우장산",	"월계",	"월곡",	"월드컵경기장",	"을지로입구",	"을지로3가",	"을지로4가",	"응봉",	"응암",	"이대",	"이수",	"이촌",	"이태원",	"일원",	"잠실",	"잠실나루",	"잠실새내",	"잠원",	"장승배기",	"장지",	"장한평",	"정릉",	"제기동",	"종각",	"종로3가",	"종로5가",	"종합운동장",	"중계",	"중곡",	"중랑",	"중앙보훈병원",	"중화",	"증미",	"증산",	"창동",	"창신",	"천왕",	"천호",	"청구",	"청담",	"청량리",	"충무로",	"충정로",	"태릉입구",	"하계",	"학동",	"학여울",	"한강진",	"한남",	"한성대입구",	"한성백제",	"한양대",	"한티",	"합정",	"행당",	"혜화",	"홍대입구",	"홍제",	"화계",	"화곡",	"화랑대",	"회기",	"회현",	"효창공원앞",	"흑석"	]
    
    #엑셀의 전체 역들 중복제거
    station = pdata["역명"].unique()
    print(len(station) , len(seoul_station) )

    cnt =0
    same_st = []
    for j in seoul_station: # 여기서 단어를 비교
        for i in station:   # statiion 내부 값에 () 가 추가로 붙어있음
            #print(j.find(i))
            if i.find(j) == 0 and i not in same_st:
                if i==j:
                    same_st.append(i)
                elif i.find(j+"(")==0:
                    same_st.append(i) 
                else:
                    pass                   
            elif i == "신촌" and j == "신촌(2)":
                same_st.append(j)
            elif i == "신촌" and j == "신촌(경)":
                same_st.append(j)
            elif i == "양평" and j == "양평(5)":
                same_st.append(j)

    cnt = 0
    ncnt = 0
    for i in all_data["역명"].unique():
        if i in same_st:
            cnt +=1
        else:
            ncnt +=1

    print("카운트  " , cnt , ncnt)
    print("---------------------------------------------------------------------")
    print("분류되기 전에 역명의 길이"  ,  len(all_data["역명"].unique()))
    seoul_data = all_data[ all_data["역명"].isin(same_st) ]
    print("---------------------------------------------------------------------")
    print("분류된 역명의 길이 " , len(seoul_data["역명"].unique()))
    print("---------------------------------------------------------------------")
    print(seoul_data)
    return seoul_data



from glob import glob # 파일 경로를 조작할 수 있다.
import chardet
def subway_all_file():
    # 해당 디렉토리 내에 .csv 파일을 다 불러와서 리스트에 담아준다.
    file_path = glob('C:\\Users\\ksy\\downloads\\data\\*.csv')
    all_file = []
    #인코딩 확인 코드-----------------------------------------------
    for path in file_path:
        rawdata = open(path, 'rb').read() #파일 열고
        result = chardet.detect(rawdata) # 인코딩 형식 검사하고
        charenc = result['encoding']  # 인코딩 결과 확인하고
        #print(charenc)    
    #인코딩 확인 코드 마무리 ----------------------------------------
        # utf8 error -> engine='python' 으로 해결 (무시하는듯 한글깨짐) 
        # 위에서 확인한 인코딩을 넣어서 append
        #위에 인코딩 확인코드 시간 줄일 필요 있을 듯 
        all_file.append(pd.read_csv(path ,encoding = charenc , index_col=False))
    #print(len(all_file))

    # 위에서 모든 엑셀 파일을 열어서 내용을 담은 all_file을 같은 컬럼이니 합친다.
    all_data = pd.concat(all_file, ignore_index=True)
    all_data["사용일자"] = pd.to_datetime(all_data["사용일자"], format='%Y%m%d')
    print("전체 엑셀 데이터가 합쳐진 첫번째")
    print(all_data)

    # 이제 모아놓은 전 엑셀 데이터를 서울을 주소지로 갖는 역으로 필터링 해주어야 한다.
    all_data = subway_st(all_data)
    print("역명이 분류된 두번째 전체 데이터")
    print(all_data) 

#--시각화 진행 함수로 만들기도 가능----------------------------------------------------------------------------------
    subway_col = [i for i in all_data.columns]
    #종합 통계를 불러오는 함수
    #print(all_data.describe())

    # 새로운 컬럼 생성 (승하차총승객수)
    all_data["승하차총승객수"] = all_data["승차총승객수"] + all_data["하차총승객수"]
    #print(all_data.head())

    # 사용일자 별로 묶어서 승하차총승객수만 나오는 테이블 저장
    pdata_sum = all_data.groupby(['사용일자'], as_index = False)["승하차총승객수"].sum()
#    pdata_sum = pdata.groupby(['사용일자'])["승하차총승객수"].sum()
    print( "pdata_sum groupby 사용일자 승하차총승객수" )
    print(pdata_sum)

#----------------------------선그래프?----------------------
    plt.plot(pdata_sum["사용일자"] , pdata_sum["승하차총승객수"])
    plt.show()
#----------------------------막대그래프----------------------
    plt.bar(pdata_sum["사용일자"] , pdata_sum["승하차총승객수"])
    plt.show()
    
    print('-----------------------------------------------------------')

from matplotlib import rcParams
from matplotlib import font_manager, rc
import matplotlib
matplotlib.font_manager._rebuild()
def gu_corona():
    
    file_path = 'C:\\Users\\ksy\\downloads\\서울특별시 코로나19 자치구별 확진자 발생동향.csv'
    pdata = pd.read_csv(file_path , encoding ='cp949' , index_col=False)
    # 날짜 변환
    pdata["자치구 기준일"] = pd.to_datetime(pdata["자치구 기준일"])# , format='%Y%m%d')
    # 날짜기준 정렬
    pdata = pdata.sort_values(by = ['자치구 기준일'])  
    print(pdata)
    print(pdata.dtypes)

    # 행열전환 자치구가 행으로 확진자수가  자세한 설명 아래 링크 참조
    # https://computer-science-student.tistory.com/158
    pdata = pdata.transpose()
    pdata.rename(columns = pdata.iloc[0] , inplace=True)
    pdata = pdata.drop(pdata.index[0])
    print(pdata)
    #------------------------------------------------------------
    print()
    print(pdata[1::2]) #추가 부분
    print(pdata[0::2]) #전체 부분만

    # 종로 - 기타
    pdata_add = pdata[1::2]
    pdata_all = pdata[0:-1:2]

    print(pdata_all.columns)
    print(type(pdata_all.columns))
    print(pdata_add.columns[0])
    print(len(pdata_all.index))
    print(len(pdata_add[pdata_add.columns[0]]))

    #한글깨짐 폰트설정
    font_path = 'C:\\Users\\ksy\\Downloads\\MaruBuri-Regular\\MaruBuri-Regular.ttf'
    font = font_manager.FontProperties(fname=font_path, size=18).get_name()
    rc('font' , family = font)
    plt.rcParams['axes.unicode_minus'] = False #한글 폰트 사용시 마이너스 폰트 깨짐 해결
    
    #파이차트
    plt.pie(pdata_add[pdata_add.columns[-1]], labels=pdata_all.index, autopct='%.1f%%')
    plt.title(str(pdata_add.columns[-1]) , fontsize = 15)
    plt.show()

    #종로구 전체에대해서 확진자수 그래프 index[0]에서 0을 i로주고 반복문 돌리면 전체 자치구
    print(pdata_all.loc[pdata_all.index[0]])
    plt.plot(pdata_all.columns , pdata_all.loc[pdata_all.index[0]])
    plt.title(pdata_all.index[0],fontsize=15)
    plt.show()
    # df = pdata_all.sort_values(by = ['확진자수'], ascending = False)       

    # # 누적 확진자 수 기준 파이 차트 그리기
    # # 시계 방향(12시, 90도), Top 5순
    # _, _, autopct = plt.pie(df['확진자수'], explode = explode, labels = df.index, shadow = True, autopct = '', startangle = 90, counterclock = False)

    # # 각각의 파이 안에 들어가는 레이블 중 Top 5만 설정
    # for i in range(5):
    #     autopct[i].set_text('{:,}'.format(df['확진자수'][i]))

    # plt.title('서울시 코로나 확진자 현황(자치구별)')
    # plt.xlabel('단위(명)')
    # plt.show()

#corona()
#subway()
#subway_st()
#subway_all_file()
gu_corona()



# %%
