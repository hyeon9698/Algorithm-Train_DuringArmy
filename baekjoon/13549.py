from collections import deque
from heapq import *
import sys
sys.stdin = open('input.txt', 'r')
def bfs(n, k):
    q = deque([n])
    while q:
        now = q.popleft()
        if now == k:
            return count_list[now]
        for nxt in (now-1, now+1, now*2):
            if 0 <= nxt <= 100000 and not count_list[nxt]:
                if nxt == now*2 and now != 0:
                    count_list[nxt] = count_list[now]
                    q.appendleft(nxt)
                else:
                    count_list[nxt] = count_list[now] + 1
                    q.append(nxt)
# def dijkstra(start, end):
#     q = [(start, 0)]
#     heapify(q)
#     while q:
#         now, cnt = heappop(q)
#         if now == end:
#             print('finished')
#             return
#         for nxt in (now*2, now+1, now-1):
            
n, k = map(int, input().split())
count_list = [0]*(1000000)
print(bfs(n, k))