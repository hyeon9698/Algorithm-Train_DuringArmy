S = input()
tmp = ""
ck = False
for i in S:
    if i == ' ':
        if not ck:
            print(tmp[::-1], end=' ')
            tmp = ""
        else:
            tmp += i
    elif i == '<':
        if tmp:
            print(tmp[::-1], end='')
            tmp = ""
        ck = True
    elif i == '>':
        print(f'<{tmp}>', end='')
        ck = False
        tmp = ""
    else:  # 알파벳과 숫자
        tmp += i

if tmp:
    print(tmp[::-1])
