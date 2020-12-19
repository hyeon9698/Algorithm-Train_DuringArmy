import heapq
import sys

# sys.stdin = open('input.txt', 'r')
n = int(input())
result = 0
data = []
hp = []
for _ in range(n):
    dead, reward = map(int, input().split())
    data.append((dead, reward))
data.sort()
for dead, reward in data:
    heapq.heappush(hp, reward)
    if len(hp) > dead:
        heapq.heappop(hp)
        # print(hp)

print(sum(hp))
