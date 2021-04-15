# 나중에 문제 나오면 풀어보기
# a = [0,1,0]
# edges = [[0,1],[1,2]]
n = len(a)
ans = 0
graph = [[] for i in range(n)]
indegree = [0]*n
visited = [False]*n
q = []
for i in edges:
    graph[i[0]].append(i[1])
    graph[i[1]].append(i[0])
for i in range(n):
    indegree[i] = len(graph[i])
    if len(graph[i]) == 1:
        q.append(i)
        
while q:
    # print(a)
    now = q.pop()
    visited[now] = True
    if a[now] == 0:
        continue
    for nxt in graph[now]:
        if visited[nxt]:
            continue
        indegree[nxt] -= 1
        if a[now] > 0:
            while a[now] != 0:
                ans += 1
                a[now] -= 1
                a[nxt] += 1
        else:
            while a[now] != 0:
                ans += 1
                a[now] += 1
                a[nxt] -= 1
        if indegree[nxt] == 1:
            # print("q가 append 됐습니다.",nxt)
            q.append(nxt)
print(a)

print(ans)