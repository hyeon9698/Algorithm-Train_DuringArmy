# import sys
# sys.stdin = open('input.txt', 'r')
# input = sys.stdin.readline

# 크루스칼 Kruskal's algorithm
# parent = {}
# rank = {}
# def find(node):
#     if parent[node] != node:
#         parent[node] = find(parent[node])
#     return parent[node]
# def union(node_v, node_u):
#     root1 = find(node_v)
#     root2 = find(node_u)
#     if rank[root1] > rank[root2]:
#         parent[root2] = root1
#     else:
#         parent[root1] = root2
#         if rank[root1] == rank[root2]:
#             rank[root2] += 1
# def setup(node):
#     parent[node] = node
#     rank[node] = 0
# v, e = map(int, input().split())
# graph = []
# ans = 0
# for _ in range(e):
#     a, b, c = map(int, input().split())
#     graph.append((c, a, b))
# graph.sort()
# for i in range(v+1):
#     setup(i)
# for node in graph:
#     if find(node[1]) != find(node[2]):
#         union(node[1], node[2])
#         ans += node[0]
#     else:
#         pass
# print(ans)

# Prim's algorithm
import sys
from heapq import *
sys.stdin = open('input.txt', 'r')
def prim(start_node):
    ans = 0
    connected_nodes.add(start_node)
    possible_edges = graph[start_node]
    heapify(possible_edges)
    while possible_edges:
        now_weight, now_pointing_node = heappop(possible_edges)
        if now_pointing_node in connected_nodes:
            continue
        connected_nodes.add(now_pointing_node)
        ans += now_weight
        for edge in graph[now_pointing_node]:
            if edge[1] not in connected_nodes:
                heappush(possible_edges, edge)
    return ans
v, e = map(int, input().split())
graph = [[] for _ in range(v+1)]
connected_nodes = set()
possible_edges = {}
for _ in range(e):
    a, b, c = map(int, input().split())
    graph[a].append((c, b))
    graph[b].append((c, a))
print(prim(1))