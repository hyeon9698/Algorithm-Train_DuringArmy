import sys
sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline
for _ in range(int(input())):
    n = int(input())
    data = [input().rstrip('\n') for _ in range(n)]
    data.sort()
    flag = True
    for i in range(n-1):
        length = len(data[i])
        if length < len(data[i+1]):
            if data[i] == data[i+1][:length]:
                flag = False
                break
    if flag:
        print("YES")
    else:
        print("NO")
