from copy import deepcopy
import sys
sys.stdin = open('input.txt', 'r')

def rotate90(B, n):
    NB = deepcopy(B)
    for i in range(n):
        for j in range(n):
            NB[j][n-i-1] = B[i][j]
    return NB
def convert(lst, n):
    new_list = [i for i in lst if i]
    for i in range(1, len(new_list)):
        if new_list[i-1] == new_list[i]:
            new_list[i-1] *= 2
            new_list[i] = 0
    new_list = [i for i in new_list if i]
    return new_list + [0]*(n-len(new_list))
def dfs(n, B, count):
    ret = max([max(i) for i in B])
    if count == 0:
        return ret
    for _ in range(4):
        X = [convert(i, n) for i in B]
        if X != B:
            ret = max(ret, dfs(n, X, count-1))
        B = rotate90(B, n)
    return ret
n = int(input())
Board = []
for _ in range(n):
    Board.append(list(map(int, input().split())))
print(dfs(n, Board, 5))