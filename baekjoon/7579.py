import sys
sys.stdin = open('input.txt', 'r')
n, m = map(int, input().split())
memory_list = list(map(int, input().split()))
cost_list = list(map(int, input().split()))
result = sum(cost_list)
dp = [[0 for _ in range(sum(cost_list)+1)] for _ in range(n+1)]
for i in range(1, n+1):
    byte = memory_list[i-1]
    cost = cost_list[i-1]
    for j in range(1, sum(cost_list)+1):
        if j < cost:
            dp[i][j] = dp[i-1][j]
        else:
            dp[i][j] = max(byte + dp[i-1][j-cost], dp[i-1][j])
        if dp[i][j] >= m:
            result = min(result, j)
print(result)
