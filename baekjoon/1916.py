import sys
from collections import deque
sys.stdin = open('input.txt', 'r')
def kruskal(start, end):
    visited[start] = 0
    q = deque([(start, 0)])
    while q:
        now, now_cost = q.popleft()
        # print(now, now_cost, visited)
        # if now == end:
            # return visited[now]
        for nxt, nxt_cost in data[now]:
            cost = now_cost + nxt_cost
            if visited[nxt] > cost:
                visited[nxt] = cost
                q.append((nxt, cost))
n = int(input())
m = int(input())
data = [[] for _ in range(n+1)]
visited = [1e9 for _ in range(n+1)]
for _ in range(m):
    a, b, c = map(int, input().split())
    data[a].append((b, c))
start, end = map(int, input().split())
kruskal(start, end)
print(visited[end])