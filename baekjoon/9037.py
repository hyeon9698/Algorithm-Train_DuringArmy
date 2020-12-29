import sys
sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline
def pass_to_next(candy_list):
    candy_list = [c//2 for c in candy_list]
    tmp = candy_list[-1]
    for i in range(len(candy_list)-1, 0, -1):
        candy_list[i] += candy_list[i-1]
    candy_list[0] += tmp
    return candy_list
for _ in range(int(input())):
    ch_number = int(input())
    result = 0
    data = list(map(int, input().split()))
    while True:
        data = [c if c % 2 == 0 else c+1 for c in data]
        if len(set(data)) == 1:
            print(result)
            break
        data = pass_to_next(data)
        result += 1
