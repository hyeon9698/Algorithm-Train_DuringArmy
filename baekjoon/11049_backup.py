import sys
sys.stdin = open('input.txt', 'r')
n = int(input())
data = [list(map(int, input().split())) for _ in range(n)]
dp = [[0 for _ in range(n)] for _ in range(n)]
# dp[i][j] -> min i to j -> dp[i][j] = min(dp[a][b] + dp[b][c] + data[a][0]*data[a][1]*data[a+1][1])
for i in range(n):
    for j in range(n-i):
        dp[i][j] = min(dp[i][j], dp[i][k] + dp[k+1][j] + dp[k][0])