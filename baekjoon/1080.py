import sys
# sys.stdin = open('input.txt', 'r')
def change(x, y, data1):
    for i in range(x-1, x+1+1):
        for j in range(y-1, y+1+1):
            data1[i][j] ^= 1
n, m = map(int, input().split())
data1 = [list(map(int, list(input()))) for _ in range(n)]
data2 = [list(map(int, list(input()))) for _ in range(n)]
cnt = 0
for i in range(1, n-1):
    for j in range(1, m-1):
        if data1[i-1][j-1] != data2[i-1][j-1]:
            change(i, j, data1)
            cnt += 1
print(cnt if data1 == data2 else -1)