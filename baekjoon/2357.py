import sys
sys.stdin = open('input.txt', 'r')
n, m = map(int, input().split())
data = [0] + [int(input()) for _ in range(n)]
array = [list(map(int, input().split())) for _ in range(m)]
for start, end in array:
    # print(start, end)
    min_number = min(data[start:end+1])
    max_number = max(data[start:end+1])
    print(min_number, max_number)
