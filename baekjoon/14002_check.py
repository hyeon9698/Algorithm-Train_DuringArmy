# https://hjp845.tistory.com/117
import sys
sys.stdin = open('input.txt', 'r')
n = int(input())
lst = list(map(int, input().split()))

dp = [1 for i in range(n)]
array = [[x] for x in lst]
print(lst)
print(array)
for i in range(n):
    for j in range(i):
        if lst[i] > lst[j]:
            if dp[j] + 1 > dp[i]:
                array[i] = array[j] + [lst[i]]
                dp[i] = dp[j] + 1
length = 0
flag = 0
for i in range(n):
    if length < dp[i]:
        flag = i
        length = dp[i]
print(length)
print(*array[flag])