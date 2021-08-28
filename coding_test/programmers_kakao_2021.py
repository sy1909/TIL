import re # 정규표현식 라이브러리
def solution(new_id):
    answer = ''
    #print(new_id)
    new_id = new_id.lower() # 소문자로
    #print(new_id)
    new_id = re.sub( r"[^a-z0-9-_.]" , "" , new_id  ) #영문자 숫자 - _ . 빼고 다 삭제
    #print(new_id)
    while '..' in new_id:
        new_id = new_id.replace('..' , '.') # 문자안에 .. 이 있으면 없어질때까지 반복
    #print(new_id , len(answer))
    if new_id[0] == '.' and len(new_id) > 1: # 빈문자열이 아니고 첫글자가 . 이면 .을 제외하고 나머지 문자열 반환
        new_id = new_id[1:]
    if new_id[-1] == '.': # 끝에도 마찬가지
        new_id = new_id[:-1]
    if not new_id: # 빈문자열이면 a를 채워넣는다
        new_id += 'a'
    #print(new_id)
    if len(new_id) >= 16: #글자수가 16을 넘어가면 15까지만
        new_id = new_id[:15]
    if new_id[-1] == '.': # 마지막글자가 .이면 제외
        new_id = new_id[:-1] 
    while len(new_id) <= 2: #글자수가 2보다 작다면 클때까지 마지막글자 반복
        new_id += new_id[-1]
    #print(new_id)
    answer = new_id
    return answer
'''
유저들의 아이디 생성
카카오 아이디 규칙에 맞지 않는 아이디 입력 -> 입력된 아이디와 유사하면서 규칙에 맞는 아이디 추천
길이 3 15 <=
소문자 숫자 - _ . 사용가능
. 는 처음과 끝에 사용X 연속X
'''
'''
# https://doorbw.tistory.com/127 정규표현식 관련
import re
def solution(new_id):
    st = new_id
    st = st.lower()
    st = re.sub('[^a-z0-9\-_.]', '', st) # [] 대괄호라는 문자클래스 안에서 ^가 사용되면 not 의 의미다
    st = re.sub('\.+', '.', st) # .이라는 문자가 1개이상 있을 경우 .으로 치환
    st = re.sub('^[.]|[.]$', '', st) # ^은 시작의 뜻 시작이 .이거나 끝이 .으로 끝나는 것들 의미 ^은 not의 의미로사용되기도 함
    st = 'a' if len(st) == 0 else st[:15]
    st = re.sub('^[.]|[.]$', '', st)
    st = st if len(st) > 2 else st + "".join([st[-1] for i in range(3-len(st))])
    return st
'''






#순위검색
# 시간초과 코드
def solution(info, query):
    answer = []
    infos = [list(map(str , i.split(' '))) for i in info ]
    querys = [list(map(str , i.replace(' and ' , ' ').split(' '))) for i in query ]
    infdict = [dict.fromkeys(infos_[:-1]+['-'] , int(infos_[-1])) for infos_ in infos ]
    qdict = [dict.fromkeys(querys_[:-1], int(querys_[-1])) for querys_ in querys ]
            
    for q in qdict:
        cnt =0  
        for inf in infdict:
            res = True
            for qk in list(q.keys()):
                if qk not in list(inf.keys()):
                    res = False
                    break
            if res and list(q.values())[0] <= list(inf.values())[0]:
                cnt +=1
        answer.append(cnt)
    return answer





#합승 택시 요금 > 플로이드 워셜 or 다익스트라 -> 공부
def solution(n, s, a, b, fares):
    # 갈 수 없는 곳은 요금이 무한이라
    INF = int(1e9)
    answer = INF
    
    dp = [ [INF]*n for i in range(n)]
    #print(dp)
    for i in fares:
        dp[ i[0]-1 ][ i[1]-1 ] = dp[ i[1]-1 ][ i[0]-1 ] = i[2]
    # for dp1 in dp:
    #     print(dp1)
    # for i in range(n):  
    #     dp[i][i] = 0
    #플로이드 워셜
    # k : 경유지
    for k in range(0, n):
        dp[k][k] = 0
        # i : 출발지    
        for i in range(0, n):
            # j : 목적지
            for j in range(0, n):
                # if문 continue 추가하니 테스트 26번 통과(시간초과 나던거)
                if dp[i][j] ==INF and (dp[i][k]==INF or dp[k][j] == INF):
                    dp[j][i] = dp[i][j] = INF
                    continue
                temp = min(dp[i][j], dp[i][k] + dp[k][j])
                dp[j][i] = dp[i][j] = temp

    #경유지점에따라 최소 합승비용 
    for t in range(n):
        temp = dp[s-1][t] + dp[t][b-1] + dp[t][a-1]      
        answer = min(answer, temp)
    return answer

'''
택시비를 아낄 수 있는 방법 고민
무지 와 비슷한 방향인 어피치
6개 지점 사이의 이동 가능한 택시노선 예상요금
출발지점은 S로 표시된 4번 지점
A B 두사람은 4번지점에서 출발하여두사람 모두 귀가하는데 소요되는 예상 최저 택시요금

그래프에서 최단 거리를 구할 수 있는 알고리즘에는 대표적으로 다익스트라와 플로이드 와샬
'''


# 카드 짝 맞추기
from itertools import permutations # 중복을 허용한 조합
from collections import deque # 양쪽 끝에서 삽입과 삭제가 모두 가능한 자료구조 큐와 스택을 합친것

size = 4  # 보드 사이즈
myboard = [[] for i in range(4)] # 내 보드인 이중 리스트  ? * 4인 행렬
card_pos = {} # 카드의 위치
d = [[0,1], [1,0], [0,-1], [-1,0]] # 조작키 (x좌표 y좌표) DFS/BFS 를 위한 
INF = int(1e4) # 무한대
answer = INF # 우선 답은 무한대라고 가정
orders = [] 

# 전역 변수를 이용한 보드(myboard), 카드 2장의 위치(card_pos) 초기화 
# 지우는 순서에 대한 순열(orders) 초기화
# card_pos 예시: card_pos[1] = [[0,0], [1,2]] // 카드 1은 보드의 [0,0], [1,2]에 존재 
def init(board): # 이문제에서 size 는 4 * 4 보드이다
    global myboard, card_pos, orders
    for i in range(size):
        for j in range(size):
            if board[i][j] != 0: # 넘어온 보드의 i행 j열 이 0이 아니라면 (카드가 있다면)
                card = board[i][j] # card 라는 변수에 해당 카드값 1 or 2 or 3 or.. 을 넘긴다 (카드의 종류)
                if card not in card_pos.keys(): card_pos[card] = [[i,j]] #카드종류가 내가 알고있는 위치가 아니라면 위치추가
                else: card_pos[card].append([i,j]) # 알고있는 카드가 1장 더 있다면 해당 종류의 위치를 추가 총 2장 위치 알게됨

            myboard[i].append(board[i][j]) # 내가 유지하고 있는 보드에 카드를 복사
    
    orders = [key for key in card_pos.keys()] # 123의 카드가 있다면 [1,2,3] 으로 나눠담고
    orders = list(permutations(orders)) # 123 213 231 등의 permutations 종류를 리턴하는 list를 담는다 지우는 순서
    
# 이동한 결과가 보드 범위내 있는지 판단하는 함수            
def isin(y,x): # 이동하고자 하는 좌표가 보드내에 있는지 판단
    if -1<y<size:
        if -1<x<size: return True
        
    return False

# ctrl + 방향키
def move(y, x, mv): 
    # mv는 한 행이 담겨서 넘어오고 ctrl 해서 그 행의 다음 카드로 넘어갈 수 있는지 판단하고 그 카드 좌표를 리턴
    global myboard
    ny, nx = y, x

    while True:
        _ny = ny + mv[0] # 0 1 0 -1
        _nx = nx + mv[1] # 1 0 -1 0
        if not isin(_ny, _nx): return ny, nx # mv의 0과 1 위치에 있는 값을 더했을때 그 좌표가 보드내에 없다면 전값
        if myboard[_ny][_nx] != 0: return _ny, _nx # 보드내에 있으면서 내 보드의 값이 0이 아니라면 (카드가 있다면)
            
        ny = _ny
        nx = _nx

# 카드 1장을 찾을 때 나오는 거리를 반환하는 함수(목표 위치도 반환함)
# 시작 위치: myboard[sy, sx], 찾아야 할 위치: myboard[ey, ex] 
def bfs(sy, sx, ey, ex):
    if [sy, sx] == [ey, ex]: return sy, sx, 1 #시작위치와 찾아야할 위치가 같으니 그대로 return
    global myboard
    q = []
    q = deque(q) # 리스트를 덱 으로  큐 + 스택
    table = [[0 for j in range(size)] for i in range(size)]  # 4 * 4 인데 0으로 채워져있다
    visit = [[False for j in range(size)] for i in range(size)] # False 로 방문 이중리스트
    q.append([sy, sx]) # 덱에다가 시작위치를 넣는다
    visit[sy][sx] = True # 들어온 값은 방문했으니까 True 로 변경

    while q:
        y, x = q.popleft()

        for i in range(4):
            ny = y + d[i][0] # 0 1 0 -1  4군데 돌아보기 위함
            nx = x + d[i][1] # 1 0 -1 0

            if isin(ny, nx): # 옮겨가야 할 좌표가 보드내에 있다면 판단 시작
                if not visit[ny][nx]: # 방문하지 않았어야 한다.
                    visit[ny][nx] = True # 방문하지 않았었으니 방문으로 변환
                    table[ny][nx] = table[y][x] + 1 # 옮겨가야할 좌표의 table에 전에 있던 좌표의 값 +1
                    if [ny,nx] == [ey,ex]: # 옮겨가야할 좌표가 끝 좌표랑 같다면
                        return ny, nx, table[ny][nx] + 1 # 해당 좌표 return 하고 table 1추가해주고

                    q.append([ny, nx]) # 아직 좌표가 끝나지 않았다면 덱에 넣고

            ny, nx = move(y, x, d[i]) # 다음 카드가 있는 곳 까지 옮겨가서

            if not visit[ny][nx]: # 옮겨간 카드에 대해서도 방문 여부와  table 추가하고 마지막인지 확인하고 덱추가
                visit[ny][nx] = True      
                table[ny][nx] = table[y][x] + 1
                if [ny,nx] == [ey,ex]:
                    return ny, nx, table[ny][nx] + 1

                q.append([ny, nx])

    return sy, sx, INF #카드가 있는 곳들을 다 돌았는데 시작카드가 끝카드로 가지 못하면 맞는 카드가 없다는것 무한대 리턴

# 찾은 2장의 카드를 myboard에서 지워주는 함수           
def remove(card):
    global myboard, card_pos
    for y, x in card_pos[card]: myboard[y][x] = 0 # 같은 카드 두장의 위치가 딕셔너리에 추가됐다면 해당 카드들을 지운다.

# 지워진 2장의 카드를 myboard에서 복원해주는 함수
def restore(card):
    global myboard, card_pos
    for y, x in card_pos[card]: myboard[y][x] = card

# backtracking   k 는 0 , m은 i값이니 len(orders) 의 수만큼 반복  count 시작은 0
def backtrack(sy, sx, k, m, count):
    global orders, myboard, answer, card_pos

    if k == len(card_pos.keys()): # k가 0으로 들어왓으니 최초에 그 값이 0이면 count 값을 answer에 담고 return
        if answer > count: answer = count
        return
    # k 와 카드 종류의 개수가 같지 않다면 아래 실행
    card = orders[m][k] # k 는 카드의 순서 0번째 1번째 등등 3종류라면 2까지 
    left_y, left_x = card_pos[card][0][0], card_pos[card][0][1] # 탐색할 카드종류가 key값으로 그 위치를 left_y[0][0] left_x[0][1]
    right_y, right_x = card_pos[card][1][0], card_pos[card][1][1] # 그 종류의 카드가 2개니까 left right로 두 쌍을 탐색

    ry1, rx1, res1 = bfs(sy, sx, left_y, left_x)# 시작좌표에서 left 카드까지 의 좌표와 거리
    ry2, rx2, res2 = bfs(ry1, rx1, right_y, right_x) # left 좌표에서 right 까지 좌표와 거리
    
    remove(card)  # 한 쌍을 찾았으니 remove
    backtrack(ry2, rx2, k+1, m, count + res1 + res2) # 이동거리 res1 과 res2 과 시작count 0을 더해서 count 로 넣어 재귀
    # 재귀가 끝나는 시점은 카드의 종류를 다 돌았을 때  / 아래 주석처리 했을때 answer 가 1크게 나온다.
    restore(card) # 지운카드 다시 복원 왜 다시 추가했는지 잘 모르겠
    # 중간에 길이 막혀서 돌아왔는데 한번더 실행하는경우?
    ry1, rx1, res1 = bfs(sy, sx, right_y, right_x)
    ry2, rx2, res2 = bfs(ry1, rx1, left_y, left_x)

    remove(card)
    backtrack(ry2, rx2, k+1, m, count + res1 + res2)
    restore(card)

def solution(board, r, c):
    global answer
    init(board) # 초기화 하고

    for i in range(len(orders)): # 할 수 있는 모든 경우의 수 (어떤 그림의 쌍을 먼저 찾을것인가 )
        backtrack(r, c, 0, i, 0) # r , c 시작  y , x  좌표로 들어온다. 
    return answer
# def solution(board, r, c):
#     answer = 0
    
#     for i in board:
#         print(i)
    
#     return answer

'''
카드 짝맞추기 보드게임
게임이 시작되면 화면에 카드 16장 뒷면을 위로 4X4
카드 앞면에는 캐릭터그림 8가지 캐릭터 그림이 각기 2장씩 무작위
유저 2장 선택 같은 캐릭터그림 화면에서 사라지고
다른 그림 이면 다시 뒤집기
모두 사라지면  종료

옆으로이동하는 함수구현 1
제거하는 함수 2
리스토어 함수 3




'''