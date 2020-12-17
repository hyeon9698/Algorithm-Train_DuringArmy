import sys

n = int(input())
limit = list(map(int, input().split()))
limit.sort(reverse=True)
m = int(input())
boxes = list(map(int, input().split()))
boxes.sort(reverse=True)
result = 0
finished = [False] * m
if boxes[0] > limit[0]:
    print(-1)
    sys.exit()

while sum(finished) != m:
    index = 0
    for li in limit:
        while index < m:
            if li >= boxes[index] and not finished[index]:
                finished[index] = True
                index += 1
                break
            else:
                index += 1
    result += 1
print(result)
