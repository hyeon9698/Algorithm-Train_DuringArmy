def numreturn(numberlist):
    newnewnum = []
    for i in range(len(numberlist)-1):
        number = numberlist[i]+numberlist[i+1]
        if number > 9:
            number = number % 10
        newnewnum.append(number)
    return newnewnum


n, m = map(int, input().split())
nameA, nameB = map(str, input().split())
newName = ''
newName = ''
numlist = []
alph = [chr(i) for i in range(65, 91)]
numnum = [3, 2, 1, 2, 4, 3, 1, 3, 1, 1, 3, 1, 3, 2, 1,
          2, 2, 2, 1, 2, 1, 1, 1, 2, 2, 1]
for i in range(min(len(nameA), len(nameB))):
    newName += nameA[i]
    newName += nameB[i]
if len(nameA) > len(nameB):
    newName += nameA[i+1:]
else:
    newName += nameB[i+1:]
for letter in newName:
    numlist.append(numnum[ord(letter)-ord('A')])
newnewnewnum = numlist
while len(newnewnewnum) > 2:
    newnewnewnum = numreturn(newnewnewnum)
if newnewnewnum[0] == 0:
    newnewnewnum.remove(0)
print(''.join(map(str, newnewnewnum))+'%')
