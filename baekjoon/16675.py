import sys
# sys.stdin = open('input.txt', 'r')
ml, mr, tl, tr = input().split()
if ml != mr and tl != tr:
    print('?')
if ml == mr:
    if ml == 'R':
        if tl == 'P' or tr == 'P':
            print('TK')
    elif ml == 'S':
        if tl == 'R' or tr == 'R':
            print('TK')
    elif ml == 'P':
        if tl == 'S' or tr == 'S':
            print('TK')
if tl == tr:
    if tl == 'R':
        if ml == 'P' or mr == 'P':
            print('MS')
    elif tl == 'S':
        if ml == 'R' or mr == 'R':
            print('MS')
    elif tl == 'P':
        if ml == 'S' or mr == 'S':
            print('MS')
