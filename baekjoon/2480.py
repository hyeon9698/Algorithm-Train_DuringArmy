x, y, z = map(int, input().split())
data = []
data.append(x)
data.append(y)
data.append(z)
if x == y and y == z:
    print(10000+x*1000)
elif len(set(data)) == 2:
    if x==y:
        print(1000+x*100)
    elif y==z:
        print(1000+y*100)
    else:
        print(1000+x*100)
else:
    print(max(x,y,z)*100)
