import sys
sys.stdin = open('input.txt', 'r')

def check(x, y, lst):
    flag = False
    if lst[x-1][y-1] != 0 and lst[x-1][y] != 0 and lst[x][y-1] != 0:
        lst[x][y] = min(lst[x-1][y-1], lst[x-1][y], lst[x][y-1]) + 1

n, m = map(int, input().split())
data = [[0]*(m+1) for _ in range(n+1)]
for i in range(1, n+1):
    data[i] = [0] + (list(int(i) for i in input()))

for i in range(1, n+1):
    for j in range(1, m+1):
        if data[i][j]:
            check(i, j, data)
maxx = max([max(i) for i in data])
print(maxx*maxx)

