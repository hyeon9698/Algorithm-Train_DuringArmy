n = int(input())
n = 1000 - n
count = 0


def coin(m):
    global n, count
    tmp = n // m
    count += tmp
    n = n % m


while n:
    if n >= 500:
        coin(500)
    elif n >= 100:
        coin(100)
    elif n >= 50:
        coin(50)
    elif n >= 10:
        coin(10)
    elif n >= 5:
        coin(5)
    elif n >= 1:
        coin(1)
print(count)
