from itertools import combinations
from itertools import permutations
import sys
sys.stdin = open('input.txt', 'r')
n, m = map(int, input().split())
list1 = [i for i in range(n, n-m, -1)]
mul1 = 1
for i in list1:
    mul1 *= i
list2 = [i for i in range(m, 0, -1)]
mul2 = 1
for i in list2:
    mul2 *= i
print(mul1//mul2)