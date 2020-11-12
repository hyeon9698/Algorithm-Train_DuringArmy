from sys import stdin

for _ in range(int(stdin.readline())):
    typing = stdin.readline().strip()
    left, right = [], []
    for typ in typing:
        if typ == '<':
            if left:
                right.append(left.pop())
        elif typ == '>':
            if right:
                left.append(right.pop())
        elif typ == '-':
            if left:
                left.pop()
        else:
            left.append(typ)
    left.extend(reversed(right))
    print(''.join(left))



#####################################

test_cases = int(input())

for _ in range(test_cases):
    left = []
    right = []
    pwd = input()

    for x in pwd:
        if x == ">":
            if right:
                left.append(right.pop()) 
        elif x=="<":
            if left:
                right.append(left.pop())
        elif x=="-":
            if left:
                left.pop()
        else:
            left.append(x)

  print("".join(left)+"".join(reversed(right)))
