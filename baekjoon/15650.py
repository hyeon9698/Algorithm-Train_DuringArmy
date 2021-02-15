from itertools import combinations
import sys
sys.stdin = open('input.txt', 'r')
n, m = map(int, input().split())
data = [i for i in range(1, n+1)]
# print(data)
a = combinations(data, m)
for i in a:
    print(' '.join(map(str, i)))
