def PrimeNum(N):
    for i in range(2, N):
        if N % i != 0:
            return False
        else:
            return True


N = int(input())
A = list(map(int, input().split()))

M = int(0)

for i in range(N):
    if PrimeNum(A[i]):
        M += 1

print(M)