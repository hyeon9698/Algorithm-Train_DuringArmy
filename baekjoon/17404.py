import sys
sys.stdin = open('input.txt', 'r')
n = int(input())
data = [2, 0, 0]
data = data + [list(map(int, input().split())) for _ in range(n)]
print(data)