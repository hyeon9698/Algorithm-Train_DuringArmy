import sys
sys.setrecursionlimit(int(1e5))
sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline
n = int(input())
data = [list(map(int, input().split())) for _ in range(n-1)]
parent = [0]*(n+1)
m = int(input())
d = [-1]*(n+1)
wantdata = [list(map(int, input().split())) for _ in range(m)]
graph = [[] for _ in range(n+1)]
for x, y in data:
    graph[x].append(y)
    graph[y].append(x)
def dfs(x, depth):
    d[x] = depth
    for y in graph[x]:
        if d[y] != -1:
            continue
        parent[y] = x
        dfs(y, depth + 1)
dfs(1, 0)
def lca(a, b):
    while d[a] != d[b]:
        if d[a] > d[b]:
            a = parent[a]
        else:
            b = parent[b]
    while a != b:
        a = parent[a]
        b = parent[b]
    return a
for x, y in wantdata:
    print(lca(x, y))