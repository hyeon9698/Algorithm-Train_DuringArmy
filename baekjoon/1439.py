s = input()
one_count = 0
zero_count = 0
flag = -1
for i in s:
    if i == '0':
        if flag == 0:
            pass
        else:
            zero_count += 1
            flag = 0
    else:
        if flag == 1:
            pass
        else:
            one_count += 1
            flag = 1
print(min(zero_count, one_count))
