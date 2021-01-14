import sys
from copy import deepcopy
sys.stdin = open('input.txt', 'r')
n, m = map(int, input().split())
# data = [list(map(int, input().split())) for _ in range(n)]
data = [[0]*(m+1) for _ in range(n+1)]
for i in range(1, n+1):
    data[i] = [0] + (list(map(int, input().split())))
# print(data)
k = int(input())
lst = [list(map(int, input().split())) for _ in range(k)]
dp = deepcopy(data)
# print(dp)
total = 0
for i in range(1, n+1):
    for j in range(1, m+1):
        # print(dp[i][j])
        dp[i][j] += dp[i-1][j] + dp[i][j-1] - dp[i-1][j-1]
        # print(i, j, dp[i][j], dp[i-1][j], dp[i][j-1])
        # break
    # break
for i, j, x, y in lst:
    ans = dp[x][y] - dp[x][j-1] - dp[i-1][y] + dp[i-1][j-1]
    print(ans)
