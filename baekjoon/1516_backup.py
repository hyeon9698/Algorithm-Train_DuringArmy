import sys
from collections import deque
sys.stdin = open('input.txt', 'r')
n = int(input())
data_time = [0]
graph = [[] for _ in range(n+1)]
indegree = [0 for _ in range(n+1)]
ans = [[0] for _ in range(n+1)]
for i in range(1, n+1):
    d = list(map(int, input().split()))
    data_time.append(d[0])
    for num in d[1:]:
        if num == -1:
            break
        indegree[i] += 1
        graph[num].append(i)
q = deque()
for i in range(1, n+1):
    if indegree[i] == 0:
        q.append((i, data_time[i]))
while q:
    now, now_time = q.popleft()
    print(now, now_time)
    ans[now] = now_time
    for nxt in graph[now]:
        TIME = now_time + data_time[nxt]
        indegree[nxt] -= 1
        if indegree[nxt] == 0:
            q.append((nxt, TIME))
for i in range(1, n+1):
    print(ans[i])