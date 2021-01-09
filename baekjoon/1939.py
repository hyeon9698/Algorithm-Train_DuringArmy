import sys
from collections import deque
sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline
def bfs(c):
    q = deque([start])
    while q:
        now = q.popleft()
        for nextt, weight in data[now]:
            if not visited[nextt]:
                
                q.append(nextt)
n, m = map(int, input().split())
ans = 1e9
data = [[]*(n+1)]
for _ in range(m):
    a, b, c = map(int, input().split())
    data[a].append((b, c))
    data[b].append((a, c))
start, end = map(int, input().split())
visited = [False]*(n+1)
bfs(c)