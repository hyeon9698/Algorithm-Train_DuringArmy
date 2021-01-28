from collections import deque
import sys
sys.stdin = open('input.txt', 'r')
n, m, k = map(int, input().split())
price_data = list(map(int, input().split()))
friends = [[]*(n+1)]
indegree = [0]*(n+1)
for _ in range(m):
    a, b = map(int, input().split())
    friends[a].append(b)
    indegree[b] += 1
q = deque()
for i in range(1, n+1):
    if indegree[i] == 0:
        q.append(i)
while q:
    now = q.popleft()
    