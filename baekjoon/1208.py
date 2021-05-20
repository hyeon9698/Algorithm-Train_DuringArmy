import sys
sys.stdin = open('input.txt', 'r')
n, s = map(int, input().split())
data = list(map(int, input().split()))
data.sort()
start = 0
end = len(data)-1
