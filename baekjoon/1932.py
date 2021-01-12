import sys
# sys.stdin = open('input.txt', 'r')
# dp 식 dp[i][j] = max(dp[i-1][j-1], dp[i-1][j]) + data[i][j]
n = int(input())
dp = [[0]*(n+1) for _ in range(n+1)]
data = []
for i in range(n):
    arr = list(map(int, input().split()))
    for j in range(n-len(arr)):
        arr.append(0)
    data.append(arr)
for i in range(n):
    for j in range(n):
        dp[i][j] = max(dp[i-1][j-1], dp[i-1][j]) + data[i][j]

print(max(max(dp)))
