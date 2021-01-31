import sys
sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline
n = int(input())
data = list(map(int, input().split()))
dp = [1]*(n)

