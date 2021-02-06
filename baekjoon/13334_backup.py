# import sys
# from heapq import *
# sys.stdin = open('input.txt', 'r')
# input = sys.stdin.readline
# n = int(input())
# data = [sorted(list(map(int, input().split()))) for _ in range(n)]
# d = int(input())
# data.sort()
# q = []
# ans = 0
# answer = 0
# heap = []
# for road in data:
#     if not heap:
#         heappush(heap, road)
#     else:
#         while heap[0][0] < road[1] - d:
#             heappop(heap)
#             if not heap:
#                 break
#         heappush(heap, road)
#     answer = max(answer, len(heap))

# print(answer)
import sys
import heapq
# import sys
sys.stdin = open('input.txt', 'r')
n = int(sys.stdin.readline())
road_info = []
for _ in range(n):
    road = list(map(int, sys.stdin.readline().split()))
    road_info.append(road)

d = int(sys.stdin.readline())
roads = []
for road in road_info:
    house, office = road
    if abs(house - office) <= d:
        road = sorted(road)
        roads.append(road)
roads.sort(key=lambda x:x[1])

answer = 0
heap = []
for road in roads:
    if not heap:
        heapq.heappush(heap, road)
    else:
        while heap[0][0] < road[1] - d:
            heapq.heappop(heap)
            if not heap:
                break
        heapq.heappush(heap, road)
    print(heap)
    answer = max(answer, len(heap))

print(answer)