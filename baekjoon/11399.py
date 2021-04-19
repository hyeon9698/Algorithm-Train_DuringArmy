import sys
sys.stdin = open('input.txt', 'r')
n = int(input())
data = list(map(int, input().split()))
data.sort()
_list = [0]*n
total = data[0]
_list[0] = data[0]
for i in range(1,n):
    _list[i] = _list[i-1]+data[i]
    total += _list[i]
print(total)