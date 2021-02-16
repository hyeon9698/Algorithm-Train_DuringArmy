import sys
from copy import deepcopy
sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline
n, m = map(int, input().split())
data = [[0]*(n+1)] + [[0] + list(map(int, input().split())) for _ in range(n)]
cor = [list(map(int, input().split())) for _ in range(m)]
for i in range(1, n+1):
    for j in range(1, n+1):
        data[i][j] += data[i-1][j] + data[i][j-1] - data[i-1][j-1]
for i in range(m):
    x1 = cor[i][0]
    y1 = cor[i][1]
    x2 = cor[i][2]
    y2 = cor[i][3]
    ans = data[x2][y2] - data[x2][y1-1] - data[x1-1][y2] + data[x1-1][y1-1]
    print(ans)
