n = int(input())
data = {}
for _ in range(n):
    book = input()
    if book in data:
        data[book] += 1
    else:
        data[book] = 1
target = max(data.values())
array = []
for book, number in data.items():
    if number == target:
        array.append(book)
print(sorted(array)[0])
