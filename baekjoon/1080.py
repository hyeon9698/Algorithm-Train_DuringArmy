import sys
# sys.stdin = open('input.txt', 'r')
def is_same():
    for i in range(n):
        for j in range(m):
            if data1[i][j] != data2[i][j]:
                return False
    return True
def change(x, y):
    for i in range(x-1, x+1+1):
        for j in range(y-1, y+1+1):
            data1[i][j] = data1[i][j]*(-1)+1
n, m = map(int, input().split())
data1 = [list(map(int, list(input()))) for _ in range(n)]
data2 = [list(map(int, list(input()))) for _ in range(n)]
cnt = 0
for i in range(1, n-1):
    for j in range(1, m-1):
        if data1[i-1][j-1] != data2[i-1][j-1]:
            change(i, j)
            cnt += 1
if not is_same():
    print(-1)
else:
    print(cnt)
