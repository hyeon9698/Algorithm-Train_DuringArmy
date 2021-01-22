import sys
# sys.stdin = open('input.txt', 'r')
N = int(input())
data = list(map(int, input().split()))
first_index = 0
last_index = len(data)-1
most_number = 1000000000
while True:
    if first_index > last_index:
        break
    number = data[first_index] + data[last_index]
    # if number == 0:
    #     print(data[first_index], data[last_index])
    #     break
    # print(f'number은 {number} data[fir] = {data[first_index]} data[las] = {data[last_index]}')
    if abs(most_number) > abs(number):
        F = first_index
        L = last_index
        # print("abs문에 들어왔습니다 ",F, L)
        most_number = number
    if number > 0:
        last_index -= 1
    elif number < 0:
        first_index += 1
print(data[F], data[L])