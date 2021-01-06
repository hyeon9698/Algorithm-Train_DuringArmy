import sys
# sys.stdin = open('input.txt', 'r')


def ck(lst):
    ret = 0
    flow = []
    for flower in lst:
        x = flower // n
        y = flower % n
        # print(f'x = {x} y = {y} 인 상황입니다.')
        if x == 0 or x == n-1 or y == 0 or y == n-1:
            return 10000
        for w in range(5):
            nx = x+dx[w]
            ny = y+dy[w]
            flow.append((nx, ny))
            ret += data[nx][ny]
    if len(set(flow)) == 15:
        return ret
    else:
        return 10000


n = int(input())
data = []
for _ in range(n):
    data.append(list(map(int, input().split())))
dx = [0, 0, 1, 0, -1]
dy = [0, 1, 0, -1, 0]
ans = 10000
for i in range(n*n):
    for j in range(i+1, n*n):
        for k in range(j+1, n*n):
            ans = min(ans, ck([i, j, k]))
print(ans)
