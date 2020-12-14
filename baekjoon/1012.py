from collections import deque
di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]
def bfs(i, j):
    q = deque([(i, j)])
    while q:
        i, j = q.popleft()
        
        for k in range(4):
            next_di = i + di[k]
            next_dj = j + dj[k]
            if 0 <= next_di < n and 0 <= next_dj < m and graph[next_di][next_dj] == 1:
                graph[next_di][next_dj] = 0
                q.append((next_di, next_dj))

test_case = int(input())
for _ in range(test_case):    
    m, n, k = map(int, input().split())
    graph = [[0]*m for _ in range(n)]
    count = 0
    for _ in range(k):
        j, i = map(int, input().split())
        graph[i][j] = 1
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 1:
                bfs(i,j)
                count += 1
    print(count)