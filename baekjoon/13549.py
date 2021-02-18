from collections import deque
import sys
sys.stdin = open('input.txt', 'r')
def bfs(n, k):
    q = deque([(n, 0)])
    while q:
        now, cnt = q.popleft()
        if now == k:
            return cnt
        for nxt in (now*2, now+1, now-1):
            if 0 <= nxt <= 100000:
                if not visited[nxt]:
                    visited[nxt] = True
                    # print(nxt, cnt+1)
                    if nxt == now*2:
                        q.append((nxt, cnt))
                    else:
                        q.append((nxt, cnt+1))
n, k = map(int, input().split())
visited = [False]*(1000000)
print(bfs(n, k))