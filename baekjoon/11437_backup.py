# https://www.youtube.com/watch?v=O895NbxirM8
# 영상 보면서 다시해보기
import sys
sys.setrecursionlimit(int(1e5))
sys.stdin = open('input.txt', 'r')
LOG = 21 # 2^21 = 1000000
input = sys.stdin.readline

def dfs(x, depth):
    d[x] = depth
    for y in graph[x]:
        if d[y] != -1:
            continue
        parent[y][0] = x
        dfs(y, depth + 1)
def lca(a, b):
    if d[a] > d[b]:
        a, b = b, a
    for i in range(LOG-1, -1, -1):
        if d[b] - d[a] >= (1 << i):
            b = parent[b][i]
    while d[a] != d[b]:
        if d[a] > d[b]:
            a = parent[a]
        else:
            b = parent[b]
    while a != b:
        a = parent[a]
        b = parent[b]
    return a
def set_parent():
    dfs(1, 0)
    for i in range(1, LOG):
        for j in range(1, n+1):
            parent[j][i] = parent[parent[j][i-1]][i-1]
n = int(input())
graph = [[] for _ in range(n+1)]
for _ in range(n-1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
parent = [[0]*LOG for _ in range(n+1)]
d = [-1]*(n+1)
set_parent()
m = int(input())
for _ in range(m):
    a, b = map(int, input().split())
    print(lca(x, y))