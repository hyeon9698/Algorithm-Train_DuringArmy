from collections import deque
import sys
sys.stdin = open('input.txt', 'r')
n, k = map(int, input().split())
data = []
for _ in range(n):
    data.append(list(int(d) for d in input()))
def same_number():
    pass
def disappear_same_number():
    pass
def gravity():
    new_data = []
    zero_data = [[0]*10 for _ in range(n)]
    for i in range(10):
        for j in range(n-1, -1, -1):
            q = deque()
            if data[j][i] != 0:
                q.append(data[j][i])
        new_data.append(list(q))
    for i in range()
    new_data = zero_data + new_data
    return new_data
# while True:
#     if same_number():
#         disappear_same_number()
#         gravity()
#     else:
#         break
def print_data():
    global data
    for i in range(n):
        for j in range(10):
            print(data[i][j], end='')
        print()
print_data()
print('gravity start =====')
data = gravity()
print_data()
