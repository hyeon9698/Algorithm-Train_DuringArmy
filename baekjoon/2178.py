import sys
from collections import deque
sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline
def bfs(xx, yy):
    q = deque([(xx, yy)])
    visited[xx][yy] = True
    while q:
        x, y = q.popleft()
        if x == n-1 and y == m-1:
            print(ans[n-1][m-1])
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<n and 0<=ny<m and data[nx][ny] == 1 and not visited[nx][ny]:
                visited[nx][ny] = True
                ans[nx][ny] = ans[x][y] + 1
                q.append((nx, ny))
n, m = map(int, input().split())
data = [list(map(int, input().rstrip())) for _ in range(n)]
visited = [[False]*(m) for _ in range(n)]
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
ans = [[1]*(m) for _ in range(n)]
bfs(0, 0)
