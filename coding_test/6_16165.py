#https://www.acmicpc.net/problem/16165
#걸그룹 마스터 준석이

N, M = map(int , input().split())
# N 걸그룹의 수 M 맞혀야할 문제의 수

member , mem_team = {} , {}
#멤버의 팀도 말해야하고 멤버가 속한 팀의 멤버도 말해야 하므로 딕셔너리 두개 생성

for i in range(N):
    team_name , team_num = input() , int(input())
    member[team_name] = []
    for j in range(team_num):
        name = input()
        member[team_name].append(name)
        mem_team[name] = team_name

for i in range(M):
    name , q  = input() , int(input())
    if q: # 1은 true 0은 false 이므로 이런식으로 사용 가능
        print(mem_team[name])
    else:
        for mem in sorted(member[name]):
            print(mem)

