import sys
sys.stdin = open('input.txt', 'r')
n = int(input())
data = []
indegree = [0]*(n+1)
for i in range(1, n+1):
    stuff = list(map(int, input().split()))
    
    for _ in range(stuff[1]):
