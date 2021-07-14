
# 함수 - function()
# for 반복구문

stu.kor  <- c(81, 95, 70)
stu.eng  <- c(75, 88, 78)
stu.mat  <- c(78, 99, 100)
stu.name <- c('한태형' , '임정섭' , '강려명')

stu.df <- data.frame(stu.name , 
                     stu.kor ,
                     stu.eng , 
                     stu.mat)
str(stu.df)
head(stu.df)

# 파생변수 : 데이터프레임에 있는 열을 이용해서 새로운 열을 추가하는것
# 총점, 평균을 구해서 stu.sum , stu.avg 파생변수 추가할려고 한다면?
# apply
# cbind()
?apply

stu.sum = apply(stu.df[2:4] , 1 , sum)
stu.avg = apply(stu.df[2:4] , 1 , mean)

stu.df$stu.sum <- stu.sum
stu.df$stu.avg <- stu.avg
stu.df

stu.cbind.df <- cbind(stu.df , 
                      stu.cbind.sum = apply(stu.df[2:4] , 1, sum))

stu.cbind.df <- cbind(stu.cbind.df , 
                      stu.cbind.avg = apply(stu.df[2:4] , 1, mean))



stu.df
# stu.grade 파생변수 추가
# A, B, C, D, F
# for, if
stu.grade <- ""
size <- nrow(stu.df)
for(idx in 1:size) {
  if(stu.df$stu.avg[idx] >= 90) {
    stu.grade[idx] <- "A"
  }else if(stu.df$stu.avg[idx] >= 80) {
    stu.grade[idx] <- "B"
  }else if(stu.df$stu.avg[idx] >= 70) {
    stu.grade[idx] <- "C"
  }else if(stu.df$stu.avg[idx] >= 60) {
    stu.grade[idx] <- "D"
  }else {
    stu.grade[idx] <- "F"
  }
}
stu.df$stu.grade <- stu.grade

# stu.df$stu.grade <- stu.grade
# stu.df$stu.grade <- NULL
stu.df[1, ]$stu.avg
stu.df$stu.avg[2]

stock.df <- read.csv(file.choose())
str(stock.df)
head(stock.df)


# 
diff <- c()
rows <- nrow(stock.df)
for(idx in 1:rows) {
  diff[idx] <-stock.df$High[idx] - stock.df$Low[idx]
}
stock.df$diff <- diff 
head(stock.df)

# diff 평균을 이용해서 평균보다 크면 'mean over' 아니면 'mean under' 
# diffmean
diffmean <- c()
for (i in 1:rows) {
  if ( stock.df$diff[i] > mean(stock.df$diff) ){
    stock.df$diffmean[i]<-"mean over"
  } else {
    stock.df$diffmean[i]<-"mean under"
  }
}
head(stock.df)

for(i in 2:9) {
  if(i == 2) {  
    cat('row i = ' , i , '\n')
    for(j in 1:9) {
      cat(i , '*' , j , '=' , (i*j) , "\t")
    }
    cat('\n')
  }
}

# while 구문
# 조건에 만족할 때 블록구문을 수행한다
idx <- 1
while(idx <= 10) {
  print(idx)
  idx = idx + 1 # 문장 마지막에 증감식을 필요로 한다
}

idx <- 1
while(idx <= 100) {
  if(idx %% 5 == 0) {
    cat(idx, '\t')
  }
  idx = idx + 1 
}

# break, next , repeat
idx <- 1
while(idx <= 10) {
  idx = idx + 1 
  print(idx)  
  if(idx %% 2 != 0) {
    next
  }
  
}

idx <- 1
repeat{
  print(idx)  
  if(idx >= 10 ) {
    break
  }
  idx <- idx + 1
}


# NA 확인방법 처리

is.na(c(1,2,3,4,NA))
sum(c(1,2,3,4,NA) , na.rm = T)

na.df <- data.frame(x = c(NA , 2, 3) , 
                    y = c(4, 5, NA))
sum(is.na(na.df))

install.packages('caret')
library(caret)

na.omit(c(1,2,3,4,NA))
na.pass(c(1,2,3,4,NA))
na.fail(c(1,2,3,4,NA))

data.na.vector <- c(2,3,NA,5,6,NA)
is.na(data.na.vector)
data.na.vector[ is.na(data.na.vector) ] <- median(data.na.vector , na.rm = T)
data.na.vector


# heatmap

iris.df <- iris

iris.df[4:10 , 3] <- NA
iris.df[1:5 , 4] <- NA
iris.df[60:70 , 5] <- NA
iris.df[97:103 , 5] <- NA
iris.df[133:138 , 5] <- NA
iris.df[140 , 3] <- NA

iris.df
?heatmap
heatmap( 1 * is.na(iris.df) , 
         Rowv = NA , 
         Colv = NA , 
         scale = 'none' , 
         cexCol = .8 ) 


# 함수
# 코드이 재활용성이 좋아진다
# function

user.function <- function() {
  print('no input and no return')
}
user.function()

user.function <- function(x) {
  print('input and no return')
  print(x)
}
user.function(1)

user.function <- function(x , y) {
  print('input and return')
  return (x+y)
}
user.function(10, 5)

result <- user.function(10, 5)
result 

user.function <- function() {
  print('no input and return')
  return ('맛점하세요~~')
}
result <- user.function()
result 

# 선언
new.user.func <- function(x, y) {
  cat("x = " , x , '\n')
  cat("y = " , y , '\n')
  result <- x + y
  return (result)
}

# 호출
result.sum <- new.user.func(y=5, x=10)
result.sum

new.user.func <- function(...) {
  args <- list(...)
  for(idx in args) {
    print(idx)
  }
}

new.user.func(1, 2 , 3)

iris.df
sum(is.na(iris.df)) / length(iris.df) * 100


# 결측치 비율을 계산하는 함수를 정의
# 행 및 열별로 비율을 계산

naMissFunc <- function(df) {
  sum(is.na(df)) / length(df)  * 100
}

rowMissPer <- apply(iris.df , 1 , naMissFunc)
colMissPer <- apply(iris.df , 2 , naMissFunc)

barplot(colMissPer)


# 조작함수
# cbind() , rbind() , 
# merge() == join 
tmp.df01 <- data.frame(name = c('임정섭', '임은결' , '임재원') , 
                       math = c(100, 60, 100))

tmp.df02 <- data.frame(name = c('임재원', '임은결' , '임정섭') , 
                       eng  = c(95, 80, 100))

tmp.df01
tmp.df02

cbind(tmp.df01 , tmp.df02)
merge(tmp.df01 , tmp.df02)


# mapply
# 다수의 인자를 함수에 넘겨줄 때 
?mapply

mapply( function(i , s) {
          sprintf("%d , %s" , i, s)
        } , 
        1:3 , 
        c('a' , 'b' , 'c') )

iris
apply(iris[-5] , 2 , mean)
mapply(mean , iris[1:4])



# doBy package
# summaryBy , orderBy , splitBy , sampleBy
install.packages("doBy")
library(doBy)

summary(iris)

# 수치형 자료의 분포를 확인하는 함수는 quantile()
quantile(iris$Sepal.Length)
quantile(iris$Sepal.Length , seq(0, 1, by=0.1))

?summaryBy
# 원하는 컬럼의 값을 특정 조건에 따라 요약할 때 사용
summaryBy(. ~ Species , iris) 

?orderBy
orderBy(~Species , iris) 
orderBy(~Species + Sepal.Width , iris) 

#base package

# install.packages("base")
# library(doBy)

order(iris$Sepal.Length)
iris[order(iris$Sepal.Length) , ]

# sample()

sample(1:10 , 5 , replace = T) 
sample(NROW(iris) , NROW(iris))

iris[ sample(NROW(iris) , NROW(iris)) , ] 


library(doBy)

?sampleBy
test.sample <- sampleBy( ~ Species , frac=0.1 , data=iris)


# split()
class( split(iris , iris$Species) )
class( split(iris$Sepal.Length , iris$Species) )
class( lapply( split(iris$Sepal.Length , iris$Species)  , mean) )

irisVec <- unlist(lapply( split(iris$Sepal.Length , iris$Species)  , mean))
irisVec

irisMat <- matrix(irisVec , ncol=3 , byrow = T)
irisMat

irisFrm <- data.frame(irisMat)
irisFrm

names(irisFrm) <- c('s_mean' , 'color_mean' , 'nica_mean')
irisFrm

# subset()

iris.setosa.df <-subset(iris , Species == 'setosa')
iris.setosa.df

iris.setosa.df <-subset(iris , Species == 'setosa' & Sepal.Length > 5.0)
iris.setosa.df

iris.setosa.df <-subset(iris , Species == 'setosa' & Sepal.Length > 5.0 , select = c(Sepal.Length))
iris.setosa.df

iris.setosa.df <-subset(iris , Species == 'setosa' & Sepal.Length > 5.0 , select = -c(Sepal.Length))
iris.setosa.df


# order() , sort() , which() , which.max() , which.min()
x <- c(20, 11, 33, 50, 47)
x
sort(x , decreasing = T)

order(x)
x[ order(x) ] 

order(iris$Sepal.Length)
head( iris[ order(iris$Sepal.Length , iris$Petal.Length) , ] )

      
x <- c(2,4,6,7,10)
x
which(x %% 2 == 0)
which.min(x)
which.max(x)

x[which.min(x)]
x[which.max(x)]






















































































































