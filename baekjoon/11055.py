import sys
from copy import deepcopy
sys.stdin = open('input.txt', 'r')
n = int(input())
data = list(map(int, input().split()))
dp = deepcopy(data)
# dp[i]는 i 번째중 제일 큰 수
for i in range(n):
    for j in range(i):
        if data[i] > data[j]:
            dp[i] = max(dp[i], data[i] + dp[j])
        # if data[i] > data[j]:
        #     if maxx < dp[j]:
        #         maxx = dp[j]
        #         dp[i] = maxx + data[i]
print(max(dp))
