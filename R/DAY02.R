txtVec <- c("BigData" , "Bigdata" , "bigdata" , "Data" , "dataMining" , "class1" , "class2")
txtVec

# nchar() : character 개수 반환
nchar(txtVec)


#package 설치 아래 명령어가 실행되지 않으므로
#패키지가 꼬이면 삭제할 줄도 알아야 하므로 
#
remove.packages("stringr")

install.packages("stringr")
library("stringr")

str_length(txtVec)

?substr
?strsplit

greetingMsg <- "hi , higdata is very important"
substr(greetingMsg , 5, 11)
class(strsplit(greetingMsg, ","))

?str_extract

str_extract("abc123def456" , "[0-9]{3}")
str_extract_all("abc123def456" , "[0-9]{3}")

str_extract("abc123def456" , "[a-zA-Z]{3}")
str_extract_all("abc123def456" , "[a-zA-Z]{3}")


gsub("[0-9]" , "" , "abc123def456")


stringDumy <- "임정섭jslim49섭서seop34강봉진곶ㅅ우리낭룬알"

str_extract_all(stringDumy , "[a-zA-Z]{3,5}")

# 문제01) 연속된 한글 3자 이상을 추출한다면?
str_extract_all(stringDumy , "[가-힣]{3,}")
class(str_extract_all(stringDumy , "[가-힣]{3,}"))

# 문제02) 나이추출
str_extract_all(stringDumy , "[0-9]{2,}")

# 문제03) 숫자를 제외하고 추출
gsub("[0-9" , "" , stringDumy)
str_extract_all(stringDumy , "[^0-9]")
str_extract_all(stringDumy , "[^0-9]+")
str_extract_all(stringDumy , "[^0-9]{3,}")

# 문제04) 영문자를 제외한 한글이름만
str_extract_all(stringDumy , '[^a-z]+')



# 메타문자
# 단어 \\w
# 숫자 \\d
# 엔터키 \n , 탭키 \t
 
ssn <- "123456-1234567"
str_extract_all(ssn , '[0-9]{6}-[1-4][0-9]{6}')
str_extract_all(ssn , '\\d{6}-[1-4]\\d{6}')

email <- "seungyoon1909@gmail.com"
str_extract_all(email , '\\w{9,}@\\w{3,}.[a-z]{2,}')

strMsg <- "우리는 달려간다 ~ 이상한 나라로 ~김승윤이 잡혀있는 마왕의 소굴로~"
length(strMsg)
str_length(strMsg)
#문자열의 위치
str_locate_all(strMsg , '승윤')
str_replace_all(strMsg , '승윤' , '윤윤윤')

str_sub(strMsg , start = 5 , end = 8)

#특수문자제외($ , ,)
num <- "$123,466"

str_replace_all(num , "\\$|\\," , "")
str_replace_all(num, "\\$|\\,", "")

#변환함수 as.

tmp <- str_replace_all(num , "\\$|\\," , "" )
class(tmp)
digt <- as.numeric(tmp)
digt

# 행렬(maatrix)
# matrix()  rbind()  cbind()
# apply()

# 생성
var01 <- matrix(c(1:5))
class(var01)
nrow(var01)

var02 <- matrix(c(1:10) , nrow=2 , byrow = T)
var02

var03 <- matrix(c(1:9) , nrow = 3 , ncol = 3) 
var03

var04 <- matrix(x, 2, 3)
var04

t(var04)

row(var04)
col(var04)


#데이터 접근 [행인덱스 , 열 인덱스]
class(var04[1,1])

var04[2,3]

var05 = matrix(c(1:9) , 3, 3)


# 1,2행의 2열의 성분만 출력
var03[c(1:2) , 2]
class(var03[c(1:2) , 2])
typeof(var03[c(1:2) , 2])
mode(var03[c(1:2) , 2])

var03[2 , c(1:2)]

# 1행을 제외하고 1,3열의 정보만 추출

var05[-1 , c(T,F,T)]
var05[c(2:3), c(1:3)] 


# 1,3 열을 제외한 행렬을 만든다면?

var05[   , -c(1,3)]
class(var05[   , -c(1,3)])

  #드랍을 할건데 2만 드랍하지마 라는 뜻
var05[, 2, drop=F]
class(var05[, 2, drop=F])

x <- rbind(c(1,2,3) , c(4,5,6))


x <- cbind(c(1,2,3) , c(4,5,6))

x <- rbind(1:3 , c(4,5,6) , 7:9)
x

x[c(1:2), ]
x[-3 , ]


yookMat <- matrix(c(1,2,3,4,5,6,7,8,9) , nrow = 3 , dimnames = list(c("row01", "row02", "row03") , c("cow01", "cow02", "cow03")))
yookMat

# 행의 이름과 열의 이름을 이용하여 조회가 가능하다

yookMat["row01" ,]

yookMat * 2
yookMat / 2
yookMat + 2
yookMat - 2

mat01 = matrix(c(1,2,3,4,5,6,7,8,9) , nrow = 3)
mat02 = matrix(c(1,2,3,4,5,6,7,8,9) , ncol = 3)

mat01 * mat02 #값의 곱
mat01 %*% mat02 #행렬곱


# 행렬의 연산에서는 앞 행열의 열의 숫자와 뒤 행열의 행의 숫자가 같아야한다.
# 3*3 , 2*3
mat01%*%mat02


# apply(data, 방향, 함수)
#vector or matrix를 data로 받아 임의의 함수를 적용한 결과를 얻는 것
#방향: 1->행, 2->열
#함수 sum, mean, user_def function도 가능
?apply

mat01
apply(mat01, 1, sum)
class(apply(mat01, 1, sum))


iris
class(iris)

# 각 열(species 제외한)에 대한 합과 평균, 중위수

apply(iris[ , 1:4] , 2 , sum)
apply(iris[ , 1:4] , 2 , mean)
apply(iris[ , -5] , 2 , median)

# rowSum() , colSums() rowMean()  colMeans()

colSums(iris[, -5])


#order() 정렬
?order

order(iris[ , 1] , decreasing = T)

iris[ order(iris[,1] , decreasing = T) , ]

?data.frame
exDF <- data.frame(x = c(1,2,3,4,5) , y = c("a", "b","c","d","e"))
exDF = data.frame(x = c(1,2,3,4,5) , y = c("a", "b","c","d","e"))
exDF


#특정행 가져오기
exDF[c(T,F,T,F,T),]

exDF[ exDF[,1] %%2 == 0 ,]
exDF[ exDF[,"x"]%%2==0,]
exDF[ exDF$x %% 2 ==0 ,]


#베얄
#array() , dim(c())
(m <- matrix(1:12 , ncol =4))
class(m)
ary <- array(1:12 , dim = c(3,4))
ary
#c(2,2,3) 2행 2열 짜리 배열의 3개의 레이어를 가지고 있다.
ary <- array(1:12 , dim = c(2,2,3))
ary
ary[1,1,1]

apply(ary , c(1,2) , mean)

iris3

dim(iris3)
mode(iris3)
class(iris3)
iris3[,,1]

#lapply() 반환형자체가 리스트와 키밸류 형식으로 나온다, 
#sapply() 리스트 밸류만을 반환   

tmpList <-list(name='jslim' , height = 186)
tmpList
tmpList$name
tmpList$height
mode(tmpList)
class(tmpList)

#list 타입의 경우 구조를 확인 할 경우
str(tmpList)

tmpList <- list(1:4 , rep(3:5) , "dog")
tmpList


newlist <- c(list(1,2, tmpList) , c(3,4))
class(newlist)
overlist <- list(a = list(c(1,2,3)),
            b=list(c(1,2,3,4)))

overlist

overlist$a[1]
overlist$b[1]


userInfo <- list(name = 'hinpyo',
                 address = '신논현',
                 tel = '010-3333-2333',
                 age = 18,
                 marriage = F)
userInfo
str(userInfo)

userInfo[1]
class(userInfo[1])
userInfo$name
class(userInfo$name)