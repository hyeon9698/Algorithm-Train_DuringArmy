import sys
sys.stdin = open('input.txt', 'r')
MAX = 100001
def bfs(start, end):
    visited = [0]*20
    q = []
    q.append((start, 0))
    ans = 0
    while q:
        now, now_cnt = q.pop()
        if now == end:
            ans += 1
            print(now_cnt)
        for nxt in (now+1, now-1, now*2):
            nxt_cnt = now_cnt + 1
            if 0 <= nxt < 20:
                if visited[nxt] and visited[nxt] <= now_cnt:
                    continue
                visited[nxt] = nxt_cnt
                print(nxt, nxt_cnt)
                q.append((nxt, nxt_cnt))
    print("ans = ", ans)

n, k = map(int ,input().split())
bfs(n, k)