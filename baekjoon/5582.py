import sys
sys.stdin = open('input.txt', 'r')
x = " " + input()
y = " " + input()
dp = [[0 for _ in range(len(x))] for _ in range(len(y))]
for i in range(1, len(y)):
    for j in range(1, len(x)):
        if y[i] == x[j]:
            dp[i][j] = dp[i-1][j-1] + 1
max_num = 0
for i in dp:
    max_num = max(max_num, max(i))
print(max_num)
