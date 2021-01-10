from collections import deque
import sys
sys.stdin = open('input.txt', 'r')
n, k = map(int, input().split())
data = []
for _ in range(n):
    data.append(list(int(d) for d in input()))

dx, dy = [0, 1, 0, -1], [1, 0, -1, 0]

def new_array(n):
    return [[False]*10 for _ in range(n)]
def dfs(x, y):
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx < 0 or nx >= n or ny < 0 or ny >= 10:
            continue
        if ck[nx][ny] or dfs[x][y] != dfs[xx][yy]:
            continue
        
def dfs2(x, y):
    pass
def down():
    pass
while True:
    exist = False
    for i in range(n):
        for j in range(10):
            if data[i][j] == 0 or ck[i][j]:
                continue
            res = dfs(i, j)
            if res >= k:
                dfs2(i, j)
                exist = True
    if not exist:
        break
    down()
def same_number_check():
    
def disappear_same_number():
    pass
def gravity():
    new_data = []
    zero_data = [[0]*10 for _ in range(n)]
    for i in range(10):
        for j in range(n-1, -1, -1):
            q = deque()
            if data[j][i] != 0:
                q.append(data[j][i])
        new_data.append(list(q))
# while True:
#     if same_number():
#         disappear_same_number()
#         gravity()
#     else:
#         break
def print_data():
    global data
    for i in range(n):
        for j in range(10):
            print(data[i][j], end='')
        print()
print_data()
print('gravity start =====')
# data = gravity()
# print_data()
