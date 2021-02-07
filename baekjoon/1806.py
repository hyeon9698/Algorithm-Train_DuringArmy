import sys
sys.stdin = open('input.txt', 'r')
n, s = map(int, input().split())
data = list(map(int, input().split()))
total = 0
sum_data = [0]
for i in data:
    total += i
    sum_data.append(total)
num = 0
Flag = False
ans = []
def check(start_index):
    global Flag
    SUM = 0
    left_pointer = start_index
    right_pointer = start_index
    while left_pointer <= right_pointer and left_pointer < n and right_pointer < n:
        # print(left_pointer, right_pointer)
        SUM = sum_data[right_pointer+1] - sum_data[left_pointer]
        # print(SUM)
        if SUM < s:
            right_pointer += 1
        elif SUM > s:
            ans.append(right_pointer-left_pointer+1)
            left_pointer += 1
        else:
            ans.append(right_pointer-left_pointer+1)
            right_pointer += 1
    return right_pointer + 1
while num < n:
    num = check(num)
if ans:
    print(min(ans))
else:
    print(0)
