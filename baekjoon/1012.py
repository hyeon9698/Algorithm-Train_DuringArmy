from collections import deque
import sys
sys.setrecursionlimit(10 ** 4)
# sys.stdin = open('input.txt', 'r')
def bfs(x_cor, y_cor):
        q = deque([(x_cor, y_cor)])
        while q:
            x, y = q.popleft()
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0 <= nx < n and 0 <= ny < m and data[nx][ny] == 1:
                    q.append((nx, ny))
                    data[nx][ny] = 0
def dfs(x_cor, y_cor):
    x, y = x_cor, y_cor
    for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0 <= nx < n and 0 <= ny < m and data[nx][ny] == 1:
                    data[nx][ny] = 0
                    dfs(nx, ny)
for _ in range(int(input())):
    m, n, k = map(int, input().split())
    data = [[0]*m for _ in range(n)]
    cnt = 0
    for _ in range(k):
        y, x = map(int, input().split())
        data[x][y] = 1
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    for i in range(n):
        for j in range(m):
            if data[i][j] == 1:
                dfs(i, j)
                cnt += 1
    print(cnt)














# from collections import deque
# di = [0, 1, 0, -1]
# dj = [1, 0, -1, 0]
# def bfs(i, j):
#     q = deque([(i, j)])
#     while q:
#         i, j = q.popleft()
        
#         for k in range(4):
#             next_di = i + di[k]
#             next_dj = j + dj[k]
#             if 0 <= next_di < n and 0 <= next_dj < m and graph[next_di][next_dj] == 1:
#                 graph[next_di][next_dj] = 0
#                 q.append((next_di, next_dj))

# test_case = int(input())
# for _ in range(test_case):    
#     m, n, k = map(int, input().split())
#     graph = [[0]*m for _ in range(n)]
#     count = 0
#     for _ in range(k):
#         j, i = map(int, input().split())
#         graph[i][j] = 1
#     for i in range(n):
#         for j in range(m):
#             if graph[i][j] == 1:
#                 bfs(i,j)
#                 count += 1
#     print(count)