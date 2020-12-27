n = int(input())
second_list = list(map(int, input().split()))
first_list = []
for i in range(n):
    first_list.append(second_list[i]*(i+1)-sum(first_list))
print(' '.join(map(str, first_list)))
