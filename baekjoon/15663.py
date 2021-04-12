from itertools import permutations
import sys
sys.stdin = open('input.txt', 'r')
n, m = map(int, input().split())
data = list(map(int, input().split()))
data.sort()
# set_nums = set()
# for i, nums in enumerate(permutations(data, m)):
#     if i == 0:
#         print(' '.join([str(k) for k in nums]))
#         set_nums.add(nums)
#         continue
#     if nums not in set_nums:
#         print(' '.join([str(k) for k in nums]))
#         set_nums.add(nums)
ans = []
for nums in permutations(data, m):
    ans.append(nums)
ans = sorted(set(ans))
for i in ans:
    print(' '.join(str(k) for k in i))