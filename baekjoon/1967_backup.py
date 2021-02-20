from collections import deque
import sys
sys.stdin = open('input.txt', 'r')
n = int(input())
tree = [[] for _ in range(n+1)]
for _ in range(n-1):
    a, b, c = map(int, input().split())
    tree[a].append((b, c))
    tree[b].append((a, c))
# for i in range(1, n+1):
#     print(tree[i])
visited = [False]*(n+1)
q = deque([(1, 0)])
total_weight = [0 for _ in range(n+1)]
while q:
    now, now_weight = q.popleft()
    for nxt, nxt_weight in tree[q]:
        if not visited[nxt]:
            total_weight[now] = max(total_weight[now] + nxt_weight, )