import sys
sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline
def ccw(x1, y1, x2, y2, x3, y3):
    return (x1*y2 + x2*y3 + x3*y1) - (y1*x2 + y2*x3 + y3*x1)
n = int(input())
data = [list(map(int, input().split())) for _ in range(n)]
tmp = 0
for i in range(n-2):
    tmp += ccw(data[0][0], data[0][1], data[i+1][0], 
               data[i+1][1], data[i+2][0], data[i+2][1])
print(abs(tmp)/2)
