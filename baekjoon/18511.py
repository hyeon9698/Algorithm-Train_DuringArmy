def dfs(result):
    global ans
    if result > n:
        return
    ans = max(ans, result)
    for i in data:
        dfs(result*10 + i)
n, k = map(int, input().split())
data = list(map(int, input().split()))
ans = 0
dfs(0)
print(ans)
