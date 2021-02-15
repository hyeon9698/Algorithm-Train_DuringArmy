import sys
from collections import deque
sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline
def bfs(start):
    q = deque([(start, 1)])
    check[start] = True
    stage = 1
    while q:
        now, prev = q.popleft()
        ans[now] = prev
        for nxt in tree[now]:
            if not check[nxt]:
                check[nxt] = True
                q.append((nxt, now))
n = int(input())
data = [list(map(int, input().split())) for _ in range(n-1)]
check = [False]*(n+1)
tree = [[] for _ in range(n+1)]
ans = [0]*(n+1)
for x, y in data:
    tree[x].append(y)
    tree[y].append(x)
bfs(1)
for i in ans[2:]:
    print(i)
