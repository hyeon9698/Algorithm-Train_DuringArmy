import sys
sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline
def find(node):
    if parent[node] != node:
        find(parent[node])
    return parent[node]
def union_byrank(a, b):
    root_a = find(a)
    root_b = find(b)
    if rank[root_a] < rank[root_b]:
        tmp = parent[root_a]
        for i, num in enumerate(parent):
            if num == tmp:
                parent[i] = root_b
    else:
        tmp = parent[root_b]
        for i, num in enumerate(parent):
            if num == tmp:
                parent[i] = root_a
        if rank[root_a] == rank[root_b]:
            rank[root_a] += 1
def connected(data_i, data_j):
    i_x = data_i[0]
    i_y = data_i[1]
    i_r = data_i[2]
    j_x = data_j[0]
    j_y = data_j[1]
    j_r = data_j[2]
    if (j_x - i_x)**2 + (j_y - i_y)**2 <= (i_r + j_r)**2:
        return True
    return False
for _ in range(int(input())):
    n = int(input())
    data = [list(map(int, input().split())) for _ in range(n)]
    parent = [i for i in range(n)]
    rank = [0 for _ in range(n)]
    for i in range(n):
        for j in range(1, n):
            if connected(data[i], data[j]):
                # print(f'union => {i}, {j}')
                union_byrank(i, j)
                # print(f'parent-> {parent}')
                # print(f'rank-> {rank}')
    print(len(set(parent)))
"""
1
4
0 0 1
0 4 1
0 1 1
0 3 1
답 : 1
"""