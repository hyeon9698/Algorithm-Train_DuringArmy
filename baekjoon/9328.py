import sys
from collections import deque
sys.stdin = open('input.txt', 'r')
# 편하게 프린트하려고 만들어둔 함수
def printdata(data):
    for i in data:
        print(''.join(i))
def bfs(xx, yy, data, visited, h, w, keys):
    global ans
    visited[xx][yy] = True
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    q = deque([[xx, yy]])
    flag = False
    while q:
        now = q.popleft()
        x = now[0]
        y = now[1]
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx > h+1 or ny < 0 or ny > w+1 or visited[nx][ny] or data[nx][ny] == '*':
                continue
            if data[nx][ny] == '.':
                visited[nx][ny] = True
                # data[nx][ny] = '@'
                q.append([nx, ny])
            elif data[nx][ny].isupper():
                if data[nx][ny].lower() in keys:
                    visited[nx][ny] = True
                    data[nx][ny] = '.'
                    q.append([nx, ny])
            elif data[nx][ny].islower():
                # 키를 먹을 때 bfs 함수를 또 실행해야함
                flag = True
                visited[nx][ny] = True
                # data[nx][ny] = '@'
                keys.update(data[nx][ny])
                data[nx][ny] = '.'
                q.append([nx, ny])
            else:
                visited[nx][ny] = True
                data[nx][ny] = '.'
                ans += 1
                q.append([nx, ny])
    if flag:
        visited = [[False]*(w+2) for _ in range(h+2)]
        bfs(0, 0, data, visited, h, w, keys)
def process():
    global ans
    h, w = map(int, input().split())
    data = [['.']*(w+2)]
    for _ in range(h):
        new_data = ['.'] + list(input()) + ['.']
        data.append(new_data)
    data.append(list(['.']*(w+2)))
    keys = set()
    keys.update(list(input()))
    visited = [[False]*(w+2) for _ in range(h+2)]
    bfs(0, 0, data, visited, h, w, keys)
    print(ans)
for _ in range(int(input())):
    ans = 0
    process()