import sys
sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline
def find(node):
    if parent[node] != node:
        parent[node] = find(parent[node])
    return parent[node]
def union(node_v, node_u):
    root1 = find(node_v)
    root2 = find(node_u)
    if rank[root1] > rank[root2]:
        parent[root2] = root1
    else:
        parent[root1] = root2
        if rank[root1] == rank[root2]:
            rank[root2] += 1
def kruskal(graph):
    weights = []
    graph.sort()
    for i in range(n+1):
        setup(i)
    for edge in graph:
        if find(edge[1]) != find(edge[2]):
            union(edge[1], edge[2])
            weights.append(edge[0])
    print(sum(weights)-max(weights))
def setup(node):
    parent[node] = node
    rank[node] = 0
n, m = map(int, input().split())
graph = []
parent = {}
rank = {}
for _ in range(m):
    a, b, c = map(int, input().split())
    graph.append((c, a, b))
kruskal(graph)
