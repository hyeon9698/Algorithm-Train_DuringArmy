import sys
import heapq
INF = sys.maxsize
def dijkstra(start_node):
    distance = [INF] * (n+1)
    heap = []
    heapq.heappush(heap, [0, start_node])
    distance[start_node] = 0
    while heap:
        now_cost, node = heapq.heappop(heap)
        for next_cost, next_node in graph[node]:
            next_cost = next_cost + now_cost
            if next_cost < distance[next_node]:
                distance[next_node] = next_cost
                heapq.heappush(heap, [next_cost, next_node])
    return distance

sys.stdin = open('input.txt', 'r')
n, m, x = map(int, input().split())
graph = [[]*(n+1) for _ in range(n+1)]
for _ in range(m):
    start, end, cost = map(int, input().split())
    graph[start].append((cost, end))
answer = [0] * (n+1)
for i in range(1, n+1):
    arr = dijkstra(i)
    answer[i] += arr[x]
    arr2 = dijkstra(x)
    answer[i] += arr2[i]
print(max(answer))