import sys
from itertools import permutations
sys.stdin = open('input.txt', 'r')
n = int(input())
data = list(map(int, input().split()))
cal_list = list(map(int, input().split()))
list_list = []
arr = ['+', '-', '*', '/']
calculation_list = []
final_cal_this = []
min_n = sys.maxsize
max_n = -sys.maxsize
for k, n in enumerate(cal_list):
    for i in range(n):
        list_list.append(arr[k])
for lst in permutations(list_list):
    calculation_list.append(list(lst))
    k = 0
    cal_this = []
    for cc in list(lst):
        cal_this.append(data[k])
        cal_this.append(cc)
        k += 1
    cal_this.append(data[k])
    final_cal_this.append(cal_this)
for cal in final_cal_this:
    string = ''.join(map(str, cal))
    total = int(string[0])
    cal_l = []
    for s in string[1:]:
        if s == '+':
            cal_l.append(s)
        elif s == '-':
            cal_l.append(s)
        elif s == '*':
            cal_l.append(s)
        elif s == '/':
            cal_l.append('//')
        else:
            c = cal_l.pop()
            if c == '//' and total < 0:
                    txt = str(-total) + c + s
                    total = -eval(txt)
            else:
                txt = str(total) + c + s
                # print(txt)
                total = eval(txt)
                # print('total=', total)
    if total < min_n:
        min_n = total
    if total > max_n:
        max_n = total
print(max_n)
print(min_n)