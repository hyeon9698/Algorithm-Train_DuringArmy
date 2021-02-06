import sys
from heapq import *
sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline
n = int(input())
data = [sorted(list(map(int, input().split()))) for _ in range(n)]
d = int(input())
# data.sort()
q = []
ans = 0
for left, right in data:
    right = left + d
    tmp = 0
    for dd in data:
        if dd[1] - dd[0] <= right - left and dd[0] >= left:
            heappush(q, dd)
    while q:
        popleft, popright = heappop(q)
        if popleft > right:
            q = []
            break
        if popright <= right:
            # print(popleft, popright, left, right)
            tmp += 1
            ans = max(ans, tmp)
print(ans)