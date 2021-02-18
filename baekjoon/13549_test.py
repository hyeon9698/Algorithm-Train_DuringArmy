from collections import deque

def bfs():
    q = deque([n])
    while q:
        x = q.popleft()
        if x == k:
            return array[x]
        for nx in (x-1, x+1, 2*x):
            if 0 <= nx < MAX and not array[nx]:
                if nx == 2*x and x != 0:
                    array[nx] = array[x] 
                    q.appendleft(nx) # 2*X 가 더 높은 우선순위를 가지기 위함
                else:
                    array[nx] = array[x] + 1
                    q.append(nx)
    
MAX = 100001
n, k = map(int, input().split())
array = [0] * MAX
print(bfs())