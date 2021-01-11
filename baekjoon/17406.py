import sys
from itertools import permutations
sys.stdin = open('input.txt', 'r')
def rotate(data, i):
    r = i[0]
    c = i[1]
    s = i[2]
    # //2 해서 더 작은걸로 for 문 돌리기
    
n, m, k = map(int, input().split())
data = []
rotate_list = []
ans_list = []
for _ in range(n):
    data.append(list(map(int, input().split())))
for _ in range(k):
    rotate_list.append(list(map(int, input().split())))
permutations_rotate_list = list(permutations(rotate_list))
for i in permutations_rotate_list:
    rotate(data, i)
