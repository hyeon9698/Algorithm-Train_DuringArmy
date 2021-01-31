import sys
sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline
n = int(input())
data = [list(map(float, input().split())) for _ in range(n)]

