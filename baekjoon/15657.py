import sys
from itertools import product

def dfs():
    if len(stack) == m:
        print(' '.join(map(str, stack)))
        return
    for i in data:
        if stack:
            if stack[-1] > i:
                continue
        stack.append(i)
        dfs()
        stack.pop()
sys.stdin = open('input.txt','r')
n, m = map(int, input().split())
data = list(map(int, input().split()))
data.sort()
stack = []
dfs()
# data.sort()
# flag = True
# for i in product(data, repeat=m):
#     for k in range(1, m):
#         if i[k-1] > i[k]:
#             flag = False
#     if flag:
#         print(' '.join(map(str, i)))
#     flag = True
