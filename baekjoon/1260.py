from collections import deque
import sys
# sys.stdin = open('input.txt', 'r')


def dfs(v):
    visited[v] = True
    print(v, end=' ')
    for nextt in data[v]:
        if not visited[nextt]:
            visited[nextt] = True
            dfs(nextt)

def bfs(v):
    q = deque([v])
    visited[v] = True
    while q:
        now = q.popleft()
        print(now, end=' ')
        for nextt in data[now]:
            if not visited[nextt]:
                visited[nextt] = True
                q.append(nextt)
n, m, v = map(int, input().split())
data = [[]*(n+1) for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    data[a].append(b)
    data[b].append(a)
for i in range(n):
    data[i].sort()

visited = [False]*(n+1)
dfs(v)
print()
visited = [False]*(n+1)
bfs(v)



















# def bfs(v):
#     q = deque([v])
#     visited[v] = True
#     while q:
#         now = q.popleft()
#         print(now, end=' ')
#         for next_val in graph[now]:
#             if not visited[next_val]:
#                 visited[next_val] = True
#                 q.append(next_val)
# def dfs(v):
#     print(v, end=' ')
#     visited[v] = True
#     for next_val in graph[v]:
#         if not visited[next_val]:
#             dfs(next_val)


# n, m, v = map(int, input().split())
# graph = [[] for _ in range(n+1)]
# for _ in range(m):
#     x, y = map(int, input().split())
#     graph[x].append(y)
#     graph[y].append(x)
# for data in graph:
#     data.sort()
# visited = [False]*(n+1)
# dfs(v)
# print()
# visited = [False]*(n+1)
# bfs(v)
