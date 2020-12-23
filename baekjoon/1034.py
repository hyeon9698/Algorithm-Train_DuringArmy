n, m = map(int, input().split())
arr = [input() for _ in range(n)]
k = int(input())
cnt = [0]*n
if k%2:
    for i in range(n):
        zero_cnt = arr[i].count('0')
        if zero_cnt%2 and zero_cnt <= k:
            for j in range(n):
                if arr[i] == arr[j]:
                    cnt[i] += 1
else:
    for i in range(n):
        zero_cnt = arr[i].count('0')
        if not zero_cnt%2 and zero_cnt <= k:
            for j in range(n):
                if arr[i] == arr[j]:
                    cnt[i] += 1
print(max(cnt))
