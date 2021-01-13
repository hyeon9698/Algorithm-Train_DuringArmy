import sys
sys.stdin = open('input.txt', 'r')
n = int(input())
lst = list(map(int, input().split()))

dp = [1 for i in range(n)]
array = [[x] for x in lst]
for i in range(n):
    for j in range(i):
        if lst[i] > lst[j]:
            if dp[j] + 1 > dp[i]:
                array[i] = array[j] + [lst[i]]
                dp[i] = dp[j] + 1
length = 0
flag = 0
for i in range(n):
    if length < dp[i]:
        flag = i
        length = dp[i]
print(length)
print(*array[flag])

# import sys
# from copy import deepcopy
# # sys.stdin = open('input.txt', 'r')
# n = int(input())
# data = list(map(int, input().split()))
# dp = deepcopy(data)
# rev = [i for i in range(n)]
# idx = 0
# for i in range(n):
#     for j in range(i):
#         if data[i] > data[j] and dp[i] < data[i] + dp[j]:
#             dp[i] = data[i] + dp[j]
#             rev[i] = j
#     if dp[idx] < dp[i]:
#         idx = i
# ans = []
# while rev[idx] != idx:
#     ans.append(data[idx])
#     idx = rev[idx]
# ans.append(data[idx])
# ans.sort()
# print(len(ans))
# print(' '.join(map(str, ans)))
