import sys
sys.stdin = open('input.txt', 'r')
for _ in range(int(input())):
    n, m, w = map(int, input().split())
    graph = [[] for _ in range(n+1)]
    for _ in range(m):
        a, b, c = map(int, input().split())
        graph[a].append((b, c))
        graph[b].append((a, c))
    for _ in range(w):
        a, b, c = map(int, input().split())
        graph[a].append((b, -c))
    