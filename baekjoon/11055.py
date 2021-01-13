import sys
from copy import deepcopy
sys.stdin = open('input.txt', 'r')
n = int(input())
data = list(map(int, input().split()))
dp = deepcopy(data)
maxx = 0
# dp[i]는 i 번째중 제일 큰 수
for i in range(n):
    maxx = 0
    for j in range(i-1, -1, -1):
        if data[i] > data[j]:
            if maxx < dp[j]:
                maxx = dp[j]
                dp[i] = maxx + data[i]
            
print(max(dp))