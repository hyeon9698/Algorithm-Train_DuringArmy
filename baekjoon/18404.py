import sys
from collections import deque
sys.stdin = open('input.txt', 'r')


def bfs(x, y):
    q = deque([(x, y)])
    while q:
        x, y = q.popleft()
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
            if 1<=nx<n+1 and 1<=ny<n+1 and count_data[nx][ny] == 0:
                count_data[nx][ny] = count_data[x][y] + 1
                q.append((nx, ny))

# def dfs(x, y):
#     for i in range(8):
#         nx = x + dx[i]
#         ny = y + dy[i]
#         if 1<=nx<n+1 and 1<=ny<n+1 and count_data[x][y] + 1 < count_data[nx][ny]:
#             count_data[nx][ny] = count_data[x][y] + 1
#             dfs(nx, ny)

dx = [-2, -1, 1, 2, 2, 1, -1, -2]
dy = [1, 2, 2, 1, -1, -2, -2, -1]
n, m = map(int, input().split())
x, y = map(int, input().split())
data = []
count_data = [[0]*(n+1) for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    data.append((a, b))
# dfs(x, y)
bfs(x, y)
for xx, yy in data:
    print(count_data[xx][yy])