from collections import deque
import sys
sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline
for _ in range(int(input())):
    n = int(input())
    data = list(map(int, input().split()))
    graph = [[] for _ in range(n+1)]
    indegree = [0]*(n+1)
    count = 0
    for i in range(1, n+1):
        graph[i].append(data[i-1])
        indegree[data[i-1]] += 1
    q = deque()
    for i in range(1, n+1):
        if indegree[i] == 0:
            q.append(i)
    while q:
        now = q.popleft()
        count += 1
        for next_num in graph[now]:
            indegree[next_num] -= 1
            if indegree[next_num] == 0:
                q.append(next_num)
    print(count)
