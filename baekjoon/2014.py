import sys
import heapq
from copy import deepcopy
k, n = map(int, input().split())
data = list(map(int, input().split()))
lst = deepcopy(data)
ck = set()
heapq.heapify(lst)
ith = 0
while ith < n:
    mn = heapq.heappop(lst)
    if mn in ck:
        continue
    ith += 1
    ck.add(mn)
    for i in data:
        if mn * i < 2 ** 32:
            heapq.heappush(lst, mn*i)
print(mn)
