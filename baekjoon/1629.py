import sys
sys.stdin = open('input.txt', 'r')
a, b, c = map(int, input().split())
print(pow(a, b, c))