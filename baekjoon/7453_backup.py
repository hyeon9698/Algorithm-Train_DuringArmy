import sys
sys.stdin = open('input.txt', 'r')
n = int(input())
data = [list(map(int, input().split())) for _ in range(n)]
ans = 0
d = {}
d2 = {}
for i in range(n):
    for j in range(n):
        num = data[i][0] + data[j][1]
        if num in d:
            d[num] += 1
        else:
            d[num] = 1
for i in range(n):
    for j in range(n):
        num = data[i][2] + data[j][3]
        if num in d2:
            d2[num] += 1
        else:
            d2[num] = 1
# for i in d:
#     for j in d2:
#         if i == -j:
#             ans += 1
print(sorted(d))