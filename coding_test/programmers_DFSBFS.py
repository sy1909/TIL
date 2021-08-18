numbers = [1, 1, 1, 1, 1]
target =3
# 아마 bfs 탐색 일듯
def solution43165(numbers, target):
    answer = 0
    temp = [0]
    for i in numbers:
        tmp = []
        for j in temp:
            tmp.append(j + i)
            tmp.append(j - i)
        temp = tmp
    answer = temp.count(target)
    return answer
solution43165(numbers, target)


n = 3
computers =  [[1, 1, 0], [1, 1, 0], [0, 0, 1]]
# n = 3
# computers =  [[1, 1, 0], [1, 1, 1], [0, 1, 1]]
def solution43162(n, computers):
    def DFS(i):
        visited[i] = 1
        for a in range(n):
            if computers[i][a] and not visited[a]:
                DFS(a)      
                
    answer = 0
    visited = [0 for i in range(len(computers))]
    for i in range(n):
        if not visited[i]:
            DFS(i)
            answer += 1
        
    return answer
solution43162(n, computers)

begin = "hit"
target = "cog"
words = ["hot", "dot", "dog", "lot", "log", "cog"]
# begin = "hit"
# target = "cog"
# words = ["hot", "dot", "dog", "lot", "log"]
def solution43163(begin, target, words):
    if target not in words:
        return 0
    answer = 0

    def match(current , word):
        match_count=0
        for c , w in zip(current , word):
            if c == w:
                match_count +=1
        if match_count == len(word)-1:
            return True
        else:
            return False

    current_list = [begin]
    visited = [0 for i in range(len(words))]

    while current_list:
        print(current_list)
        current = current_list.pop()
        if current == target:
            print(answer)
            return answer
        for j in range(len(words)):
            if not visited[j]: 
                if match(current, words[j]):
                    visited[j] = 1
                    current_list.append(words[j])
        answer +=1
    

#solution43163(begin, target, words)

tickets = 	[["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL", "SFO"]]
def solution(tickets):
    answer = []
    routes = {}
    for t in tickets:
        print( routes.get(t[0] , []))
        routes[t[0]] = routes.get(t[0] , []) +  [t[1]]
        print(routes)
#        routes[t[0]] = [t[1]]
    print(routes)
    for r in routes:
        routes[r].sort(reverse=True)
    current_list = ["ICN"]
    
    while current_list:
        current = current_list[-1]
        if current in routes and routes[current]:
            current_list.append(routes[current].pop())
        else:
            answer.append(current_list.pop())
            
    answer.reverse()
    return answer
solution(tickets)