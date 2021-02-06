import sys
# sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline
a = input().strip()
b = input().strip()
dp = [[0 for i in range(len(a) + 1)] for _ in range(len(b) + 1)]
for i in range(1, len(b) + 1):
    for j in range(1, len(a) + 1):
        if a[j-1] == b[i-1]:
            dp[i][j] = dp[i-1][j-1] + 1
        else:
            dp[i][j] = max(dp[i-1][j], dp[i][j-1])
print(dp[-1][-1])
# A = list(i for i in input().strip())
# B = list(i for i in input().strip())
# dp = [[0]*(len(A)) for _ in range(len(B))]
# first = []
# second = []
# for i, strB in enumerate(B):
#     first.append(strB)
#     for j, strA in enumerate(A):
#         second.append(strA)
#         if first in second and i != 0 and j != 0:
#             print(first)
#             print(second)
#             dp[i][j] = max(dp[i-1][j], dp[i][j-1]) + 1
# for i in dp:
#     print(i)
        
