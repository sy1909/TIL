# 변수의 데이터 타입
# scalar
var.scalar = 100  # 단일값을 담는게 스칼라
var.scalar

#vector
var.vector <-c()
var.vector = c(1,2,3)
var.vector

#matrix
var.matrix = matrix(1:4 , nrow = 2 , ncol = 2)
var.matrix %*% var.matrix  # 행렬곱

#array
var.array = array(1:8 , dim=c(2,2,2))
var.array

#list
userInfo <- list(name = c('hinpyo', '입성') , 
                    
                 address = c('신논현', 'seoul') ,
                 tel = c('010-3333-2333', '010-3292-2232') ,
                 age = c(18,30) ,
                 marriage = c(F,T) )
userInfo$name
userInfo$name[1]
userInfo$name[2]

userInfo$age[1] <- 30
userInfo$age

#새로운 키,값을 추가한다면?
userInfo$id <- c("jslim " , "parksu")
userInfo
str(userInfo)


#key 제거
userInfo$id <- NULL
str(userInfo)

#서로다른 자료구조 (veector , matrix , array)
lst01 <- list(one = c("one" , "two" , "three"),
              two = matrix(1:9 , nrow = 3),
              three = array(1:12 , dim = c(2,3,2))
              )
str(lst01)
lst01$one
lst01$two[2,2]
lst01$three

lst02 <- list(1:5)
lst02[[1]][4]

#list -> vector
#vector -> list
# 형변환 as.

as.vector(lst02) # 형변환
class(as.vector(lst02))

lst03 <- unlist(lst02)
lst03
class(lst03)
#리스트 여기까지

# lapply , sapply 처리함수
?lapply

lst04 <- list(1:5)
lst05 <- list(6:10)

lapply( c(lst04, lst05) , max) # 리턴 받는 형식이 s 와 다르다
sapply(x = c(lst04, lst05) , FUN = sum) # 값만 보여준다.

result <- sapply(1:3 , function(x){x*2})
result

unlist(result)
class(result)


# data.frame
# vector 를 이용한 방법
?data.frame
id     <- c(100 , 200 , 300)
name   <- c("abc" , "abc" , "abc")
salary <- c(1000000 , 2000000 , 3000000)

exDF <- data.frame(id , name , salary)
exDF$id

#matrix 를 이용한 방법
matrix
matDF <- matrix(data = c(1,"abc" , 150, 2,"abc" , 50 , 3 , "rlatmd" , 150) 
                ,nrow = 3 ,
                byrow = T)

#위 처럼 데이터를 입력하면 벡터 하나 안에서 가장 큰 형식으로 형변환이 된다 
# 그래서 1,2,3 이 string (char) 형식으로 변환된다. 문자열이 제일 크므로
matDF
matDF <- data.frame(matDF)
matDF

sampleDF <- data.frame(x = c(1,2,3,4,5),
                       y = c(2,4,6,8,10))
sampleDF
sampleDF$x
sampleDF$y
sampleDF[1, ]#행의 값
sampleDF[1]#열의 값

sampleDF[c(1,3) , 2]
sampleDF[-1] # 첫번째 열을 제외한 모든 열
sampleDF[-1,] # 첫번째 행을 제외한 모든 행

sampleDF[-1 , c('x' , 'y')]
sampleDF[-1 , "x"]

#vector 리턴을 data.frame 형식으로 반환받기를 원한다면
class(sampleDF[-1 , c("x")])
sampleDF[-1 , c("x") , drop = F] #일차원으로 리턴되는 값도 데이터프레임을 유지하고 싶다
#drop을 쓰면된다

str(sampleDF)
head(sampleDF)

#rownames() , colnames()

sampleDF <- data.frame(1:3)
sampleDF

colnames(sampleDF) <- c('feature01')
rownames(sampleDF) <- c('idx01', 'idx02', 'idx03')

names(sampleDF)
sampleDF
class(names(sampleDF))

#문자열이 인수일 경우 문제가 생긴다.

tmp.students <- c('john' , 'jdfa' ,'johnd', 'dfd')
tmp.score <- c(76 , 82 , 84 , 67)
tmp.grade <- c('c' , 'B' ,'B' , 'D')

tmp.class.df <- data.frame(tmp.students , tmp.score , tmp.grade )
tmp.class.df

#행의 갯수 nrow() 및 열갯수 ncol() 확인하고 싶으면
ncol(tmp.class.df)
nrow(tmp.class.df)
names(tmp.class.df)

# 행의 이름을 변경?
rownames(tmp.class.df) <- c('idx01', 'idx02', 'idx03', 'idx04')
tmp.class.df

#열 , 행 추가 할 때
#cbind() , rbind()
tmp.id <- c("100","200","200","200") #이거만 했을때 tmp.class.df 에는 추가가 안된다
tmp.class.df <-cbind(tmp.class.df #원래 잇던 거에 아래 추가된 내용 입력
                     ,tmp.id)
tmp.class.df


tmp.class.df <-rbind(tmp.class.df , c('ksy' , 100 , 'a' , '500'))
tmp.class.df

rownames(tmp.class.df) <- c('idx01', 'idx02', 'idx03', 'idx04' , 'idx05')

# factor

tmp.factor <- c('a' , 'o' , 'ab' , 'b' , 'a' , 'o' , 'a')
tmp.factor

blood.factor <- factor(tmp.factor)
blood.factor

class(blood.factor)
nlevels(blood.factor) #요소의 개수  중복제거같은거
levels(blood.factor) # 요소의 종류
is.factor(blood.factor)
ordered(blood.factor) # 요소들의 순서 가나다 순서인가?

# 빈도수 구할 때 사용하는 함수
table()
table(blood.factor)
plot(blood.factor)


id <- c(1,2,3,4,5,6,7,8,9,10)
gender <- c("f","f","f","f","m","m","m","m","m","m")
age <- c(20,10,13,15,20,23,26,29,30,40)
area <- c('서울' , '경기' , '경기', '제주', '대전', '서울', '경기', '인천', '인천', '대구')

tmp.df <- data.frame(id , gender , age, area )
tmp.df

class(tmp.df$gender)
#class(tmp.df[2])
#class(unlist(lapply( tmp.df[2], as.character)))
#gender.factor <- unlist(lapply( tmp.df[2], as.character))
#gender1.factor <- as.factor(gender.factor)


gender.factor <- factor(tmp.df$gender)
gender.factor
is.factor(gender1.factor)
class(gender.factor)

area.factor <- factor(tmp.df$area)
area.factor


table(gender.factor)
plot(gender.factor)
plot(area.factor)


tmp.df$gender <- factor(tmp.df$gender)
tmp.df$area <- factor(tmp.df$area)
str(tmp.df)


iris
levels(iris$Species)

mean(iris$Sepal.Length)
class(iris$Sepal.Length)

# with(dataset , 함수() | 표현식 ) , within()
# 데이터 프레임 또는 리스트내에 존재하는 필드를 손쉽게 접근하기 위한 함수
?with

iris
mean(iris$Sepal.Length)
mean(iris$Petal.Width)
# 위처럼 사용하는거 보다 with 를 사용하면 편하다

with( iris , { (mean(Sepal.Length))   
               (mean(Sepal.Width))} )

with(iris , { print(mean(Sepal.Length)) 
              print(mean(Sepal.Width)) } )

x <- data.frame(val= c(1,2,3,4,NA , 5,NA))
x

is.na(x$val)
mean(x$val , na.rm = T) # na.rm = T   na를 제외
median(x$val , na.rm = T)


x <- within(x , val <- ifelse(is.na(val) , mean(x$val , na.rm = T) , val))
x

x$val[is.na(x$val)] <- median(x$val , na.rm =T)
x

lapply(iris[ , -5] , mean)
sapply(iris[ , -5] , mean)

#vector -> data.frame(as.data.frame())
x <- sapply(iris[ , -5] , mean)
x
xx<-as.data.frame(t(x))
class(xx)

xx$Sepal.Length
sapply(iris , class)
str(iris)

iris
iris[1,1] = NA
head(iris)

#setosa종의 sepal.length의 평균을 구해서 NA가 있는 값을 대체한다면?

iris[1,1] = NA
iris[1,]

#학생 코드
tmp.mat<-iris
tmp.mat[1,1] <- NA
pos <- tmp.mat$'Species' == 'setosa' #true false 로 리턴
pos
tmp.mat$Sepal.Length[is.na(tmp.mat$Sepal.Length)] <- mean(tmp.mat$Sepal.Length[pos], na.rm=T)
tmp.mat
# 여기까지 학생 코드



?split
split(iris$Sepal.Length , iris$Species)  #Species 대로 분리 groupby 같은거

iris.sl.median <- sapply(split(iris$Sepal.Length , iris$Species) , median , na.rm = T)
iris.sl.median
class(iris.sl.median)
iris <- within(iris , 
               {
                 Sepal.Length <- ifelse(is.na(Sepal.Length), 
                                        iris.sl.median[Species],
                                        Sepal.Length)
                 })
head(iris)


#subset()
#data.frame 으로부터 조건만족하는 행을 추출하여 그걸 data.frame 으로 만든다.
x<-1:5
y<-6:10
?letters
z<-letters[1:5]

tmp.frm <- data.frame(x,y,z)
tmp.frm
tmp.frm.subset <- subset(tmp.frm , x>=3) 
tmp.frm.subset

tmp.frm.subset <- subset(tmp.frm , y<=8) 
tmp.frm.subset

tmp.frm.subset <- subset(tmp.frm , x>=2&y<=8) 
tmp.frm.subset

tmp.frm.subset <- subset(tmp.frm , select = c(x,y)) 
tmp.frm.subset

tmp.frm.subset <- subset(tmp.frm , y<=8, select = c(x,y)) 
tmp.frm.subset
class(tmp.frm.subset)

tmp.frm.subset <- subset(tmp.frm , y<=8, select = c(x) , drop = T) #vector로 바꾼다.
tmp.frm.subset
class(tmp.frm.subset)


iris
dim(iris)
str(iris)

# 1,3,5 칼럼을 대상으로 subset
# 3번 컬럼은 평균이상 선택

tmp = mean(iris$Petal.Length)
tmp
iris.subset <- subset(iris , 
                      select = c(Sepal.Length , 
                                 Petal.Length, 
                                 Species) , 
                      Petal.Length >= mean(iris$Petal.Length))
iris.subset



# 연습문제
# 1. 4,6,5,7,10,9,4,15를 R의 숫자형 벡터 x로 만드세요.
x <- c(4,6,5,7,10,9,4,15)
x
str(x)
class(x)
      

# 2. 아래의 두 벡터의 계산 결과는?
x1 = c(3,5,6,8)
x2 = c(3,3,3)

x1+x2
x1/x2
x1*x2
x1/x2
x1%%x2 #나머지
x1%/%x2 #몫
x1^x2



# 3. Data Frame과 subset을 이용하여 다음의 결과를 도출하세요
Age <- c(22, 25, 18, 20)
Name <- c("James", "Mathew", "Olivia", "Stella")
Gender <- c("M", "M", "F", "F")

##   Age   Name Gender
## 1  22  James      M
## 2  25 Mathew      M

# 4. 아래의 R코드를 실행한 결과는?
x <- c(2, 4, 6, 8)
y <- c(TRUE, TRUE, FALSE, TRUE)
sum(x[y])

# 5. 아래의 벡터에서 결측치의 수를 구하는 R코드를 작성하세요
x <- c(34, 56, 55, 87, NA, 4, 77, NA, 21, NA, 39)


# 6. 아래 두 벡터를 결합하는 코드이다. 결과는?
a=c(1,2,4,5,6)
b=c(3,2,4,1,9)
cbind(a,b)

# 7. 아래 두 벡터를 결합하는 코드이다. 결과는?
a=c(10,2,4,15)
b=c(3,12,4,11)
rbind(a,b)

# 9. 아래 R 코드의 결과는?
x=c(1:12)
length(x)


# 10. 아래 R 코드의 결과는?
x=c('blue',10,'green',20)
is.character(x)  


# 11. 아래의 세개의 벡터를 이용하여 아래의 결과가 나오도록 리스트(Date)를 만들어라.
year=c(2005:2016)
month=c(1:12)
day=c(1:31)

# Date
# $year
#  [1] 2005 2006 2007 2008 2009 2010 2011 2012 2013 2014 2015 2016
# $month
#  [1] 1 2 3 4 5 6 7 8 9 10 11 12
# $day
#  [1] 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31


# 12. 아래의 행렬계산 결과는?
M=matrix(c(1:9),3,3,byrow=T)
N=matrix(c(1:9),3,3)

M%*%N

# 14. 아래의 데이터를 데이터프레임(Department)으로 만들어라.
#DepartmentID	DepartmentName
#31	          영업부
#33	          기술부
#34	          사무부
#35	          마케팅































