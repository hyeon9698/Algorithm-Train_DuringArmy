import sys

n = int(input())
k = int(input())
if k >= n:
    print(0)
    sys.exit()
data = list(map(int, input().split()))
data.sort()
length_data = []
for i in range(n-1):
    length_data.append(abs(data[i] - data[i+1]))
length_data.sort(reverse=True)
for i in range(k-1):
    length_data[i] = 0
print(sum(length_data))
