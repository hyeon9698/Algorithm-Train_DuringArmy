import sys
sys.stdin = open('input.txt', 'r')
def bfs(start, end):
    cnt = 0
    min_cnt = sys.maxsize
    q = []
    q.append((start, 1))
    while q:
        now, now_cnt = q.pop()
        # print(now, now_cnt)
        if now == end:
            if min_cnt > now_cnt:
                min_cnt = now_cnt
        if now*2 <= end:
            q.append((now*2, now_cnt + 1))
        if now*10 + 1 <= end:
            q.append((now*10 + 1, now_cnt + 1))
    return min_cnt if min_cnt != sys.maxsize else -1
    
a, b = map(int, input().split())
print(bfs(a, b))