import sys
sys.stdin = open('input.txt', 'r')
n, m, x = map(int, input().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    start, end, cost = map(int, input().split())
    graph[start].append((end, cost))
print(graph)