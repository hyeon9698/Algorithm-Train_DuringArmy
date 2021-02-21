from collections import deque
import sys
sys.stdin = open('input.txt', 'r')
n, m = map(int, input().split())
data = [list(map(int, input())) for _ in range(n)]
visited = [[[0 for _ in range(m)] for _ in range(n)] for _ in range(2)]
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
def bfs():
    q = deque([(0, 0, 0)])
    visited[0][0][0] = 1
    while q:
        x, y, c = q.popleft()
        if x == n-1 and y == m-1:
            return visited[c][x][y]
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<n and 0<=ny<m and not visited[c][nx][ny]:
                if not data[nx][ny]:
                    visited[c][nx][ny] = visited[c][x][y] + 1
                    q.append((nx, ny, c))
                elif data[nx][ny] and not c:
                    visited[1][nx][ny] = visited[c][x][y] + 1
                    q.append((nx, ny, 1))
    return -1
print(bfs())