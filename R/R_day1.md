# R_day1

빅데이터 분석을 위한 R 교육 day1



## 코드와 주석

```R
# 주석

# Package = 함수(func) + 데이터 셋
# install.packages('패키지명')
# library('패키지명')

# 디버깅용 함수 print(), sprintf(), paste(), cat()
# ?print 블럭 시키고 실행(ctrl+enter), 함수의 구문형식 출력

?print

?letters #내장되어있는 상수
letters
print(letters)
print(LETTERS)
month.abb
month.name
#console 창에 [숫자]는 인덱스임, 몇 번째 문자인지

print('Hi')
print('Sup~~')

?sprintf
# %d: 인수 정수로
# %s: 인수 문자열로
# %f: 인수 실수로
sprintf("Number: %f, String1: %s String2: %s", 123, "hi", 'hello')

?paste
print('a', "b", 'c') #여러개 print 불가
paste('a', 'b', 'c', sep='-')


myFunc <- function() {
  total <- 0
  cat('appen ...') #개행이 안 되는 print
  for(i in 1:10) {
    total <- total + i
    cat(i, "...")
  }
  cat("End!!", "\n")
  return (total)
}
myFunc()


# 변수이름은 문자나 .으로 시작해야 함
# 스칼라 값
# 단일행 변수: vector, matrix, array
# 복수형 변수: list, data.frame         type을 섞어서

# vector(정수, 실수, 문자, 논리)
# c()  - 줄여서 표현
sampleVec <- c(1,2,3,4,5)
sampleVec
sampleVec <- c(1,2,3,4,"5", TRUE)
sampleVec

# 변수 선언방식
# snake 형: sample_vec
# cammel 형: sampleVec

2x <- c(0,1,4,9,16) #숫자로 시작하면 안됨
x <- c(0,1,4,9,16)
x
avg <- sum(x)/length(x)
avg
mean(x)
x <- 1:10
x
y <- x^2
y
plot(x,y) #시각화
cor(x,y) #상관계수

# 변수의 data type 확인 typeof(), mode()
typeof(X)
ex_vec <- c(TRUE, FALSE, TRUE, FALSE)
typeof(ex_vec)
mode(ex_vec)
str(str_vec) #데이터 타입 + 개수

sample_na <- NA #결측값1
sample_null <- NULL #결측값2
is.na(sample_na)
is.null(sample_null)

#vector 중첩가능
over_vec <- c(1,2,3, c(1,2,3))
over_vec
typeof(over_vec) #double 실수형 #디테일한 출력
mode(over_vec) #numeric 수치형
str(over_vec) #num [1:6]
class(over_vec) #numeric

#수치형 vector 만들기 start:end
x <- 1:10 #c() 안 써도

#반복
?rep
#설명에 ... 돼 있는건 가변인자로 0~n 개까지 쓸 수 있는거
rep(1:5, 5)
rep(1:5, each=5)

#시퀀스
?seq
seq(1, 10, 2)
seq(1, 10, length.out = 3) #3개를 출력하되 간격 알아서 결정

sample_seq <- seq(1, 100, by = 3)
sample_seq

length(sample_seq)

#인덱싱
sample_seq[1]
sample_seq[length(sample_seq)-4]

# 벡터의 각 셀에 이름을 부여할 수 있다.
x <- c(1,3,5)
col <- c('feature01' , 'feature02' , 'feature03')
names(x) <- col
x['feature01']
x[c(1,3)]
x[c('feature01' , 'feature03')]
names(x)[3]

# 음수 인덱스를 사용해 특정 요소만 제외할 수 있다.
x[-2]
x[c(-1,-3)]

#길이 length() , nrow() , NROW()
length(x)
nrow(x)
NROW(x)

# 벡터의 연산 %in% - 어떤 값이 벡터에 포함되어있는지를 알려주는 연산자
a_vec <- 'A' %in% c('a' , 'b' , 'c')
a_vec

#setdiff() 합집합 , union() intersect()
setdiff(c("a" , "b" , "c") , c('a' , 'b'))
union(c("a" , "b" , "c") , c('a' , 'b'))
intersect(c("a" , "b" , "c") , c('a' , 'b'))

setequal(c("a" , "b" , "c") , c('a' , 'b'))
setequal(c("a" , "b" , "c") , c('a' , 'b', 'd'))



#100에서 200으로 구성된 벡터 sample_vec 생성 후 문제풀기
#eX01. 인덱스가 10번째인 값 출력
#ex02. 끝에서 10개의 값을 잘라내어 출력
#ex03. 홀수만 출력
#ex04. 3의 배수만 출력 (%% 나머지 연산자)
#ex05. 앞에서 20개의 값을 잘라내어 변수 d.20에 저장/출력
#ex06. d.20의 5번째 값을 제외한 나머지 값 출력
#ex07. d.20의 5,7,9 번째 값을 제외한 나머지 값 출력

samplevec <- c(100:200)
samplevec
#1.
samplevec[10]
#2.
tail(samplevec , 10)
#3,
samplevec[samplevec%%2 ==1]
#4.
samplevec[samplevec%%3 == 0]
#5.
d.20 <- head(samplevec , 20)
d.20
#6.
head(samplevec)
d.20[-5]
#7.
d.20[c(-5 , -7, -9)]

?month.name
absent <- c(10, 8 , 14, 15, 9, 10, 15, 12, 9, 7, 8, 7)
names(absent) <- month.name
absent

#5월 의 결석생 수를 출력하시오
absent[5]
absent['May']

# 7월 9월 의 결석생 수의 합계를 출력하시오
absent[c('May' , 'September')]

#상반기 의 결석생수의 합계
sum(absent[c(1:6)])

#하반기 의 결석생수의 평균
mean(absent[c(7:12)])


#문자형 벡터
c('a' , "b", "c" , 'd' , "e")
strVec <- c("H" , "S" , "T" , "N" , "O")
strVec[3] > strVec[5]

paste("May I" , "help u?")

month.abb
paste(month.abb , 1:12)

paste(month.abb , 1:12 , c("st" , "nd" , "rd" , rep("th" , 9)))

paste("/user" , "local" , "bin" , sep = "/")
paste("/user" , "local" , "bin" , sep = "")

?grep

strvec <- c("gender" , "height" , "age" , "weight" , "eight")
# ei로 시작하는 값을 추출한다면
grep("^ei" , strvec , value = T)
grep("^EI" , strvec , value = T)
grep("^EI" , strvec , value = T , ignore.case = T)

grep("+ei+" , strvec , value = T)

strvec[grep('ei' , strvec)]

txtVec <- c("BigData" , "Bigdata" , "bigdata" , "Data" , "dataMining" , "class1" , "class2")
txtVec

#시작문자를 지정 ^
# + 1 or more
# 소문자 b로 시작하는 데이터를 추출한다면?

grep('^b+' , txtVec ,  value = T)
grep('^b+' , txtVec ,  value = T , ignore.case = T)

# big 문자열이 있는 요소를 찾아 해당 문자열을 bigger 라는 단어로 바꾼다면?

?gsub
gsub('+big+' , "bigger" , txtVec , ignore.case = T)

#숫자를 제거하고 싶다면?
gsub("[0-9]" , "" , txtVec)
gsub("[[:digit:]]" , "" , txtVec)


# [정규표현식(regular expression)]

# *  0 or more.
# +  1 or more.
# ?  0 or 1.
# .  무엇이든 한 글자를 의미
# ^  시작 문자 지정 
# ex) ^[abc] abc중 한 단어 포함한 것으로 시작
# [^] 해당 문자를 제외한 모든 것 ex) [^abc] a,b,c 는 빼고
# $  끝 문자 지정
# [a-z] 알파벳 소문자 중 1개
# [A-Z] 알파벳 대문자 중 1개
# [0-9] 모든 숫자 중 1개
# [a-zA-Z] 모든 알파벳 중 1개
# [가-힣] 모든 한글 중 1개
# [^가-힣] 모든 한글을 제외한 모든 것
# [:punct:] 구두점 문자, ! " # $ % & ’ ( ) * + , - . / : ; < = > ? @ [ ] ^ _ ` { | } ~.
# [:alpha:] 알파벳 대소문자, 동등한 표현 [A-z]
# [:lower:] 영문 소문자, 동등한 표현 [a-z]
# [:upper:] 영문 대문자, 동등한 표현 [A-Z].
# [:digit:] 숫자, 0,1,2,3,4,5,6,7,8,9,
# [:xdigit:] 16진수  [0-9A-Fa-f]
# [:alnum:] 알파벳 숫자 문자, 동등한 표현[A-z0-9].
# [:cntrl:] \n, \r 같은 제어문자, 동등한 표현[\x00-\x1F\x7F].
# [:graph:] 그래픽 (사람이 읽을 수 있는) 문자, 동등한 표현
# [:print:] 출력가능한 문자, 동등한 표현
# [:space:] 공백 문자: 탭, 개행문자, 수직탭, 공백, 복귀문자, 서식이송
# [:blank:] 간격 문자, 즉 스페이스와 탭.






























```

















