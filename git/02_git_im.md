

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





# Git Intermediate

git의 중급과정



## -gitignore

1 repo 당 한개(이상)의 `.gitignore`필요 (readme.md 도 마찬가지)

git이 관리하길 원치 않는 파일들을 정리한 파일

https://www.toptal.com/developers/gitignore

로 접속하여 원하는 내용을 적고 (사용하는 언어라던가 환경등)







## Local Branching

브랜치를 만들게 (따게) 되면 , 현재 브랜치의 모든 상황을 복사하여 평행세계를 만든다.



### create branch

```
# 브랜치 생성
$ git branch <new-branch-name>

# 브랜치 목록 확인
$ git branch

# 브랜치 이동
$ git switch <branch-name>

# 완성된 브랜치 결과물에 마스터가 가리키게 한다 (병합)
$ git merge aaa

```

```
# 브랜치 생성 후 이동
$ git switch -c <new-branch-name>
```



## delete branch

```
# merge 완료한 브랜치 완전삭제
$ git branch -d <branch-name>

# merge 미완료된 브랜치 강제 삭제
$ git branch -b <branch-name>
```





## merge

### 1. Fast Forwarding(꽃길)

혼자 일 할 경우 

```
(master)
$ git branch aaa
(master)
$ git switch aaa

(aaa)
$ 

# ... 수정 수정

(aaa)
$ git add .
$ git commit -m 'aaa1'
$ git switch master

(amster)
$ git merge aaa
```



### 2. Confilict - Auto merge(충돌 & 자동병합)

	1. `a` 브랜치 수정
 	2. `master`브랜치 수정
 	3. `(master) $ git merge a`
 	4. 운이좋아 두 커밋이 겹치지 않음
 	5.  자동으로 merge완료



### 3. Conflict - Manual merge(충돌& 수동병합)

1. a 브랜치에서 커밋
2. `master` 브랜치에서 커밋
3. `(master) $ git merge a`
4. 두 커밋이 겹치는 구간이 있음
5. 수동으로 충돌 해결 후 저장
6. 직접 `git add` , `git commit`



## Remote Branching

1. 조장이 리모트 생성
   1. `README.md` , `.gitignore` 생성하여 리포 생성
   2. settings > manage access 에서 팀원 추가
2. 모든 팀원이

## 협업 Collaborating

