import itertools
dif = 0
min = 1e9
n, m = map(int, input().split())
data = list(map(int, input().split()))
nums = itertools.combinations(data,3)
for num in nums:
    total =0
    for x in num:
        total += x
    if m-total >= 0:
        if(m-total)<min:
            min = m-total
            answer = total
print(answer)
