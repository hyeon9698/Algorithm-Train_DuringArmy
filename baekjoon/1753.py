import sys
from heapq import *
sys.stdin = open('input.txt', 'r')
def dijkstra(start):
    distance[start] = 0
    q = [(0, start)]
    heapify(q)
    while q:
        dist, now = heappop(q)
        for nxt in graph[now]:
            cost = dist + nxt[1]
            if cost < distance[nxt[0]]:
                distance[nxt[0]] = cost
                heappush(q, (cost, nxt[0]))
v, e = map(int, input().split())
k = int(input())
graph = [[] for _ in range(v+1)]
for _ in range(e):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
distance = [1e9]*(v+1)
dijkstra(k)
for i in range(1, v+1):
    if distance[i] == 1e9:
        print('INF')
    else:
        print(distance[i])
