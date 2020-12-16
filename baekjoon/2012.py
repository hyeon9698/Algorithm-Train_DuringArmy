n = int(input())
data = []
result = 0
for _ in range(n):
    data.append(int(input()))
data.sort()
for i in range(1, n+1):
    result += abs(data[i-1] - i)
print(result)
