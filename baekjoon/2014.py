import sys
import heapq
from copy import deepcopy
# sys.stdin = open('input.txt', 'r')
# def check(num, data):
#     while num != 1:
#         flag = False
#         for prime_number in data[::-1]:
#             if num % prime_number == 0:
#                 num = num / prime_number
#                 flag = True
#         if not flag:
#             break
#     return flag
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
# cnt = 0
# ans = []
# for i in range(min(data), 2 ** 31):
#     if check(i, data):
#         cnt += 1
#         data.append(i)
#         ans.append(i)
#     if cnt == n:
#         break
# print(ans[-1])
