minn, maxn = map(int, input().split())
eratos = [False for _ in range(maxn-minn+2)]
i = 2
cnt = maxn - minn + 1
while i*i <= maxn:
    s = minn // i*i
    if minn % (i*i) != 0:
        s += 1
    while s*(i*i) <= maxn:
        if not eratos[s*(i*i) - minn]:
            eratos[s*(i*i) - minn] = True
            cnt -= 1
        s += 1
    i += 1

print(cnt)
