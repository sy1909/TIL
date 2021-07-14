#실습
library(readxl)
dataset.raw <- read_excel(file.choose())
str(dataset.raw)

dataset.raw.df <- as.data.frame(dataset.raw)
str(dataset.raw.df)

address <- dataset.raw.df$소재지전체주소
class(address)

address[1]
substr(address , 12 , 16)

address.trim.num <- gsub('[0-9]' , "" , address)
address.trim.space <- gsub('' , "" , address.trim.num)

library(dplyr)
address.tbl.df <- address.trim.space



install.packages('treemap')
library(treemap)



dust.dataset.raw <- read_excel(file.choose())
str(dust.dataset.raw)
head(dust.dataset.raw)

dust.dataset.df <- as.data.frame(dust.dataset.raw)
str(dust.dataset.df)
dust.dataset.df$area


dust.dataset.df %>%
  filter(area %in% c('동작구' , '서초구'))

library(readxl)
dataset.raw <- read_excel(file.choose())
str(dataset.raw)


# 아래문제들
# https://continuous-development.tistory.com/49 참조




library(stringr)
library(dplyr)


# 1. 데이터 전처리

# select와 filter를 통해 아래 컬럼만 뽑고 
# 주소지가 서울특별시인 데이터만 추출하여 확인해보자
# 번호, 사업장명, 소재지전체주소, 업태구분명, 시설총규모, 인허가일자, 폐업일자, 
# 소재지면적, 상세영업상태명, 영업상태구분코드

str(dataset.raw)
seoul_coffee <- dataset.raw %>%
  select(번호, 사업장명, 소재지전체주소, 업태구분명,시설총규모,인허가일자,폐업일자, 소재지면적, 상세영업상태명, 영업상태구분코드)
  filter( str_detect(소재지전체주소 , "서울특별시"))


# 커피숍 업태만 선택하기 # filter(업태구분명 == '커피숍')
# 폐업하지않고 현재 영업중인 카페찾기  # filter(상세영업상태명 == '영업')
# 지역구별로 데이터 나누기(서대문, 영등포, 동대문) 3개의 구만  #substr(seoul_coffee$소재지전체주소 , 6, 10)
# 추출(시각화로 사용할 예정)

seoul_coffee <- seoul_coffee%>%
  filter(업태구분명 == '커피숍')
View(seoul_coffee)
seoul_coffee <- seoul_coffee%>%
  filter(상세영업상태명 == '영업')
seoul_coffee$지역구 <-
  substr(seoul_coffee$소재지전체주소 , 6, 10)

nrow(seoul_coffee %>%
  filter(str_detect(지역구 , c("서대문구","영등포구","동대문구"))) )





# 인허가일자와 폐업일자의 데이터 형식이 
# chr와 logic으로 되어있는 것을 확인할 수 있다.
# ymd함수를 통해 chr와 logi형식으로 되어있는 데이터형식을 Date로 바꾼다.
install.packages("anytime")
library(anytime)
install.packages("lubridate")
library(lubridate)


# Date로 바꾼 인허가 일자 데이터를 바탕으로 인허가 
# year, month, day을 각각 추출해 가변수를 만들어보자  # ymd(seoul_coffee$인허가일자)
                                                      # year month day 로 붙할
seoul_coffee$인허가일자 <- ymd(seoul_coffee$인허가일자)
seoul_coffee$폐업일자 <- ymd(seoul_coffee$폐업일자)
str(seoul_coffee$인허가일자)
str(seoul_coffee$폐업일자)

seoul_coffee$년도 <- year(seoul_coffee$인허가일자)
seoul_coffee$월<- month(seoul_coffee$인허가일자)
seoul_coffee$일<- day(seoul_coffee$인허가일자)

# 데이터 형식 전처리(규모변수 추가)
# 시설총규모 타입 확인 후 문자형 -> 수치형    #as.numeric
# 시설총규모에 따라 이를 구분지어 

str(seoul_coffee$시설총규모)
seoul_coffee$시설총규모 < - as.numeric(seoul_coffee$시설총규모)

# 초소형, 초형, 중형, 대형, 초대형으로 구분지어볼려고 한다면
# 구분은 다음코드와 같이 임의로 지정
# 3제곱미터 이하는 초소형, 
# 30제곱미터 이하는 소형, 
# 70제곱미터이하는 중형 
# 300제곱미터 이하는 대형 그 이상은 초대형

library(dplyr) #mutate 에러있을 때 라이브러리
str(seoul_coffee)
seoul_coffee <- seoul_coffee %>%
  mutate(규모 = ifelse(시설총규모 <= 3 , "초소형" ,
                  ifelse(시설총규모 > 3 & 시설총규모 <= 30 , "소형" ,
                    ifelse(시설총규모 > 30 & 시설총규모 <= 70 , "중형" ,
                      ifelse(시설총규모 > 70 & 시설총규모 <= 300 , "대형" ,
                        ifelse(시설총규모 > 300, "초대형", "" ))))))
seoul_coffee$규모


# 규모별 커피숍 수 확인하기
# 영업중이면서 인허가일자가 2000년 이후 인 커피숍 수를 규모별로 확인해 본다면

# group_by() 는 출력결과를 데이터프레임의 업그레이드 버전인 tibble 형태로 만들고
# n()은 데이터가 몇 행으로 되어 있는지 ’빈도’를 구하는 기능

seoul_coffee %>% 
  group_by(규모) %>%
  summarise(n=n())



seoul_coffee %>% 
  filter(상세영업상태명 == "영업" & 인허가일자>="2000-01-01") %>%
  group_by(규모) %>%
  summarise(n=n())

# 가장 큰 규모의 카페는 어딜까요?

cafe
with.max(cafe$시설총규모)

cafe <- seoul_coffee %>% 
  filter(상세영업상태명 == "영업" & 인허가일자>="2000-01-01")
cafe[which.max(cafe$시설총규모),]


# 시설 총규모를 히스토그램으로 시각화한다면?
install.packages("ggplot2")
library(ggplot2)
library(dplyr)
library(magrittr)
str(cafe$시설총규모)
cafe$시설총규모 <- as.numeric(cafe$시설총규모)
cafe %>%
  ggplot(aes(x = 시설총규모 , y = ..density.. , fill = 규모)) +
  geom_histogram(binwidth = 30) +
  scale_x_continuous(breaks = c(100, 200, 300, 400, 500, 600))+
  geom_density(fill = NA , col = "red" , alpha=.8)+
  geom_line(stat = "density" , size = 1)


# 현재영업중인 카페의 인허가연도 히스토그램


# 영업과페업한 카페의 인허가 연도를 히스토 그램으로 시각화
seoul_coffee %>%
  filter(인허가일자 >= "2000-01-01") %>%
  ggplot( aes(x=년도 , fill= 상세영업상태명))+
  geom_histogram()


# 서울소재 커피숍의 인허가 년도별 숫자 확인
# 정보확인 후 데이터 프레임으로 만드세요~~

# 서울소재 커피숍의 인허가 년도별 숫자와 현재 영업중인 정보확인
# 정보확인 후 데이터 프레임으로 만드세요~ 


# 생존율 시각화
# geom_line , geom_point


# 2001년도 시설총규모에 따른 영업구분을 히스토그램으로 시각화




# 2000년도 ~ 
# 지역구에 따른 년도별 커피숍 인허가 정보를 요약하고
# 데이터 프레임으로 만들어보자


# 2000년도 ~
# 지역구에 따른 년도별 커피숍 인허가 정보와 
# 현재영업중인 정보를 요약하고 
# 데이터 프레임으로 만들어보자
