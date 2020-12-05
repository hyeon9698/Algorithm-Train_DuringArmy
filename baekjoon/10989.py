import sys

n = int(sys.stdin.readline())
data = [0] * 10001
for _ in range(n):
    x = int(sys.stdin.readline())
    data[x] += 1
for i, num in enumerate(data):
    for _ in range(num):
        print(i)

