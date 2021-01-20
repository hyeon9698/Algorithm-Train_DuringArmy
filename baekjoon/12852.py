n = int(input())
data = []
while n > 1:
    data.append(n)
    if n%3 == 0:
        n /= 3
    elif n%2==0:
        n/=2
    else:
        n-=1
print(data)