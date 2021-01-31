import sys
sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline
n = int(input())
lines = [list(map(int, input().split())) for _ in range(n)]
lines.sort()
l = lines[0][0]
r = lines[0][1]
max_line = r - l
ans = 0
for x, y in lines[1:]:
    # 현재구간이면
    if r >= x:
        if r <= y:
            r = y
            max_line = r - l
    else:
        ans += max_line
        l = x
        r = y
        max_line = r - l
ans += max_line
print(ans)