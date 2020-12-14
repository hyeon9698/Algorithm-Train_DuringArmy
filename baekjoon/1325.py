from collections import deque

n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    x, y = map(int, input().split())
    graph[y].append(x)
max = -1
result = []
def bfs(v):
    visited = [False]*(n+1)
    q = deque([v])
    visited[v] = True
    count = 1
    while q:
        now = q.popleft()
        for next_val in graph[now]:
            if not visited[next_val]:
                visited[next_val] = True
                q.append(next_val)
                count += 1
    return count

for i in range(1, n+1):
    count = bfs(i)
    if max < count:
        result = [i]
        max = count
    elif count == max:
        result.append(i)
# for num in result:
#     print(num, end=' ')
print(*result)