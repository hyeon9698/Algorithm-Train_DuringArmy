from collections import deque
import sys
sys.stdin = open('input.txt', 'r')
n, k = map(int, input().split())
data = []
for _ in range(n):
    data.append(list(d for d in input()))

dx, dy = [0, 1, 0, -1], [1, 0, -1, 0]

def new_array(n):
    return [[False]*10 for _ in range(n)]
def dfs(x, y):
    ck[x][y] = True
    ret = 1
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx < 0 or nx >= n or ny < 0 or ny >= 10:
            continue
        if ck[nx][ny] or data[x][y] != data[nx][ny]:
            continue
        ret += dfs(nx, ny)
    return ret
def dfs2(x, y, val):
    ck2[x][y] = True
    data[x][y] = '0'
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx < 0 or nx >= n or ny < 0 or ny >= 10:
            continue
        if ck2[nx][ny] or data[nx][ny] != val:
            continue
        dfs2(nx, ny, val)
def down():
    for i in range(10):
        tmp = []
        for j in range(n):
            if data[j][i] != '0':
                tmp.append(data[j][i])
        for j in range(n-len(tmp)):
            data[j][i] = '0'
        for j in range(n-len(tmp), n):
            data[j][i] = tmp[j-(n-len(tmp))]
while True:
    exist = False
    ck = new_array(n)
    ck2 = new_array(n)
    for i in range(n):
        for j in range(10):
            if data[i][j] == '0' or ck[i][j]:
                continue
            res = dfs(i, j)
            if res >= k:
                dfs2(i, j, data[i][j])
                exist = True
    if not exist:
        break
    down()
for i in data:
    print(''.join(i))
