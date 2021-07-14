library(dplyr)
library(ggplot2)
#데이터 프레임 불러오기
midwest_raw<-as.data.frame(ggplot2::midwest)

#데이터 프레임의 복사본 생성하기
midwest_new<-midwest_raw

#1번 문제
str(midwest_new)
View(midwest_new)

#2번 문제
midwest_new <- rename(midwest_new, total=poptotal)
midwest_new <- rename(midwest_new, asian=popasian)

#3번 문제 total, asian 변수를 이용해 '전체 인구 대비 아시아 인구 백분율' 
#파생변수를 만들고, 
#히스토그램을 만들어 도시들이 어떻게 분포하는지 살펴보세요.
installed.packages(Cairo_pdf)
#3번 문제
midwest_new$percasian <- (midwest_new$asian / midwest_new$total) * 100
hist(midwest_new$percasian)


#4번 문제
percasian_mean <- mean(midwest_new$percasian)
percasian_mean
## [1] 0.4872462
midwest_new$mean <- ifelse(midwest_new$percasian > 
                             percasian_mean, 
                           "large", "small")

#5번 문제
table(midwest_new$mean)
## large small 
##  119   318 
qplot(midwest_new$mean)


#3번 문제
midwest_new <- midwest_new %>% 
  mutate(gradeyouth = ifelse(percyouth >= 40 ,"large",
                             ifelse(percyouth >= 30,"middle","small")))
table(midwest_new$gradeyouth)

## large middle  small 
##    32    396      9 


# x 축을 평균일 승차인원(AVG_ONEDAY)으로 설정하고
# y 축을 각 노선의 운행횟수(RUNNINGTIMES_WEEKDAYS)로 설정하고
# 평균 혼잡도(AVG_CROWDEDNESS)로 산점도를 그려보자


# x 축 각 노선(LINE)으로 일평균 막대그래프를 만들어보자
























