from itertools import combinations

l, c = map(int, input().split())
data = list(map(str, input().split()))
aeiou = ['a', 'e', 'i', 'o', 'u']
data.sort()
no_aeiou_count = 0
flag = False
for i in list(combinations(data, l)):
    no_aeiou_count = 0
    flag = False
    for j in range(len(i)):
        if i[j] in aeiou:
            flag = True
        else:
            no_aeiou_count += 1
    if no_aeiou_count >= 2 and flag:
        print(''.join(i))
