n = int(input())
a = 0
b = 1
while n:
    a, b = b, a+b
    n -= 1
print(a)


# def fibo(n):
#     if n == 0:
#         return 0
#     if n == 1:
#         return 1
#     return fibo(n-1) + fibo(n-2)


# print(fibo(int(input())))