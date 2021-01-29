# 다시 해보기 패스트캠퍼스
from collections import defaultdict
from heapq import *
myedges = [
    (7, 'A', 'B'), (5, 'A', 'D'),
    (8, 'B', 'C'), (9, 'B', 'D'), (7, 'B', 'E'),
    (5, 'C', 'E'),
    (7, 'D', 'E'), (6, 'D', 'F'),
    (8, 'E', 'F'), (9, 'E', 'G'),
    (11, 'F', 'G')
]
def prim(start_node, edges):
    mst = list()
    adjacent_edges = defaultdict(list)
    connected_nodes = set(start_node)
    for weight, n1, n2 in edges:
        adjacent_edges[n1].append((weight, n1, n2))
        adjacent_edges[n2].append((weight, n2, n1))
    candidate_edge_list = adjacent_edges[start_node]
    heapify(candidate_edge_list)
    while candidate_edge_list:
        weight, now1, now2 = heappop(candidate_edge_list)
        if now2 in connected_nodes:
            continue
        connected_nodes.add(now2)
        mst.append((weight, now1, now2))
        for edge in adjacent_edges[now2]:
            if edge[2] in connected_nodes:
                continue
            heappush(candidate_edge_list, edge)
    return mst
print(prim('A', myedges))