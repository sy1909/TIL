# 마크다운 배우기 / MD배우기

개발자의 문서양식 마크다운(markdown을 배웁니다)



## 제목

'#' 의 개수에 따라 제목의 중요도가 달라져요

h1 => 문서에서 가장 큰 제목

문서에 h1 과 h3만 있다 => 문서 잘못 작성



## 본문

본문은 그냥 적으면 본문이에요



## 리스트



### 순서있는 리스트

1. 식용유를 두른다
2. 파를 넣고 파기름을 낸다
3. 계란을 풀어서 익힌다
4. 간장을 볶는다

### 순서없는 리스트

- cli학습
- git복습
- md작성 익숙해지기



## 인라인 코드(`)

`파일` 을 생성하기 위해서 `touch` 명령어를 사용한다.

`cd`를 통해 폴더간 이동을 한다.



## 볼드코드(**)

이것은 **굵어** 질거야





## 코드블럭(''')

```
$ 얼아
$ 뭐 이런거
```



## 표

cli 단축키

| 단축키 | 설명 |
| ------ | ---- |
|        |      |
|        |      |
|        |      |

| ---  | ---  | ---  |
| ---- | ---- | ---- |
|      |      |      |



## 수식 ($$)

$$
x = {-b \pm \sqrt{b^2-4ac} \over 2a}
$$













## git

git 의 기초를 배운다



- ***```git init```*** 
  - 폴더를 업그레이드한다
  - 기능이 추가된 폴더 어떤기능? 추가기능을 설치한 것
  - 저장소 혹은 repo(리포) 라고 부를 것이다.
  - 절대로 홈에서 이 명령어를 써서는 아니된다.
- **```rm -rf .git```**
  - 저장소를 일반 디렉토리로 되돌리기
- ***```git status```***
  - 현재 깃의 상태 커밋이 되어있고 안되어 있고등
  - 빨간색으로 표시되는 파일은 commit에 포함되지 않음
  - 초록색으로 표시되는 파일은 commit에 포함됨
  - 변경사항이 없는 파일은 표시되지 않음
- ***```git add file```***
  - 깃에 새로 생성된 파일을 정상 추가하는 명령어
  - (분장실에서 스테이지로 올린다)
- **```git add .```**
  - 폴더 전체중에 수정사항이 있는 파일만 가져와서 추가한다.
- **```git commit -m 'first commit'```**
  - 커밋하기위한 명령어 와 메세지
  - (스테이지에서 사진으로 찍는다/ 스냅샷 저장)
- **```git commit```**
  - 엔터치면 메세지 적는 vim으로 넘어간다. 맨위에 변경메세지 적는다.
- **```git config --global user.name ' ```'**
  - 사용자 이름 이메일
- **```git config --global user.email '```** '
- **```git log```**
  - 어떤 깃 로그가 있었나 커밋







## 스테이지에 올려야해요 = > git add

## 사진이 남았느냐가 중요해요 commit을 했느냐 안했느냐











## GIT 두번째강의



```git remote add name url```

```gir remote -v```

```git remote remove```


```git config --global user.name 'github username'```

```
$ git remote rename <old-name> <new-name>
```

## 리모트에 PUSH 하기

```
# 리모트에 업로드
$ git push <name> <branch>
```

## 리모트에서 PULL 하기

```
# 리모트에서 다운로드
$ git pull origin master 
```

## 리모트에서 최종 CLONE 받기

```
$ git clone <url> 
$ ex) git clone https://github.com/sy1909/TIL.git (url)
```

## 강의장 <=> 집 공부/프로젝트 시나리오

> 앉을 때 PULL, 일어설 때 PUSH
>
> Sit pull, Stand push

1. 집에서 기상
2. 강의장 도착
   1. `pull`
3. 공부/TIL 정리
   1. `commit`
4. 강의 종료
   1. `commit`
   2. `push`
5. 집 도착
6. 복습
   1. (처음이라면) `clone`
   2. `pull`
   3. `commit`
7. 복습 끝
   1. `commit`
   2. `push`
8. 잠
9. 1번으로 이동







