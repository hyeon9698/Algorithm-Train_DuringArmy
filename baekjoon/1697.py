from collections import deque


def bfs(v):
    q = deque([v])
    while q:
        now = q.popleft()
        if now == k:
            return array[now]
        for next_val in (now + 1, now - 1, now*2):
            if 0 <= next_val < 100001 and not array[next_val]:
                array[next_val] = array[now] + 1
                q.append(next_val)


n, k = map(int, input().split())
array = [0] * (100001)
print(bfs(n))
