from collections import deque
import sys
input = sys.stdin.readline
def bfs(n):
    q = deque([n])
    visited[n] = True
    while q:
        now = q.popleft()
        if now == k:
            return ar[now]
        for i in (now-1, now+1, now*2):
            if 0<=i<MAX and 0<=i<MAX and not visited[i]:
                visited[i] = True
                ar[i] = ar[now] + 1
                q.append(i)
n, k = map(int, input().split())
MAX = 100001
ar = [0]*MAX
visited = [False]*(MAX)
print(bfs(n))























# from collections import deque


# def bfs(v):
#     q = deque([v])
#     while q:
#         now = q.popleft()
#         if now == k:
#             return array[now]
#         for next_val in (now + 1, now - 1, now*2):
#             if 0 <= next_val < 100001 and not array[next_val]:
#                 array[next_val] = array[now] + 1
#                 q.append(next_val)


# n, k = map(int, input().split())
# array = [0] * (100001)
# print(bfs(n))
