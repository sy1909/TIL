
# 외부파일(csv , xsl , txt) & 데이터 가공 & 시각화

install.packages('readxl')
library(readxl)

# read_excel() - xl
# read.table() - txt
# header , skip , nrows , sep
tmp.xl <- read_excel(file.choose())
class(tmp.xl)
View(tmp.xl)
tmp.xl.df <- as.data.frame(tmp.xl)
class(tmp.xl.df)

tmp.txt <- read.table(file.choose() , 
                      header = T , 
                      nrows = 7  , 
                      sep = "\t") 

class(tmp.txt)
tmp.txt
str(tmp.txt)

# 데이터 로드 및 열 이름 부여
# col.names = 
colname <- c('ID' , 'GENDER' , 'AGE' , 'AREA') 
tmp.txt <- read.table(file.choose() , 
                      header = F , 
                      sep = "," , 
                      col.names = colname)
tmp.txt
names(tmp.txt)


write.csv(tmp.txt , file = "c:\\R_STUDY\\data\\save_data.csv")
write.table(tmp.txt , file = "c:\\R_STUDY\\data\\save_data.txt")

ex.data <- read_excel(file.choose())
ex.data.frm <- as.data.frame(ex.data)
str(ex.data.frm)

# sex , area -> factor 변경

ex.data.frm$SEX <- as.factor(ex.data.frm$SEX)
ex.data.frm$AREA <- as.factor(ex.data.frm$AREA)
levels(ex.data.frm$SEX)
levels(ex.data.frm$AREA)

# [ chain %>% , group_by , summarise ] , split
library(dplyr)

# 성별에 따른 AMT17 평균이용 금액
?split

class( split(ex.data.frm$AMT17 , ex.data.frm$SEX) )
class( sapply( split(ex.data.frm$AMT17 , ex.data.frm$SEX) , 
        mean , 
        na.rm = T) )

ex.data.frm %>%
  group_by(SEX) %>%
    summarise(cnt = n() , 
              mean = mean(AMT17))

# 지역에 따른 Y17_CNT 이용건수의 합

dim( ex.data.frm )

# rename()
# AMT17 -> Y17_AMT , AMT16 -> Y16_AMT 
?rename
ex.data.frm <- rename(ex.data.frm , Y17_AMT = AMT17 , Y16_AMT = AMT16 )

# 파생변수 추가
# AMT 합 , CNT 합

ex.data.frm$AMT.SUM <- ex.data.frm$Y16_AMT + ex.data.frm$Y17_AMT
ex.data.frm$CNT.SUM <- ex.data.frm$Y16_CNT + ex.data.frm$Y17_CNT

mutate(ex.data.frm,
                      amt.sum = Y17_AMT + Y16_AMT,
                      cnt.sum = Y17_CNT + Y16_CNT,
                      amt.avg = amt.sum / cnt.sum) 

# AGE50_YN 추가 나이가 50초과이면 Y , 미만 N
# ifelse~
ex.data.frm <- ex.data.frm %>%
  mutate(AGE50_YN = ifelse(AGE > 50 , 'Y' , 'N'))

ex.data.frm

class( ex.data.frm$ID )

class( ex.data.frm %>% select(ID) )

ex.data.frm %>% 
  select(ID , AREA , Y17_CNT) %>% 
    filter(AREA == '서울' & Y17_CNT >= 10) %>%
      arrange(desc(Y17_CNT) )


# 데이터 결합

# 두개의 파일을 로드
# 가로결합 , join
# inner join , left join, right join , full join
# inner.df <- join(tmp.x.df , tmp.y.df , by='id' , type='xxxxxx')
# left_join() , inner_join() , full_join()

m.history <- read_excel(file.choose())
f.history <- read_excel(file.choose())
m.history <- as.data.frame(m.history)
f.history <- as.data.frame(f.history)
library(plyr)

m.f.history.df <- join(m.history , f.history , by='ID' , type='full')

# 1. m.f.history.df 데이터 세트에서 ID 변수만 추출

# 2. m.f.history.df 데이터 세트에서 ID, AREA, Y17_CNT 변수 추출

# 3. m.f.history.df 데이터 세트에서 AREA 변수만 제외하고 추출

# 4. m.f.history.df 데이터 세트에서 AREA, Y17_CNT 변수를 제외하고 추출

# 5. m.f.history.df 데이터 세트에 AREA(지역)가 서울인 경우만 추출

# 6. m.f.history.df 데이터 세트에서 AREA(지역)가 서울이면서 
#    Y17_CNT(17년 이용 건수)가 10건 이상인 경우만 추출 

# 7. m.f.history.df 데이터 세트의 AGE 변수를 오름차순 정렬

# 8. m.f.history.df 데이터 세트의 Y17_AMT 변수를 내림차순 정렬


# 정렬 중첩 
# 9. m.f.history.df 데이터 세트의 AGE 변수는 오름차순, Y17_AMT 변수는 내림차순 정렬

# 데이터 요약하기
# 10. m.f.history.df 데이터 세트의 Y17_AMT(17년 이용 금액) 변수 값 합계를
# TOT_Y17_AMT 변수로 도출


# 11. m.f.history.df 데이터 세트의 AREA(지역) 변수 값별로 
# Y17_AMT(17년 이용 금액)를 더해 SUM_Y17_AMT 변수로 도출

# 12. m.f.history.df 데이터 세트의 AMT를 CNT로 나눈 값을 
# m.f.history.df 데이터 세트의 AVG_AMT로 생성

# 13. m.f.history.df 데이터 세트에서 AGE 변수 값이 50 이상이면 “Y”
# 50 미만이면 “N” 값으로 m.f.history.df 데이터 세트에 AGE50_YN 변수 생성 


# ::나이분류
# 14. m.f.history.df 데이터 세트의 
# AGE 값이 50 이상이면 “50++”, 
# 40 이상이면 “4049”
# 30 이상이면 “3039”, 
# 20 이상이면 "2029”, 
# 나머지는 “0019”를 값으로 하는 AGE_GR10 변수 생성

m.f.history.df$AGE_GR10 <- ifelse(m.f.history.df$AGE >=50 , '50++' , 
                                  ifelse(m.f.history.df$AGE >=40 , '4049' ,
                                         ifelse(m.f.history.df$AGE >=30 , '3039' ,
                                                ifelse(m.f.history.df$AGE >=20 , '2029' ,'0019'))))

str( m.f.history.df )
?summarise

m.f.history.df %>% 
  group_by(AREA) %>% 
    dplyr::summarise(SUM_Y17_AMT=sum(AMT17))

m.f.history.df

# descr::freq()
# 빈도분석 : 특정값이 얼마나 반복되는지

install.packages('descr')
library(descr)
?freq
freq(m.f.history.df$AREA , plot = T)
freqGender <- freq(m.f.history.df$SEX , plot = T)

barplot(freqGender)

# 시각화
# 변수 구분(이산 vs 연속)
# 이산변수 - 명목변수 , 순위변수
# 막대 , 점 , 파이


chart.data <- c(380, 520, 330, 390, 320, 460, 300, 405)
names(chart.data) <- c("2020 1Q","2020 2Q","2020 3Q","2020 4Q","2021 1Q","2021 2Q","2021 3Q","2021 4Q")

chart.data
range(chart.data)
max(chart.data)
min(chart.data)
length(chart.data)

?barplot

# 막대차트(세로, 가로)
barplot(chart.data , 
        xlim = c(0, 600), 
        col  = rainbow(8) , 
        main = '2020 vs 2021' , 
        horiz = T , 
        ylab  = '년도별 현황' , 
        xlab  = '매출 현황')

?dotchart

dotchart(chart.data , 
         color = c('green' , 'red') , 
         lcolor = 'blue' , 
         pch = 1:3 , 
         xlab = '매출액' , 
         cex = .8 ,
         main = '2020 vs 2021')

?pie

pie(chart.data , 
    labels = names(chart.data) , 
    border = 'blue' , 
    col = rainbow(8) , 
    cex = 1.5)

iris
pie(table(iris$Species))

?table

barplot( table(m.f.history.df$SEX)  , 
         names = c('남자' , '여자') , 
         main  = '성별' , 
         xlab  = 'gender' , 
         ylab  = 'cnt')



# 연속형 : 변수가 연속된 구간을 가지고 있다는 뜻
# 간격변수 , 비율변수
# 상자 , 히스토그램, 산점도
# boxplot() , hist() , plot()


m.f.history.df
?boxplot

boxplot(m.f.history.df$Y17_CNT , m.f.history.df$Y16_CNT)

iris
hist(iris$Sepal.Length , 
     xlab = '꽃받침 길이' , 
     ylim = c(0 , 40))

# 산점도
?plot
x <- runif(5, min = 0 , max = 1)
y <- x^2
x

plot(x, y , type = 'l')
plot(x, y , type = 'o' , pch = 25)
plot(x, y , type = 'h')
plot(x, y , type = 's')

# ?pairs - 산점도 매트릭스
pairs(iris[1:4])

# 3차원 산점도
install.packages('scatterplot3d')
library(scatterplot3d)
?scatterplot3d

scatterplot3d(iris$Sepal.Length , 
              iris$Petal.Length , 
              iris$Sepal.Width , type = 'p' , 
              color = c('red'))



# 시각화 알아보기
install.packages('mlbench')
library(mlbench)
iris

data(Ozone)
str(Ozone)

?Ozone

# 수치형 데이터 산점도
length(Ozone$V8)
length(Ozone$V9)
plot(Ozone$V8 , Ozone$V9)

# 축 이름
range(Ozone$V8 , na.rm = T)
range(Ozone$V9 , na.rm = T)

plot(Ozone$V8 , Ozone$V9 , 
     xlab = 'Sandburg Temp' , 
     ylab = 'EI Monte Temp' ,
     main = 'Region Temp' , 
     pch  = '+' , 
     cex  = 0.5 , 
     col  = 'red' , 
     xlim = c(20 , 100) , 
     ylim = c(25 , 85))


iris
summary(iris$Sepal.Length)
boxplot(iris$Sepal.Length)

# IQR(3사분위수 - 1사분위수)
summary(iris$Sepal.Width)
boxplot(iris$Sepal.Width)
# 3 -> 3.3
# 1 -> 2.8
# m -> 3
# whisker
# low   whisker : 중앙값 - 1.5 * IQR : 2.25
# high  whisker : 중앙값 + 1.5 * IQR : 3.75

boxplot(iris$Sepal.Width , 
        horizontal = T)

?boxplot

# iris의 setosa종과 versicolor종의 Sepal.Width 대한 상자 그림을 그려본다면?
# subset()

iris.subset <- subset(iris , Species == 'setosa'|Species == 'versicolor')
str(iris.subset)
levels(iris.subset$Species)
boxplot(Sepal.Width ~ Species , data = iris.subset)


library(ggplot2)
mpg

# 주요컬럼
# manufacturer : 제조회사
# displ : 배기량
# cyl : 실린더 개수
# drv : 구동 방식
# hwy : 고속도로 연비
# class : 자동차 종류
# model : 자동차 모델명
# year : 생산연도
# trans : 변속기 종류
# cty : 도시 연비
# fl : 연료 종류


















































































































