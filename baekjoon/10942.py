import sys
sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline
n = int(input())
data = [0] + list(map(int, input().split()))
m = int(input())
questions = [list(map(int, input().split())) for _ in range(m)]
dp = [[-1]*(n+1) for _ in range(n+1)]
for a, b in questions:
    if dp[a][b] == 1:
        # print('dp에 들어왔음')
        print(dp[a][b])
    else:
        if data[a:b+1] == data[b:a-1:-1]:
            for i in range((b-a)//2 + 1):
                dp[a+i][b-i] = 1
            print(1)
        else:
            print(0)
# print(data)