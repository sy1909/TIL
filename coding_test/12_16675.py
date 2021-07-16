#https://www.acmicpc.net/problem/16675
#두개의 손

ML , MR , TL , TR = ('SPR'.index(i) for i in input().split())
#SPR의 스트링에서 해당하는 스펠링이 있을경우 그 위치를 반환한다.
# 위치를 쓰는 이유는 그 위치의 +2 해서 %2한 값은 서로 먹고 먹히는 관계이기 떄문
#print(ML , MR , TL , TR)

if ML == MR and (ML+2)%3 in [TL, TR]:
    print("TK")
elif TL == TR and(TL+2)%3 in [ML , MR]:
    print("MS")
else:
    print('?')

#무조건 이기고 지는 경우의수는 같은걸 내고 상대에게 내가 지는 가위바위보가 있을경우