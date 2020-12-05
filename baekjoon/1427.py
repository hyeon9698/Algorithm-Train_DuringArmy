data = input()
numdata = []
for alpha in data:
    numdata.append(int(alpha))
numdata.sort(reverse=True)
# print(''.join(numdata))
print(''.join(map(str, numdata)))