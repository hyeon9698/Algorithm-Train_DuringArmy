# 다시해보기
import sys
from math import inf
sys.stdin = open('input.txt', 'r')
n = int(input())
m = int(input())
graph = [[inf for _ in range(n+1)] for _ in range(n+1)]
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a][b] = min(graph[a][b], c)
for i in range(1, n+1):
    graph[i][i] = 0
for k in range(1, n+1):
    for i in range(1, n+1):
        for j in range(1, n+1):
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])
for i in graph[1:]:
    print(' '.join(map(str, i[1:])))
