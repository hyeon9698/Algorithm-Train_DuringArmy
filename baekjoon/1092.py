n = int(input())
limit = list(map(int, input().split()))
limit.sort(reverse=True)
m = int(input())
boxes = list(map(int, input().split()))
boxes.sort(reverse=True)
for li in limit:
    for box in boxes:
        if li >= box:
            pass
        elif 