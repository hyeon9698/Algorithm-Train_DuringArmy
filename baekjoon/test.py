graph = {
    'vetices':['A','B','C','D','E','F','G'],
    'edges':[
        (7,'A','B')
    ]
}
parent = {}
rank = {}
# 초기화
def make_set(node):
    parent[node] = node
    rank[node] = 0



def kruskal(graph):
    mst = []
    for node in graph['vetices']:
        make_set(node)
    edges = graph['edges']
    edges.sort()
    
    for edge in edges:
        weight, node_v, node_u = edge
        if find(node_v) != find(node_u):
            
    
    return mst