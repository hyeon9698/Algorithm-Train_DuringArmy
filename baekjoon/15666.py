from itertools import combinations
import sys
# sys.stdin = open('input.txt','r')
def dfs():
    if len(stack) == m:
        ans.append(stack)
        return
    for num in data:
        if not stack:
            stack.append(num)
            print('h')
        elif num < stack[-1]:
            print('h')
            continue
        stack.append(num)
        dfs()
        stack.pop()
# n, m = map(int, input().split())
n,m = 4, 2
stack = []
ans = []
data = [9,7,9,1]#list(map(int, input().split()))
data.sort()
dfs()