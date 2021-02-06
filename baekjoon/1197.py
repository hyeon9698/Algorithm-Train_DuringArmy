import sys
sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline
크루스칼 Kruskal's algorithm
parent = {}
rank = {}
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
def setup(node):
    parent[node] = node
    rank[node] = 0
v, e = map(int, input().split())
graph = []
ans = 0
for _ in range(e):
    a, b, c = map(int, input().split())
    graph.append((c, a, b))
graph.sort()
for i in range(v+1):
    setup(i)
for node in graph:
    if find(node[1]) != find(node[2]):
        union(node[1], node[2])
        ans += node[0]
    else:
        pass
print(ans)