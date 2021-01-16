import sys
sys.stdin = open('input.txt', 'r')
n = int(input())
data = list(map(int, input().split()))
data.sort()
# 1 1 2 3 6 7 30
