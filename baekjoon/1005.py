import sys
from collections import deque
sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline
for _ in range(int(input())):
    n, k = map(int, input().split())
    delay_time = [0] + list(map(int, input().split()))
    delay_stack_time = [0]*(n+1)
    data = [[] for _ in range(n+1)]
    indegree = [0]*(n+1)
    for _ in range(k):
        a, b = map(int, input().split())
        data[a].append(b)
        indegree[b] += 1
    q = deque()
    for i in range(n+1):
        if indegree[i] == 0:
            q.append(i)
    while q:
        now = q.popleft()
        for nxt in data[now]:
            # 기존 데이터가 더 큰지 확인 필요 더크면 변경 x
            if delay_stack_time[nxt] < delay_stack_time[now] + delay_time[now]:
                delay_stack_time[nxt] = delay_stack_time[now] + delay_time[now]
            indegree[nxt] -= 1
            if indegree[nxt] == 0:
                q.append(nxt)
    w = int(input())
    total_time = 0
    print(delay_stack_time[w] + delay_time[w])
