# 41. Ch 05. 코딩테스트 유형별 분석 (탐욕 알고리즘) - 03.
import sys
sys.stdin = open('input.txt', 'r')
n = int(input())
data = list(map(int, input().split()))
data.sort()

ans = 0
# 1 1 2 3 6 7 30
for i in data:
    if i <= ans + 1:
        ans += i
    else:
        break
print(ans+1)
