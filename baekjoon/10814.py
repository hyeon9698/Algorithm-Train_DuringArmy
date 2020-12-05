N = int(input())
data = []
for _ in range(N):
    age, name = input().split()
    data.append((int(age), name))
data = sorted(data, key=lambda x: x[0])
for d in data:
    print(d[0], d[1])