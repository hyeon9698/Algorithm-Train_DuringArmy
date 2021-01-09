import heapq
import sys
# sys.stdin = open('input.txt', 'r')
def dijkstra(start, data, distance):
    heap_data = []
    heapq.heappush(heap_data, (0, start))
    distance[start] = 0
    while heap_data:
        dist, now = heapq.heappop(heap_data)
        if distance[now] < dist:
            continue
        for nextt, time in data[now]:
            # print(f'')
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





















# import heapq
# import sys
# input = sys.stdin.readline


# def dijkstra(start):
#     heap_data = []
#     heapq.heappush(heap_data, (0, start))
#     distance[start] = 0
#     while heap_data:
#         dist, now = heapq.heappop(heap_data)
#         if distance[now] < dist:
#             continue
#         for i in adj[now]:
#             cost = dist + i[1]
#             if distance[i[0]] > cost:
#                 distance[i[0]] = cost
#                 heapq.heappush(heap_data, (cost, i[0]))


# for _ in range(int(input())):
#     n, m, start = map(int, input().split())
#     adj = [[] for i in range(n+1)]
#     distance = [1e9] * (n+1)
#     for _ in range(m):
#         x, y, cost = map(int, input().split())
#         adj[y].append((x, cost))
#     dijkstra(start)
#     count = 0
#     max_distance = 0
#     for i in distance:
#         if i != 1e9:
#             count += 1
#             if i > max_distance:
#                 max_distance = i
#     print(count, max_distance)
