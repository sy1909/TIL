
# 시각화
# graphics , lattice , ggplot

# ggplot2

library(ggplot2)
library(dplyr)

# 크게 4가지의 종류로 분류 할 수 있다
# ggplot()
# geom_XXXXXXX (그래프, 도형)
# coord_XXXXXX (옵션)

# ggplot()
# aes(x축변수 , y축변수)
# geom_point() : 산점도
# geom_line() : 선 그래프
# geom_boxplot() : 
# geom_histogram()
# geom_bar()


# ggplot() + geom_xxxx() + coord_xxx()

iris
?ggplot
ggplot(data = iris , 
       mapping = aes(x = Sepal.Length , 
                     y = Sepal.Width)) +
  geom_point(colour = 'red' , 
             pch  = 4 , 
             size = 1 )

g <- ggplot(data = iris , 
       mapping = aes(x = Sepal.Length , 
                     y = Sepal.Width)) +
  geom_point(colour = c('red','blue','green')[iris$Species] , 
             pch  = c(0,2,20)[iris$Species] , 
             size = c(1,1.5,2)[iris$Species] )

g

# geom_abline() , geom_hline() , geom_vline() , geom_rect() , geom_text() 

library(plyr)
iris

# 종별 sl , sw 최소값과 최대값을 구한다면?

tmp <- ddply(iris , 
             .(Species) , 
             summarise , 
             min_x = min(Sepal.Length) , 
             max_x = max(Sepal.Length) ,
             min_y = min(Sepal.Width)  , 
             max_y = max(Sepal.Width) )

start_x <- max(tmp$min_x)
end_x   <- min(tmp$max_x) 

start_y <- max(tmp$min_y)
end_y   <- min(tmp$max_y)

# annotate() - 어떠한 도형을 그릴 것인지를 정하고 옵션을 부여할 수 있다
?annotate
annotate()

g <- ggplot(data = iris , 
            mapping = aes(x = Sepal.Length , 
                          y = Sepal.Width)) +
  geom_point(colour = c('red','blue','green')[iris$Species] , 
             pch  = c(0,2,20)[iris$Species] , 
             size = c(1,1.5,2)[iris$Species] )

cat(start_x , end_x , start_y , end_y)
g + annotate(
  geom = 'rect' ,
  xmin = start_x , 
  xmax = end_x , 
  ymin = start_y , 
  ymax = end_y , 
  fill = 'red' , 
  alpha = 0.2 , 
  colour = 'black' , 
  lty = 2
)


g + coord_cartesian(xlim = c(start_x , end_x) , 
                    ylim = c(start_y , end_y) )
?labs
g + labs(title    = '제목' , 
         subtitle = '부제목' , 
         caption  = '주석' , 
         x = 'x축의 이름' , 
         y = 'y축의 이름')



tmp.df <- data.frame(
  years = c(2015, 2016, 2017, 2018, 2019, 2020, 2021) , 
  gdp   = c(300, 350, 400, 450, 500, 550, 600)
)

ggplot(data = tmp.df , 
       aes(x = years , y = gdp)) +
  geom_point(colour = 'red' , 
             pch  = 2 , 
             size = 2) +
  geom_line(linetype = 'dashed')


install.packages('gcookbook')
library(gcookbook)
uspopage
str(uspopage)
head(uspopage , 10)

# 영역차트
# ggplot + geom_area

ggplot(uspopage , 
       aes(x = Year , y = Thousands , fill=AgeGroup)) +
  geom_area(colour = 'black' , 
            size   = 2 ,
            alpha  = .4)


# 막대그래프
# geom_bar()

tmp.df <- data.frame(
  movies = c('강철비2' , '발신제한' , '아바타' , '크루엘라' , '루카'),
  cnt    = c(5, 11, 3, 8, 10)
)
str(tmp.df)
?geom_col
?geom_bar

ggplot(data = tmp.df , 
       aes(x = movies , y = cnt)) +
  geom_col(col = 'blue' , width = .4 , fill = 'red') + 
  ggtitle('bar chart')




ggplot(data = tmp.df , 
       aes(x = cnt)) +
  geom_bar()

library(MASS)
str( Cars93 )
ggplot(data = Cars93 , 
       aes(x = Type)) +
  geom_bar()

# dataframe 을 sql로 구현하는 라이브러리
install.packages('sqldf')
library(sqldf)

head(Cars93 , 10)
names(Cars93)

type.cnt.df <- sqldf('select Type , count(*) as cnt
      from  Cars93
      group by Type
      order by Type')
class(type.cnt.df)
str(type.cnt.df)

ggplot(data = type.cnt.df , 
       aes(x = Type , y = cnt)) +
  geom_bar(stat = 'identity' , fill = 'yellow' , col='red') +
    ggtitle('bar chart using type')


# Stacked Bar char
# 학급의 총 인원과 남학생, 여학생의 인원을 한 그래프에 표현

class.num <- c(1,2,3,4,5,6)
class.m   <- c(30, 20, 24, 37, 43, 23)
class.f   <- c(20, 18, 38, 32, 34, 45)

tmp.cls.df <- data.frame(class.num , class.m , class.f)

# reshape2 , melt , cast(d, a) 
library(reshape2)
?melt

cls.melt.df <- melt(tmp.cls.df , 
                    id = c('class.num'))

ggplot(data = cls.melt.df , 
       aes(x = class.num , y = value , fill = variable)) +
  geom_bar(stat = 'identity' , width = .4)


# multi bar
# position = dodge
ggplot(data = cls.melt.df , 
       aes(x = class.num , y = value , fill = variable)) +
  geom_bar(stat    = 'identity' , 
           position = position_dodge(width = .4)) 


# Cars93 차종(Type)별 제조국(Origin) 자동차 수를 막대그래프로 표현
?Cars93

ggplot(Cars93 , 
       aes(x = Type , fill = Origin)) +
  geom_bar(position = position_dodge(width = .4)) +
    ggtitle('multi bar')


# 막대그래프에 오차()막대 추가
# 오차 : 평균, 표준편차
# geom_errorbar()

letters[1:5]
sample(seq(4,15) , 5)
sd = c(1,0,2,3,2,4)

tmp.avg.df <- data.frame(
  name  = letters[1:5] , 
  value = sample(seq(4,15) , 5) , 
  sd    = c(1,0,2,3,4)
)

ggplot(tmp.avg.df) +
  geom_bar(aes(x = name , y = value) , 
           stat = 'identity' , 
           fill = 'skyblue') +
    geom_errorbar(aes(x=name , ymin = value - sd , ymax = value + sd),
                  width = 0.4 , 
                  colour = 'orange' , 
                  alpha = .8 , 
                  size = 1.3)
iris
library(dplyr)
data <- iris %>% dplyr::select(Species , Sepal.Length)

# 평균(mean) , 표준편차(sd)
# 표준오차 : 
# 신뢰구간(Confidence Interval) : 

data.mean.sd <- data %>% 
  group_by(Species) %>%
    dplyr::summarise(cnt  = n() , 
                     mean = mean(Sepal.Length) , 
                     sd   = sd(Sepal.Length)) %>%
      mutate( se = sd / sqrt(cnt) ) %>%
        mutate( ic = se * qt( (1-0.05)/2 + .5 , cnt-1) )

data.mean.sd

ggplot(data.mean.sd) +
  geom_bar(aes(x = Species , y = mean) , 
           stat = 'identity' , 
           fill = 'green' , 
           alpha = 0.5) +
    geom_errorbar(aes(x=Species , ymin = mean-sd , ymax = mean + sd) ) +
    ggtitle('using standard deviation')


# 히스토그램 vs 막대그래프
# 양적자료      범주
# 히스토그램 도수분포 표현한다
# 가로축->계급(막대의 넓이) , 세로축->도수
# geom_histogram()
# rnorm() : 정규분포난수


hist.df <- data.frame(
  gender = factor(rep(c('F' , 'M') , each = 200)),
  weight = round( c( rnorm(200 , mean=55 , sd=5) , rnorm(200 , mean=65 , sd=5) ))
)

ggplot(hist.df) +
  geom_histogram(aes(x = weight , fill = gender) )

ggplot(hist.df) +
  geom_histogram(aes(x = weight , fill = gender) , 
                 bins = 20  , 
                 binwidth = 5)


# 산점도
# geom_point()


tmp.df <- data.frame(
  years = c(2015, 2016, 2017, 2018, 2019, 2020, 2021) , 
  gdp   = c(300, 350, 400, 450, 500, 550, 600)
)

ggplot(data = tmp.df,
       aes(x = years , y = gdp)) +
  geom_point(shape = 24 , size = 5 , color = 'red')

rownames(tmp.df) <- letters[1:7]

ggplot(data = tmp.df,
       aes(x = years , y = gdp)) +
  geom_point(shape = 24 , size = 5 , color = 'red') +
  geom_text(label = rownames(tmp.df))


tmp.df <- cbind(tmp.df  ,
                gender = c('F' , 'M' , 'M' ,'M' ,'M' , 'F' , 'F'))


ggplot(data = tmp.df,
       aes(x = years , y = gdp , shape = gender , color=gender)) +
  geom_point(size = 5 , color = 'red') +
  geom_text(label = rownames(tmp.df))


# boxplot
# geom_boxplot()

weight1 <- c(56, 67, 42, 48, 55, 61, 52, 39,
             47, 58, 50, 40, 59, 62, 44, 57, 129)
weight2 = c(78, 34, 37, 72, 58, 
            68, 27, 55, 65, 40, 75, 33, 66, 116)
data1 = data.frame(weight = weight1 , 
                   num = as.factor( rep(1,17)))

data2 = data.frame(weight = weight2 , 
                   num = as.factor( rep(2,14)))

data3 <- rbind(data1 , data2)

ggplot(data = data3) +
  geom_boxplot(aes(x = num , y=weight) , 
               outlier.color = 'red' , 
               outlier.shape = 24 , 
               outlier.size  = 2) +
  coord_flip()


ggplot(data = data3 , aes(x = num , y=weight)) +
  geom_boxplot(outlier.color = 'red' , 
               outlier.shape = 24) +
  geom_dotplot(binaxis  = 'y' , 
               stackdir = 'center' , 
               dotsize  = .8)



ggplot(data = data3 , aes(x = num , y=weight)) +
  geom_boxplot() +
  geom_jitter(shape = 16)


# Word Cloud
install.packages('wordcloud2')
library(wordcloud2)

demoFreq
str(demoFreq)

# 기본
wordcloud2(demoFreq , 
           size  = 1.6 , 
           color = 'random-light' , 
           backgroundColor = 'black')

install.packages('webshot')


install.packages('htmlwidgets')

library(webshot)
library(htmlwidgets)


myHtml <- wordcloud2(demoFreq , 
           size  = 1.6 , 
           color = 'random-light' , 
           backgroundColor = 'black')

saveWidget(myHtml , 
           'tmp.html' , selfcontained = F)

webshot::install_phantomjs()

webshot('tmp.html' , 
        'tmp.pdf'  ,
        delay = 5  , 
        vwidth  = 480 , 
        vheight = 480)


airquality
str(airquality)

# x축은 Day 열, y축은 Temp 열로 맵핑1
# 산점도 그리기
# 크기를 3, 색상을 빨강으로 적용하여 산점도 그리기
# x축을 Day, y축을 Temp로 맵핑한 후 꺾은선그래프 그리기
# x축을 Day, y축을 Temp로 맵핑한 후 꺾은선그래프와 산점도 그리기
# 꺾은선그래프 색상을 빨간색과 산점도 크기를 3으로 변경하고 겹쳐 그리기
# 상자그림 그리기
# airquality에서 Temp의 히스토그램


# mtcars에서 cyl 종류별 빈도수 확인
# 빈 범주를 제외하고 cyl 종류별 빈도수 확인
# cyl 종류별 gear 빈도 누적 막대그래프
# 선버스트 차트 그리기
# 원그래프 그리기
# 산점도를 그리고 데이터 레이블 입력하기
# 산점도에 사각형 그리기
# 산점도에 사각형 및 화살표 그리기
# 산점도에 사각형, 화살표, 레이블 추가하기
# x축을 wt, y축울 mpg로 맵핑
# 막대그래프에 제목 추가하기




































































  



  



























































