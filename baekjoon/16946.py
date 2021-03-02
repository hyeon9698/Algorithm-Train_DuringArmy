import sys
from copy import deepcopy
from collections import deque
sys.stdin = open("input.txt", 'r')
input = sys.stdin.readline
def bfs(i, j):
    visited[i][j] = True
    q = deque([(i, j)])
    cnt = 1
    while q:
        x, y = q.popleft()
        for k in range(4):
            xx = x + dx[k]
            yy = y + dy[k]
            if 0<=xx<n and 0<=yy<m and not visited[xx][yy] and data[xx][yy] == 0:
                visited[xx][yy] = True
                cnt += 1
                q.append((xx, yy))
    ans[i][j] = cnt
def dfs():
    pass
n, m = map(int, input().split())
data = [list(map(int, list(input()))) for _ in range(n)]
visited_false = [[False for _ in range(m)] for _ in range(n)]
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
ans = [[0 for _ in range(m)] for _ in range(n)]
for i in range(n):
    for j in range(m):
        if data[i][j] == 0:
            continue
        visited = deepcopy(visited_false)
        data[i][j] = 0
        bfs(i, j)
        data[i][j] = 1
for i in ans:
    print(''.join(map(str,i)))