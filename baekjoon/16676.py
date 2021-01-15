n = input()
S = '1'*len(n)
if len(n) == 1:
    print(1)
elif int(n) >= int(S):
    print(len(n))
else:
    print(len(n)-1)
