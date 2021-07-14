
# 조작
# package:: plyr , dplyr
# filter() : 지정한 조건식에 맞는 데이터 추출
# select() : 열의 추출
# mutate() : 열 추가
# arrange() : 정렬
# group_by()  : 그룹
# summarise() : 집계

install.packages(c("plyr" , "dplyr" , "hflights"))
library(plyr)
library(dplyr)
library(hflights)

# 휴스턴에서 출발하는 모든 비행기의 이착륙기록(2011)
str(hflights)
head(hflights)

flight.df <- hflights

# tbl_df()
# as_tibble(flight.df)

flight.tbl <- tbl_df(flight.df)


# filter() 조건에 맞는 행 추출
# 1월 1일 데이터만 추출
?filter

filter(flight.tbl , Month==1 , DayofMonth==1)
filter(flight.df , Month==1 , DayofMonth==1)

# 1월 또는(|) 2월 정보만 추출

filter(flight.tbl , Month==1 | Month==2)

# 열의 기준 기본 오름차순 , 내림차순 desc()
arrange(flight.tbl , Month)
arrange(flight.tbl , desc(Month))

select(flight.tbl , Year , Month , DayofMonth)
select(flight.tbl , -c(Year , Month , DayofMonth))
select(flight.tbl , (Year:DayofMonth))
select(flight.tbl , -(Year:DayofMonth))

# 열 추가 - 파생변수
str(flight.df)

mutate(flight.tbl , 
       gain = ArrDelay - DepDelay , 
       gain.per.hour = gain/(AirTime/60) ) 

head(flight.tbl)

# error
transform(flight.tbl , 
       gain = ArrDelay - DepDelay , 
       gain.per.hour = gain/(AirTime/60) ) 


# summarise()
# 출발지연시간 평균 및 합계
sum(is.na(flight.df$DepDelay))

summarise(flight.df , 
          delay.avg = mean(DepDelay , na.rm = T) , 
          delay.sum = mean(DepDelay , na.rm = T))


str(flight.df)

# TailNum : 항공기 일련번호
planes.df <- group_by(flight.df , TailNum)
str(planes.df)

# 항공기별 요약 통계량 : 평균비행거리 , 평균 도착지연시간
tmp.df <- summarise(planes.df , 
                    count = n() , 
                    dis = mean(Distance , na.rm = T) , 
                    delay = mean(ArrDelay , na.rm = T) )
tmp.df

# 편수가 20 이상이고 거리가 2000 이상인 데이터 추출

delay <- filter(tmp.df , count > 20 , dis > 2000) 
str(delay)

# chain() 함수
# %>% 조작을 연결해서 한 번에 수행하는 함수

flight.df

# 단계 1 group_by
# Year , Month , DayofMonth 의 수준별 그룹화
tmp01 <- group_by(flight.df , Year , Month , DayofMonth)

# 단계 2 select
# Year 부터 DayofMonth , ArrDelay , DepDelay 열 선택
tmp02 <- select(tmp01 , Year:DayofMonth , ArrDelay , DepDelay)

# 단계 3 summarise
# 평균 연착시간과 평균 출발 지연시간을 구한다
tmp03 <- summarise(tmp02 , 
                   arr = mean(ArrDelay , na.rm = T) , 
                   dep = mean(DepDelay , na.rm = T))

# 단계 4 filter
# 평균 연착시간과 평균 지연시간이 30분 이상인 데이터만 추출
tmp04 <- filter(tmp03 , arr > 30 | dep > 30)

flight.df %>% 
  group_by(Year , Month , DayofMonth) %>%
    dplyr::select(Year:DayofMonth , ArrDelay , DepDelay) %>%
      dplyr::summarise(arr = mean(ArrDelay , na.rm = T) , 
                dep = mean(DepDelay , na.rm = T)) %>%
        filter(arr > 30 | dep > 30)


# 입력값은 배열, 데이터 프레임 , 리스트 
# adply()
# 데이터 분할(split)
# 분할된 데이터에 함수를 적용(apply) - 행 1, 열 2
# 결과를 조합(combine)하는 함수
# 리턴타입 배열, 데이터 프레임 , 리스트 


iris
apply(iris[ , 1:4] , 1 , function(row) {
  print(row)
} )

# Sepal.Length 가 5.0 이상이고
# Species가 setosa인 것들만 가져와서 새로운 열(sepal.5.setosa)을 추가한다면?

iris %>%
  filter(Sepal.Length >= 5.0 , Species == 'setosa') %>%
    mutate(sepal.5.setosa = 'selected')

tmp <- split(iris ,iris$Species)$setosa
class( tmp ) 

apply(tmp , 2 , function(x) {
  x >= 5.0 
})

tmp$sepal.5.setosa <- c(tmp$Sepal.Length >= 5.0 & 
                          tmp$Species == 'setosa')

adply(iris , 
      1,
      function(row) {
        data.frame(sepal.5.setosa = c(row$Sepal.Length >= 5.0 & 
                                      row$Species == 'setosa'))
      })  


library(MASS)
Cars93



# package::plyr
# data.frame 
# join() : key값을 기준으로 두개의 프레임을 병합
# inner join , left join, right join , full join

tmp.x.df <- data.frame(
  id=c(1,2,3,4,6) , 
  height = c(160, 175, 180, 177, 194)
)

tmp.y.df <- data.frame(
  id = c(5, 4, 3, 2, 1) , 
  weight = c(55, 77, 90, 78, 95)
)

# by=c('id','gender')
inner.df <- join(tmp.x.df , tmp.y.df , by='id' , type='full')


library(MASS)
Cars93
str(Cars93)
head(Cars93)

# 컬럼이름확인
names(Cars93)

# distinct 중복없이 유일한 값을 리턴
Cars93$Origin
distinct(Cars93 , Origin)



# 문) Cars93 데이터 프레임에서 '차종(Type)'과 '생산국-미국여부(Origin)' 변수를 기준으로 
#     중복없는 유일한 값을 추출하시오.
?distinct
distinct(Cars93 , Origin)
distinct(Cars93 , Type)
distinct(Cars93 , Origin , Type)


?sample
?sample_n
?sample_frac
# 문) Cars93 데이터 프레임(1~5번째 변수만 사용)에서 10개의 관측치를 무작위로 추출하시오.
sample_n(Cars93[ , 1:5] , 10)

# 문) Cars93 데이터 프레임(1~5번째 변수만 사용)에서 
# 10%의 관측치를 무작위로 추출하시오.
nrow(Cars93) * 0.1
sample_frac(Cars93[ , 1:5] , 0.1)


# 문) Cars93 데이터 프레임(1~5번까지 변수만 사용)에서 
# 20개의 관측치를 무작위 복원추출 하시오.
sample_n(Cars93[ , 1:5] , 20 , replace = T)


# 문) Cars93 데이터 프레임에서 
# '제조국가_미국여부(Origin)'의 'USA', 'non-USA' 요인 속성별로 
# 각 10개씩의 표본을 무작위 비복원 추출하시오.
Cars93[ , c('Model' , 'Origin')] %>% group_by(Origin) %>% sample_n(10)



# 문) Cars93 데이터프레임에서 
# 최소가격(Min.Price)과 최대가격(Max.Price)의 범위(range), 
# 최소가격 대비 최대가격의 비율(=Max.Price/Min.Price) 의 
# 새로운 변수를 생성하시오.
names(Cars93)
new.df <- Cars93[ c(1:10) , c('Model' , 'Min.Price' , 'Max.Price') ]
new.df <- mutate(new.df , 
                 Range.Price = Max.Price - Min.Price , 
                 Range.Price.Rate = Max.Price / Min.Price)


# 문) Cars93 데이터 프레임에서 
# 가격(Price)의 (a) 평균, (b) 중앙값, (c) 표준편차, (d) 최소값, 
# (e) 최대값 합계를 구하시오. 
# (단, 결측값은 포함하지 않고 계산함)
summarise(Cars93 , 
          Price.mean = mean(Price , na.rm = T) , 
          Price.median = median(Price , na.rm = T) , 
          Price.sd = sd(Price , na.rm = T) , 
          Price.var = var(Price , na.rm = T) , 
          Price.iqr = IQR(Price , na.rm = T))

# 편차 = 데이터 값 - 평균값
# 제곱을해서 평균을 취한 - 분산
# 분산은 데이터의 흩어진 척도
# 분산 root를 씌우면 표준편차(평균적인 편차)
# sd() , var()


# 문) Cars93_1 데이터 프레임에서 
# (a) 총 관측치의 개수, 
# (b) 제조사(Manufacturer)의 개수(유일한 값), 
# (c) 첫번째 관측치의 제조사 이름, 
# (d) 마지막 관측치의 제조사 이름, 
# (e) 5번째 관측치의 제조사 이름은?
new.df <- Cars93[ c(1:10) , c('Model' , 'Type' , 'Manufacturer') ]
summarise(new.df , 
          total = n() , 
          distinct_cnt = n_distinct(Manufacturer) , 
          fisrt.obs    = first(Manufacturer) , 
          last.obs     = last(Manufacturer) ,
          nth.obs      = nth(Manufacturer, 5)  )

# 문) Cars93 데이터 프레임에서 
# '차종(Type)' 별로 구분해서 
# (a) 전체 관측치 개수, 
# (b) (중복 없이 센) 제조사 개수, 
# (c) 가격(Price)의 평균과 (d) 가격의 표준편차를 구하시오. 
# (단, 결측값은 포함하지 않고 계산함)
str(Cars93)
grouped <- group_by(Cars93 , Type)
summarise(grouped , 
          total = n() , 
          distinct_cnt = n_distinct(Manufacturer) , 
          price.mean   = mean(Price , na.rm = T) , 
          price.sd     = sd(Price , na.rm = T))



# ddply()
?ddply
iris
ddply(iris , 
      .(Species) , 
      function(sub) {
        data.frame(sepal.width.mean = mean(sub$Sepal.Length) )
      })

ddply(iris , 
      .(Species , Sepal.Length >5.0) , 
      function(sub) {
        data.frame(sepal.width.mean = mean(sub$Sepal.Length) )
      })

baseball
str(baseball)

# id가 ansonca01 선수의 기록을 확인한다면?

subset(baseball , id=='ansonca01')
filter(baseball , id=='ansonca01')
baseball[baseball$id=='ansonca01' , ]

# ddply() 이용해서 각 선수가 출전한 게임수의 평균을 구한다면?
names(baseball)
ddply(baseball , 
      .(id , g > 100) , 
      function(sub) {
        data.frame(g.mean = mean(sub$g) )
      })


# 각 선수별 최대게임을 플레이한 해의 기록을 구한다면?
# View(baseball)
ddply(baseball , 
      .(id) , 
      subset , 
      g == max(g))

# 
ddply(baseball , 
      .(id) , 
      summarise , 
      minyear = min(year) , 
      maxyear = max(year)) 

# reshape
# 프레임의 구조를 변경할 때 사용하는 함수
# melt , dcast 

library(reshape2)
View(french_fries)

str(french_fries)

head(french_fries)

# melt
# ID , 측정대상 변수 , 측정치 값
# complete.cases() : 해당 행의 모든 값이 NA 아닌경우 T , 
french_fries[ !complete.cases(french_fries) ,  ]
french_fries.melt <- melt(id = 1:4, french_fries , na.rm = T)

View(french_fries.melt)
head(french_fries.melt , 20)
tail(french_fries.melt , 20)

# cast() : 원상복구
# 원상복구하고자하는 타입에 따라서 dcast(frame) , acast(vector , matrix , array)
?dcast

french_fries.dcast <- dcast(french_fries.melt , time + treatment + subject + rep ~ ...)
class( french_fries.dcast )

french_fries.acast <- acast(french_fries.melt , time + treatment + subject + rep ~ ...)
class( french_fries.acast )


tmp.data <- read.csv(file.choose())
str(tmp.data)
head(tmp.data)

unique(tmp.data$Customer_ID)
length(unique(tmp.data$Customer_ID))

?melt
wide <- dcast(tmp.data , formula = Customer_ID~Date , sum)
long <- melt(wide , id='Customer_ID')


install.packages("data.table")
library(data.table)
View(iris)
iris.table <- data.table(iris) 
class(iris.table)

iris.table[1, ]
iris.table[iris.table$Species == 'setosa', ]



























