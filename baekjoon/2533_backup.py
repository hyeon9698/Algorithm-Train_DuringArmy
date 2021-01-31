# 독립집합 공부하기 https://developmentdiary.tistory.com/453
import sys
sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline
n = int(input())
tree = [[] for _ in range(n+1)]
for _ in range(n-1):
    u, v = map(int, input().split())
    tree[u].append(v)
    tree[v].append(u)
dp = [[0,0] for _ in range(n+1)]
check = [False for _ in range(n+1)]
def dfs(cur):
    check[cur] = True
    dp[cur][0] = 1
    dp[cur][1] = 0
    for i in tree[cur]:
        if not check[i]:
            dfs(i)
            dp[cur][0] += dp[i][1]
            dp[cur][1] += max(dp[i][0], dp[i][1])
dfs(1)
print(n-max(dp[1][0], dp[1][1]))
