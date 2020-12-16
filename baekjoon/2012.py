n = int(input())
data = []
result = 0
org_data = [i for i in range(1, n+1)]
for _ in range(n):
    data.append(int(input()))
data.sort()
for i in range(0, n):
    result += abs(data[i] - org_data[i])
print(result)
