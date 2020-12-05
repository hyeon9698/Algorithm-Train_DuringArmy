N = int(input())
data = []
for _ in range(N):
    cor = input().split()
    data.append((int(cor[0]), int(cor[1])))
data.sort()
for i in data:
    print(i[0], i[1])
