from collections import deque
import sys
sys.stdin = open('input.txt', 'r')
n = int(input())
data = [[] for _ in range(n+1)]
time = [0 for _ in range(n+1)]
ori_time = [0 for _ in range(n+1)]
indegree = [0]*(n+1)
times = []
for i in range(1, n+1):
    stuff = list(map(int, input().split()))
    time[i] = stuff[0]
    ori_time[i] = stuff[0]
    for j in range(stuff[1]):
        data[stuff[j+2]].append(i)
        indegree[i] += 1
q = deque()
for i in range(1, n+1):
    if indegree[i] == 0:
        q.append((i, time[i]))
while q:
    now_index, now_time = q.popleft()
    times.append(now_time)
    for next_index in data[now_index]:
        indegree[next_index] -= 1
        time[next_index] = max(time[next_index], ori_time[next_index] + now_time)
        if indegree[next_index] == 0:
            q.append((next_index, time[next_index]))
print(max(times))
