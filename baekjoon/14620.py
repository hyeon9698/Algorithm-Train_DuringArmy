import sys
sys.stdin = open('input.txt', 'r')

def ck(lst):
    ret = 0
    for i
n = int(input())
data = []
for _ in range(n):
    data.append(list(map(int, input().split())))
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
for i in range(n*n):
    for j in range(n*n):
        for k in range(n*n):
            