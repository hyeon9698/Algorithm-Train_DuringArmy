# import sys
# sys.stdin = open('input.txt', 'r')

n, l, k = map(int, input().split())
total = 0
data = {i: (0, 0) for i in range(n)}
for i in range(n):
    easy, hard = map(int, input().split())
    data[i] = (easy, hard)
for i in range(n):
    if data[i][1] <= l and k:
        total += 140
        del data[i]
        k -= 1
leftnum = [i for i in data]
for i in leftnum:
    if data[i][0] <= l and k:
        total += 100
        del data[i]
        k -= 1
# print(data)
print(total)
