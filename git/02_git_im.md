

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



