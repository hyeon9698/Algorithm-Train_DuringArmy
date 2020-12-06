n = int(input())
max = 0
min = 101
data = []
for _ in range(n):
    data.append(int(input()))
left_count = 0
right_count = 0
for num in data:
    if max < num:
        max = num
        left_count += 1
data.reverse()
max = 0
for num in data:
    if max < num:
        max = num
        right_count += 1
print(left_count)
print(right_count)
