n = int(input())
i = 1
result = 0
while n != 0:
    if n >= i:
        n -= i
        result += 1
        i += 1
    else:
        i = 1
print(result)
