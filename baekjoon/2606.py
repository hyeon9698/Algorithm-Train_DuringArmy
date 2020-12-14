n = int(input())
m = int(input())
count = 0
graph = [[] for _ in range(n+1)]
visited = [False] * (n+1)
for _ in range(m):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)
def dfs(now_pos):
    global count
    count += 1
    visited[now_pos] = True
    for next_pos in graph[now_pos]:
        if not visited[next_pos]:
        dfs(next_pos)
dfs(1)
print(count - 1)
