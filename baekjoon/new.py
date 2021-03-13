import heapq
import sys
input = sys.stdin.readline
def dijkstra(start, data, distance):
    heap_data = []
    heapq.heappush(heap_data, (0, start))
    distance[start] = 0
    while heap_data:
        dist, now = heapq.heappop(heap_data)
        if distance[now] < dist:
            continue
        for nextt, time in data[now]:
            cost = time + dist
            if cost < distance[nextt]:
                distance[nextt] = cost
                heapq.heappush(heap_data, (cost, nextt))

def process():
    n, d, c = map(int, input().split())
    data = [[] for _ in range(n+1)]
    for _ in range(d):
        a, b, t = map(int, input().split())
        data[b].append((a, t))
    distance = [1e9]*(n+1)
    dijkstra(c, data, distance)
    count = 0
    m = 0
    for d in distance:
        if d != 1e9:
            count += 1
            m = max(m, d)
    print(count, m)
for _ in range(int(input())):
    process()

