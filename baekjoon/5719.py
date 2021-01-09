from collections import deque
import sys
import heapq

INF = 1e9


def dijkstra():
    q = []
    heapq.heappush(q, (0, s))
    distance[s] = 0  # 출발지

    while q:  # 큐가 비어있지 않다면
        dist, now = heapq.heappop(q)
        # 현재 노드가 이미 처리된 적이 있는 노드라면 무시
        if distance[now] < dist:
            continue
        # 현재 노드와 연결된 다른 인접한 노드들을 확인하면서 거리 업데이트
        for i in graph[now]:
            cost = dist + graph[now][i]
            if cost < distance[i]:  # 해당 지점을 거치는 것이 거리가 짧은 경우
                distance[i] = cost
                heapq.heappush(q, (cost, i))


def bfs():
    q = deque()
    q.append(d)
    while q:
        v = q.popleft()
        if v == s:  # 시작점 도달
            continue  # break하면 다른 최단 경로를 확인할 수 없다.
        for pre_v, pre_c in r_graph[v]:
            if distance[pre_v] + graph[pre_v][v] == distance[v]:
                if (pre_v, v) not in remove_List:
                    remove_List.append((pre_v, v))
                    q.append(pre_v)


if __name__ == "__main__":
    while True:
        n, m = map(int, sys.stdin.readline().split())
        if n == 0 and m == 0:  # n과 m이 0이면 종료
            break
        s, d = map(int, sys.stdin.readline().split())  # 출발지, 도착지
        graph = [dict() for _ in range(n)]
        r_graph = [[] for _ in range(n)]
        for _ in range(m):
            u, v, p = map(int, sys.stdin.readline().split())  # 도로 정보 입력
            graph[u][v] = p
            r_graph[v].append((u, p))  # 경로를 추적하기 위해서 역순 저장

        # 다익스트라 알고리즘을 사용하여 최단 거리 찾기
        distance = [INF] * n
        dijkstra()

        # BFS를 사용하여 최단 경로 추적
        remove_List = list()
        bfs()

        # 최단 경로 제거
        for u, v in remove_List:
            del graph[u][v]

        # 다익스트라 알고리즘을 사용하여 최종 최단 경로 찾기
        distance = [INF] * n
        dijkstra()
        if distance[d] == INF:  # 거의 최단 경로가 없는 경우
            print(-1)
        else:
            print(distance[d])

# from collections import deque
# from heapq import heappush, heappop
# import sys
# # sys.stdin = open('input.txt', 'r')
# input = sys.stdin.readline
# def dijkstra(start):
#     heap = []
#     heappush(heap, [0, start])
#     dp = [100000000 for i in range(n)]
#     dp[start] = 0
#     while heap:
#         a, b = heappop(heap)
#         for n_n, w in arr[b]:
#             wei = w + a
#             if dp[n_n] > wei and check[b][n_n] == 0:
#                 dp[n_n] = wei
#                 heappush(heap, [wei, n_n])
#     return dp
# def delete(end, dp):
#     q = deque()
#     q.append(end)
#     while q:
#         num = q.popleft()
#         for bef, co in arr_r[num]:
#             if dp[num] == dp[bef] + co:
#                 check[bef][num] = 1
#                 q.append(bef)
# while True:
#     n, m = map(int, input().split())
#     if n == 0 and m == 0:
#         break
#     s, d = map(int, input().split())
#     arr = [[] for i in range(n)]
#     arr_r = [[] for i in range(n)]
#     check = [[0] * n for i in range(n)]
#     for i in range(m):
#         a, b, c = map(int, input().split())
#         arr[a].append([b, c])
#         arr_r[b].append([a, c])
#     dp = dijkstra(s)
#     delete(d, dp)
#     dp = dijkstra(s)
#     print(dp[d] if dp[d] != 100000000 else -1)






# import sys
# import heapq
# from collections import deque
# # sys.stdin = open('input.txt', 'r')
# input = sys.stdin.readline
# def dijkstra():
#     heap_data = []
#     heapq.heappush(heap_data, (0, start))
#     distance[start] = 0
#     while heap_data:
#         dist, now = heapq.heappop(heap_data)
#         if dist > distance[now]:
#             continue
#         for nextt, price in data[now]:
#             cost = price + dist
#             # print(distance)
#             # print(now, nextt)
#             # print(dropped)
#             if cost < distance[nextt] and not dropped[now][nextt]:
#                 distance[nextt] = cost
#                 heapq.heappush(heap_data, (cost, nextt))
# def bfs(end):
#     q = deque([end])
#     while q:
#         now = q.popleft()
#         if now == start:
#             continue
#         for prev, price in data_reversed[now]:
#             if distance[prev] == distance[now] - price:
#                 q.append(prev)
#                 dropped[prev][now] = True
# while True:
#     n, m = map(int, input().split())
#     if n == 0:
#         break
#     start, end = map(int, input().split())
#     data = [[] for _ in range(n)]
#     data_reversed = [[] for _ in range(n)]
#     for _ in range(m):
#         u, v, p = map(int, input().split())
#         data[u].append((v, p))
#         data_reversed[v].append((u, p))
#     dropped = [[False]*n for _ in range(n)]
#     distance = [1e9]*n
#     dijkstra()
#     # print('distance -> ', distance)
#     bfs(end)
#     distance = [1e9]*n
#     dijkstra()
#     if distance[end] != 1e9:
#         print(distance[end])
#     else:
#         print(-1)





















# import sys
# import heapq

# sys.stdin = open("input.txt", 'r')
# def dijkstra(start):
#     heap_data = []
#     heapq.heappush(heap_data, (0, start))
#     distance[start] = 0
#     while heap_data:
#         dist, now = heapq.heappop(heap_data)
#         if distance[now] < dist:
#             continue
#         for i in graph[now]:
#             cost = dist + i[1]
#             if distance[i[0]] > cost:
#                 distance[i[0]] = cost
#                 heapq.heappush(heap_data, (cost, i[0]))
    
    
# n, m = map(int, input().split())
# s, d = map(int, input().split())
# for _ in range(m):
#     x, y, cost = map(int, input().split())
#     graph[x].append((y, cost))
# distance = [1e9] * (n+1)
