from itertools import combinations
import sys
from copy import deepcopy
sys.stdin = open('input.txt','r')
def dfs():
    if len(stack) == m:
        if stack not in ans:
            _list = deepcopy(stack)
            ans.append(_list)
        return
    for num in data:
        if stack:
            if stack[-1] > num:
                continue
        stack.append(num)
        dfs()
        stack.pop()
n, m = map(int, input().split())
stack = []
ans = []
data = list(map(int, input().split()))
data.sort()
dfs()
for i in ans:
    print(' '.join(str(k) for k in i))