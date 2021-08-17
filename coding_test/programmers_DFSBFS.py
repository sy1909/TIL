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

