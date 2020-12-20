def bfs(x, y):
    global result
    q = set()
    q.add((x, y, graph[x][y]))
    while q:
        x, y, step = q.pop()
        result = max(result, len(step))
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if (0 <= nx < r and 0 <= ny < c and graph[nx][ny] not in step):
                # print(step+graph[nx][ny])
                q.add((nx, ny, step + graph[nx][ny]))


r, c = map(int, input().split())
graph = []
for i in range(r):
    graph.append(input())
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
result = 0
bfs(0, 0)
print(result)
