import sys
from collections import deque
from heapq import *
sys.stdin = open('input.txt', 'r')
def dijkstra(start, end):
    visited[start] = 0
    q = [(start, 0)]
    heapify(q)
    while q:
        now, now_cost = heappop(q)
        for nxt, nxt_cost in data[now]:
            cost = now_cost + nxt_cost
            if visited[nxt] > cost:
                visited[nxt] = cost
                heappush(q, (nxt, cost))
n = int(input())
m = int(input())
data = [[] for _ in range(n+1)]
visited = [1e9 for _ in range(n+1)]
for _ in range(m):
    a, b, c = map(int, input().split())
    data[a].append((b, c))
start, end = map(int, input().split())
dijkstra(start, end)
print(visited[end])