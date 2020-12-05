# 이분탐색
# N = int(input())
# data = list(map(int, input().split()))
# M = int(input())
# find = list(map(int, input().split()))
# data.sort()
# for findnum in find:
#     flag = False
#     left = 0
#     right = len(data) - 1
#     while left <= right:
#         mid = (left + right) // 2
#         if data[mid] > findnum:
#             right = mid - 1
#         elif data[mid] < findnum:
#             left = mid + 1
#         else:
#             flag = True
#             print(1)
#             break
#     if not flag:
#         print(0)

# 다른 풀이
N = int(input())
data = set(map(int, input().split()))
M = int(input())
find = list(map(int, input().split()))
for findnum in find:
    if findnum in data:
        print(1)
    else:
        print(0)

