import sys

N, M = map(int, input().split())
n_p = 1
p1 = {}
p2 = {}

for _ in range(N):
    name = str(sys.stdin.readline()).strip()
    p1[n_p] = name
    p2[name] = n_p
    n_p += 1

answer = []
for _ in range(M):
    pokemon = str(sys.stdin.readline()).strip()
    try:
        print(p1[int(pokemon)])
    except:
        print(p2[pokemon])
