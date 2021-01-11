import sys
from itertools import permutations
sys.stdin = open('input.txt', 'r')
def rotate(data, i):
    r = i[0]
    c = i[1]
    s = i[2]
    # //2 해서 더 작은걸로 for 문 돌리기
    row_length = 2*s + 1
    column_length = 2*s + 1
    how_many = min(row_length//2, column_length//2)
    for i in range(how_many):
        pass
n, m, k = map(int, input().split())
rotate_list = []
ans_list = []
A = [list(map(int, input().split())) for _ in range(n)]
Q = [tuple(map(int, input().split())) for _ in range(k)]
print(Q)
ans = 10000
def value(arr):
    return min([sum(i) for i in arr])
def dfs(arr, qry):
    pass
# dfs(A, {})
print(ans)