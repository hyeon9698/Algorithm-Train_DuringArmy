import sys
from collections import deque
from collections import defaultdict
# sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline
n, m = map(int, input().split())
ind = [0 for _ in range(n+1)]
path = defaultdict(list)
for _ in range(m):
    a, b = map(int, input().split())
    path[a].append(b)
    ind[b] += 1
q = deque()
for i in range(1, n+1):
    if ind[i] == 0:
        q.append(i)
answer = []
while q:
    now = q.popleft()
    answer.append(now)
    for nxt in path[now]:
        ind[nxt] -= 1
        if ind[nxt] == 0:
            q.append(nxt)
for i in answer:
    print(i, end=' ')
