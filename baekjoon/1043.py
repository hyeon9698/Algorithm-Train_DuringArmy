import sys
sys.stdin = open(input.txt",'r')
N, M = map(int, input().split())
k = int(input())
cnt = [0]*N
if K%2:
  for i in range(N):
    zero_cnt = arr[i].count('0')
    if zero_cnt%2 and zero_cnt <= K:
      for j in range(N):
        if arr[i] == arr[j]:
          cnt[i] += 1
else:
  for i in range(N):
