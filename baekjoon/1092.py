n = int(input())
limit = list(map(int, input().split()))
m = int(input())
boxes = list(map(int, input().split()))
boxes.sort(reverse=True)
print(boxes)
