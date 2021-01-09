import heapq
n = int(input())
data = []
q = []
for _ in range(n):
    a, b = map(int, input().split())
    data.append((a, b))
data.sort()
for i in data:
    a = i[0]
    heapq.heappush(q, i[1])
    if a< len(q):
        heapq.heappop(q)
print(sum(q))


















# import heapq
# import sys

# # sys.stdin = open('input.txt', 'r')
# n = int(input())
# result = 0
# data = []
# hp = []
# for _ in range(n):
#     dead, reward = map(int, input().split())
#     data.append((dead, reward))
# data.sort()
# for dead, reward in data:
#     heapq.heappush(hp, reward)
#     if len(hp) > dead:
#         heapq.heappop(hp)
#         # print(hp)

# print(sum(hp))
