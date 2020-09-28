n = int(input())
data = []
answer = []
for _ in range(n):
    x = int(input())
    data.append(x)    
index = []
NUMBER = 1
flag = True
for num in data:
    while True:
        if not index:
            if NUMBER <= n:
                index.append(NUMBER)
                answer.append('+')
                NUMBER+=1
            else:
                break
        elif index[-1] < num:
            index.append(NUMBER)
            answer.append('+')
            NUMBER+=1
        elif index[-1] == num:
            index.pop()
            answer.append('-')
            break
        else:
            flag = False
            break
if flag:
    
    for ans in answer:
        print(ans)
else:
    print('NO')
