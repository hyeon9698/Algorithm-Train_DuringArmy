import sys
import heapq

sys.stdin = open("input.txt", 'r')
def dijkstra(start):
    heap_data = []
    heapq.heappush(heap_data, (0, start))
    distance[start] = 0
    while heap_data:
        dist, now = heapq.heappop(heap_data)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if distance[i[0]] > cost:
                distance[i[0]] = cost
                heapq.heappush(heap_data, (cost, i[0]))
    
    
n, m = map(int, input().split())
s, d = map(int, input().split())
for _ in range(m):
    x, y, cost = map(int, input().split())
    graph[x].append((y, cost))
distance = [1e9] * (n+1)
