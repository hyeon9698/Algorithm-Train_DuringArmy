import heapq

n = int(input())
data = []
result = 0
for _ in range(n):
    heapq.heappush(data, int(input()))
while len(data) >= 2:
    tmp1 = heapq.heappop(data)
    tmp2 = heapq.heappop(data)
    result = result + tmp1 + tmp2
    heapq.heappush(data, tmp1+tmp2)
print(result)
