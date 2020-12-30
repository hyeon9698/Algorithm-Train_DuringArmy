import time
import sys
sys.stdin = open('input.txt', 'r')
C, M = [], []
for i in range(3):
    a, b = map(int, input().split())
    C.append(a)
    M.append(b)
for i in range(100):
    idx = i % 3
    nxt = (i+1) % 3
    # print('asdf' , M[idx], M[nxt])
    M[idx], M[nxt] = max(M[idx] - (C[nxt] - M[nxt]), 0), min(C[nxt], M[nxt] + M[idx])
    # print(M[idx], M[nxt])
for i in M:
    print(i)
