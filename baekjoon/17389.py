n = int(input())
data = input()
bonus = 0
total = 0
for i, correct in enumerate(data):
    if correct == 'O':
        total += i+1 + bonus
        bonus += 1
    else:
        bonus = 0
print(total)
