import sys
from collections import deque
from collections import defaultdict
# sys.stdin = open('input.txt', 'r')
n, m = map(int, input().split())
ind = [0 for _ in range(n+1)]
path = defaultdict(list)
for _ in range(m):
    singers = list(map(int, input().split()))
    for i in range(2, singers[0]+1):
        ind[singers[i]] += 1
    for i in range(1, singers[0]):
        path[singers[i]].append(singers[i+1])
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
if len(answer) == n:
    for i in answer:
        print(i)
else:
    print(0)
